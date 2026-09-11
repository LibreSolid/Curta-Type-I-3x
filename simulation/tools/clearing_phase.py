"""Follow forward-only clearing contact independently of the candidate dial law."""

import argparse
import json
from math import radians, sin, cos
import numpy as np
import trimesh
import manifold3d as manifold
from simulation.clearing_contact import ClearingContactBench
from simulation.tools.carry_phase import solid


def probe(digit):
    model = ClearingContactBench()
    model.set_state(digit=0, clear=0)
    model.assemble()
    model.build_stls()
    strips = [solid(part.mesh) for part in model.clearing.tooth_stack.children]
    for kind, station, node in [
        ('outer', 0, model.results.p_10203_1.results_dial_type_1),
        ('inner', -40, model.results.p_10205_1.results_dial_type_2),
    ]:
        wheel = solid(node.mesh)
        axis = np.array((cos(radians(station)), sin(radians(station)), 0))
        at = 71.474057463 * axis + (0, 0, 33.9)
        position = float(digit)
        for sample in range(641):
            angle = sample / 8
            matrix = trimesh.transformations.rotation_matrix(radians(-angle), (0, 0, 1))
            moved = [strip.transform(matrix[:3]) for strip in strips]

            def blocked(value):
                turn = trimesh.transformations.rotation_matrix(radians(36*value), axis, at)
                posed = wheel.transform(turn[:3])
                for strip in moved:
                    overlap = posed ^ strip
                    assert overlap.status() == manifold.Error.NoError
                    if overlap.volume() > 0:
                        return True
                return False

            before = position
            if blocked(position):
                low, high = position, min(position + 1/36, 10)
                while blocked(high) and high < 10:
                    high = min(high + 1/36, 10)
                if blocked(high):
                    print(json.dumps({'kind': kind, 'digit': digit, 'angle': angle,
                        'position': position, 'refusal': 'No clear forward pose before zero'}), flush=True)
                    break
                for _ in range(14):
                    mid = (low + high)/2
                    if blocked(mid):
                        low = mid
                    else:
                        high = mid
                position = high
            if position != before or sample % 8 == 0:
                print(json.dumps({'kind': kind, 'digit': digit, 'angle': angle,
                                  'position': position}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digit', type=int, default=9, choices=range(10))
    probe(parser.parse_args().digit)
