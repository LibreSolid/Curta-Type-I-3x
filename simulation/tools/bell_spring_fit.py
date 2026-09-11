"""Measure radial hook deflection against the drum, without guessing its cavity."""

import json
import argparse
from simulation.bell_spring import BellLeafFitBench
from simulation.tools.carry_phase import solid
from simulation.tools.interference import rigid_leaves


def probe(profile=False):
    root = BellLeafFitBench()
    root.set_state(spread=0, subtract=0)
    root.assemble()
    root.build_stls()
    hooks = [solid(root.spring.right_hook.mesh), solid(root.spring.left_hook.mesh)]
    bodies = [(path, solid(part.mesh)) for path, part in rigid_leaves(root.drum)]
    if profile:
        for step in range(181):
            lift = step / 20
            drum = [body.translate((0, 0, lift)) for _, body in bodies]
            distances = []
            for side, hook in zip((1, -1), hooks):
                def blocked(distance):
                    posed = hook.translate((side*distance, 0, 0))
                    return any((posed ^ body).volume() > 0 for body in drum)
                lower, upper = 0, 8
                assert blocked(lower) and not blocked(upper), (lift, side)
                for _ in range(17):
                    middle = (lower + upper) / 2
                    if blocked(middle):
                        lower = middle
                    else:
                        upper = middle
                distances.append(upper)
            print(json.dumps(dict(lift=lift, right=distances[0], left=distances[1],
                                  spread=max(distances))), flush=True)
        return
    for lift in (0, 4.5, 9):
        for spread in (0, 2, 4, 6, 8, 10, 12, 14):
            volumes = {path: sum(max(0, (hook.translate((side*spread, 0, 0)) ^
                                        body.translate((0, 0, lift))).volume())
                                for side, hook in zip((1, -1), hooks))
                       for path, body in bodies}
            print(json.dumps(dict(lift=lift, spread=spread, overlap_mm3=volumes)), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', action='store_true')
    probe(parser.parse_args().profile)
