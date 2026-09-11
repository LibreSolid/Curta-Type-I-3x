"""Measure the first bevel pair's phase before assigning its drive law."""

import numpy as np
import argparse
from simulation.standard.assembly import Part10203_1, Part10208_1
from simulation.tools.interference import world_solids


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fit', action='store_true', help='probe pinion seating through a tooth period')
    args = parser.parse_args()
    dial_group, shaft_group = Part10203_1(), Part10208_1()
    dial_group.assemble()
    shaft_group.assemble()
    dial = dial_group.results_dial_type_1
    matrix = np.eye(4)
    for operation in dial.operations:
        matrix = operation.matrix() @ matrix
    at = matrix[:3, 3]
    axis = matrix[:3, 2]
    wheel = world_solids(dial_group)['Curta.results_dial_type_1']
    pinion = world_solids(shaft_group)['Curta.transmission_gear_tip']
    print('dial axis', at.tolist(), axis.tolist(), flush=True)
    if args.fit:
        for drop in (0, 0.2, 0.4, 0.6, 0.8, 1.0):
            volumes = []
            for angle in range(0, 73, 6):
                posed = wheel.rotate(tuple(at), tuple(at + axis), 3 - angle / 2)
                driver = pinion.rotate((40.5, 0, 0), (40.5, 0, 1), angle)
                overlap = posed.intersect(driver.translate((0, 0, -drop)))
                assert overlap.isValid(), (drop, angle)
                volumes.append(overlap.Volume())
            print('drop', drop, 'max overlap', max(volumes), 'samples', volumes, flush=True)
    else:
        for angle in range(0, 73, 3):
            posed = wheel.rotate(tuple(at), tuple(at + axis), angle)
            overlap = posed.intersect(pinion)
            print(angle, overlap.isValid(), overlap.Volume(), flush=True)
