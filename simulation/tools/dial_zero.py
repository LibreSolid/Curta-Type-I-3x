"""Resolve absolute dial zero from the missing clearing teeth, not bevel pitch."""

import json
from math import radians, sin, cos, atan2, degrees
import numpy as np
from simulation.clearing_contact import ClearingContactBench
from simulation.standard.parts import ResultsDialType1, ResultsDialType2


def probe():
    model = ClearingContactBench()
    model.set_state(digit=0, clear=0)
    model.assemble()
    gap = np.array((cos(radians(-126)), sin(radians(-126)), 0))

    def visit(node, path, ancestors):
        operations = [*node.operations, *ancestors]
        if isinstance(node, (ResultsDialType1, ResultsDialType2)):
            matrix = np.eye(4)
            for operation in operations:
                matrix = operation.matrix() @ matrix
            direction = matrix[:3, :3] @ gap
            outward = -matrix[:3, 2]
            tangent = np.cross((0, 0, 1), outward)
            angle = degrees(atan2(direction @ tangent, direction[2]))
            print(json.dumps({'dial': path, 'gap_angle_from_up': angle,
                              'whole_digit_correction': round(angle/36)}), flush=True)
        for child in node.children:
            visit(child, path + '.' + child.name, operations)

    visit(model, 'Curta', [])


if __name__ == '__main__':
    probe()
