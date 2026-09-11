"""Measure the finished cover's axial cam against the native source stop pin."""

import json
import argparse
from pathlib import Path
from simulation.curta import Curta
from simulation.tools.carry_phase import solid
from simulation.tools.interference import world_solids
from simulation.tools.compile_detents import compact


def readings(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines()
            if line.startswith('{')]


def probe(exact=False, knots=None, resume=None):
    root = Curta()
    root.set_state(**root.instructions['Rest'].targets)
    root.assemble()
    carriage = root.carriage.registers
    pin_node = carriage.carrier.upper_carriage_body_1.clearing_pin
    if exact:
        paths = ('Curta.carriage.registers.carrier.upper_carriage_body_1.clearing_pin',
                 'Curta.carriage.registers.clearing_ring.clearing_cover')
        shapes = world_solids(root, selected=set(paths))
        pin = shapes[paths[0]].translate((0, 0, pin_node.slide.value))
        cover = shapes[paths[1]]
        assert pin.isValid() and cover.isValid()
    else:
        root.build_stls()
        pin = solid(pin_node.mesh).translate((0, 0, pin_node.slide.value))
        cover = solid(carriage.clearing_ring.clearing_cover.mesh)
    angles = ([angle for angle, _ in compact([(row['angle'], row['drop'])
                                             for row in readings(knots)])]
              if knots else range(361))
    previous = {row['angle']: row for row in readings(resume)} if resume else {}
    for angle in angles:
        if angle in previous:
            print(json.dumps(previous[angle]), flush=True)
            continue
        cam = (cover.rotate((0, 0, 0), (0, 0, 1), -angle) if exact
               else cover.rotate((0, 0, -angle)))

        def blocked(drop):
            moved = pin.translate((0, 0, -drop))
            if exact:
                # Direct native separation avoids invalid near-contact Boolean
                # slivers. The target is a real .05 mm minimum surface gap.
                return moved.distance(cam) < .05
            return (moved ^ cam).volume() > 0

        lower, upper = 0, 12
        assert not blocked(upper), angle
        if blocked(lower):
            for _ in range(17):
                middle = (lower + upper)/2
                if blocked(middle):
                    lower = middle
                else:
                    upper = middle
        else:
            upper = 0
        print(json.dumps(dict(angle=angle, drop=upper + (0 if exact else .05))), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact', action='store_true')
    parser.add_argument('--knots', help='Refine the turning points of an earlier measured profile')
    parser.add_argument('--resume', help='Reuse completed measurements from an interrupted run')
    args = parser.parse_args()
    probe(args.exact, args.knots, args.resume)
