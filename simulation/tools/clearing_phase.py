"""Follow forward-only clearing contact independently of the candidate dial law."""

import argparse
import json
from math import radians, sin, cos
import numpy as np
import trimesh
import manifold3d as manifold
from simulation.clearing_contact import ClearingContactBench
from simulation.tools.carry_phase import solid


def probe(digit, lift=0, index=0, relief=0):
    model = ClearingContactBench()
    model.set_state(digit=0, clear=0)
    model.assemble()
    model.build_stls()
    strips = [solid(part.mesh).translate((0, 0, lift))
              for part in model.clearing.tooth_stack.children]
    frames = {}
    def visit(node, ancestors):
        operations = [*node.operations, *ancestors]
        matrix = np.eye(4)
        for operation in operations:
            matrix = operation.matrix() @ matrix
        frames[id(node)] = matrix
        for child in node.children:
            visit(child, operations)
    visit(model, [])
    for kind, station, node in [
        ('outer', 0, model.results.p_10203_1.results_dial_type_1),
        ('inner', -40, model.results.p_10205_1.results_dial_type_2),
    ]:
        wheel = solid(node.mesh)
        if relief:
            # Diagnostic outer-profile sanding of only the clearing gear.
            # Filling the gauge inside R4 preserves the existing axle bore.
            local = wheel.transform(np.linalg.inv(frames[id(node)])[:3])
            start, height = (18.45, 1.95) if kind == 'outer' else (21, 2.7)
            profile = local.slice(start + height/2).offset(-relief) + manifold.CrossSection.circle(4, 80)
            retained = profile.extrude(height).translate((0, 0, start))
            slab = manifold.Manifold.cylinder(height, 8, circular_segments=100).translate((0, 0, start))
            wheel = (local - (slab - retained)).transform(frames[id(node)][:3])
        axis = np.array((cos(radians(station)), sin(radians(station)), 0))
        at = 71.474057463 * axis + (0, 0, 33.9)
        position = float(digit)
        for sample in range(641):
            angle = sample / 8
            matrix = trimesh.transformations.rotation_matrix(radians(-angle), (0, 0, 1))
            moved = [strip.transform(matrix[:3]) for strip in strips]

            def blocked(value):
                turn = trimesh.transformations.rotation_matrix(radians(36*(value + index)), axis, at)
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
    parser.add_argument('--lift', type=float, default=0,
                        help='Diagnostic strip rise, before any cover-seat fit is implemented (mm)')
    parser.add_argument('--index', type=float, default=0,
                        help='Diagnostic whole-tooth dial index, independent of bevel phase')
    parser.add_argument('--relief', type=float, default=0,
                        help='Diagnostic clearing-gear outer-profile relief (mm)')
    args = parser.parse_args()
    probe(args.digit, args.lift, args.index, args.relief)
