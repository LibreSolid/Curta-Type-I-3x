"""Check the measured first-pair seating and phase around both register banks."""

from math import atan2, degrees
import json
import sys
import numpy as np

from simulation.assemblies import RegisterCarriage
from simulation.standard.layers import Transmission
from simulation.standard.parts import TransmissionGearTip, ResultsDialType1, ResultsDialType2
from simulation.tools.interference import rigid_leaves, world_solids
from simulation.fit import TENS_SHAFT_X_CORRECTION

CARRIAGE_CENTER = np.array([0.537721035, -0.038177283, 0])
CARRIAGE_CLOCKING = 0.549916905


def placement(node):
    matrix = np.eye(4)
    for operation in node.operations:
        matrix = operation.matrix() @ matrix
    return matrix


def probe():
    shafts, registers = Transmission(), RegisterCarriage()
    shafts.assemble()
    registers.assemble()
    pinions = [(path, node, placement(node)) for path, node in rigid_leaves(shafts)
               if isinstance(node, TransmissionGearTip)]
    dials = [(path, node, placement(node)) for path, node in rigid_leaves(registers)
             if isinstance(node, (ResultsDialType1, ResultsDialType2))]
    native_shafts, native_dials = world_solids(shafts), world_solids(registers)
    reference = next(matrix for path, node, matrix in dials if 'p_10203_1.' in path)
    top_roll = degrees(atan2(reference[2, 1], reference[2, 0])) - 3

    def fit(item):
        path, node, matrix = item
        at, axis = matrix[:3, 3], matrix[:3, 2]
        pinion_path, pinion_node, pinion_matrix = min(
            pinions, key=lambda item: np.linalg.norm(item[2][:2, 3] - at[:2]))
        x, y = pinion_matrix[:2, 3]
        correction = TENS_SHAFT_X_CORRECTION if '.p_10236_1.' in pinion_path else 0
        x += correction
        clocking = degrees(atan2(y, x))
        phase = degrees(atan2(matrix[2, 1], matrix[2, 0])) - top_roll
        rotation = np.deg2rad(-CARRIAGE_CLOCKING)
        transform = np.array([[np.cos(rotation), -np.sin(rotation), 0],
                              [np.sin(rotation), np.cos(rotation), 0], [0, 0, 1]])
        at, axis = transform @ (at - CARRIAGE_CENTER), transform @ axis
        wheel = native_dials[path].translate(tuple(-CARRIAGE_CENTER))
        wheel = wheel.rotate((0, 0, 0), (0, 0, 1), -CARRIAGE_CLOCKING)
        pinion = native_shafts[pinion_path].translate((correction, 0, 0))
        measurements = []
        for drop in (0, 0.4, 0.8, 1.2, 1.6):
            volumes = []
            for angle in range(0, 73, 12):
                a = wheel.rotate(tuple(at), tuple(at + axis), phase - angle / 2)
                b = pinion.rotate((x, y, 0), (x, y, 1), clocking + angle)
                try:
                    result = a.intersect(b.translate((0, 0, -drop)))
                except ValueError as error:
                    return {'dial': path, 'shaft': pinion_path,
                            'error': str(error), 'drop': drop, 'angle': angle}
                if not result.isValid():
                    return {'dial': path, 'error': 'invalid boolean', 'drop': drop, 'angle': angle}
                volumes.append(sum(solid.Volume() for solid in result.Solids()))
            measurements.append({'drop': drop, 'max_overlap': max(volumes)})
            if max(volumes) == 0:
                break
        return {'dial': path, 'shaft': pinion_path, 'axis': axis.tolist(), 'at': at.tolist(),
                'shaft_axis': [x, y, 0], 'shaft_clocking': clocking,
                'dial_phase': phase, 'measurements': measurements}

    results = []
    for item in dials:
        result = fit(item)
        print(json.dumps(result), file=sys.stderr, flush=True)
        results.append(result)
    return results


if __name__ == '__main__':
    print(json.dumps(probe(), indent=2))
