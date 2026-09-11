"""Test constant-pitch clearing laws against both complete installed tooth rows."""

import json
import argparse
from math import radians, degrees, sin, cos
import numpy as np
import trimesh
import manifold3d as manifold
from simulation.clearing_contact import ClearingContactBench
from simulation.tools.carry_phase import solid


def probe(broad=False, only_kind=None, only_digit=None):
    model = ClearingContactBench()
    model.set_state(digit=0, clear=0)
    model.assemble()
    model.build_stls()
    strips = [solid(part.mesh) for part in model.clearing.tooth_stack.children]
    angles = np.arange(0, 70.01, .5)
    posed = []
    for angle in angles:
        matrix = trimesh.transformations.rotation_matrix(radians(-angle), (0, 0, 1))
        posed.append([part.transform(matrix[:3]) for part in strips])
    for kind, station, radius, node in [
        ('outer', 0, 52, model.results.p_10203_1.results_dial_type_1),
        ('inner', -40, 49.55, model.results.p_10205_1.results_dial_type_2),
    ]:
        if only_kind and kind != only_kind:
            continue
        wheel = solid(node.mesh)
        axis = np.array((cos(radians(station)), sin(radians(station)), 0))
        at = 71.474057463 * axis + (0, 0, 33.9)
        pitch = degrees(3.75/radius)
        for digit in range(1, 10):
            if only_digit and digit != only_digit:
                continue
            scores = []
            # The broad survey found the first-row phase near 9.75°. Subsequent
            # tooth periods are physically equivalent only after entry clears.
            base = 9.75 if kind == 'outer' else 10.5
            candidates = (np.arange(8, 23.01, .25) if broad else
                          [base + tooth*pitch + delta for tooth in range(3)
                           for delta in (-.1, -.05, 0, .05, .1)])
            for start in candidates:
                worst, total = 0, 0
                for angle, rows in zip(angles, posed):
                    value = digit + np.clip((angle - start)/pitch, 0, 10 - digit)
                    turn = trimesh.transformations.rotation_matrix(radians(36*value), axis, at)
                    dial = wheel.transform(turn[:3])
                    for row in rows:
                        overlap = row ^ dial
                        assert overlap.status() == manifold.Error.NoError
                        volume = overlap.volume()
                        worst = max(worst, volume)
                        total += max(0, volume)
                scores.append({'kind': kind, 'digit': digit, 'start': float(start),
                               'pitch': pitch, 'maximum_mm3': worst, 'total_mm3': total})
            for candidate in sorted(scores, key=lambda value: (value['maximum_mm3'], value['total_mm3']))[:3]:
                print(json.dumps(candidate), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--broad', action='store_true')
    parser.add_argument('--kind', choices=('outer', 'inner'))
    parser.add_argument('--digit', type=int, choices=range(1, 10))
    args = parser.parse_args()
    probe(args.broad, args.kind, args.digit)
