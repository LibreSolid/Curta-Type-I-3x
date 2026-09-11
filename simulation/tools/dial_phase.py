"""Measure the first bevel pair's phase before assigning its drive law."""

import numpy as np
from simulation.standard.assembly import Part10203_1, Part10208_1
from simulation.tools.interference import world_solids


if __name__ == '__main__':
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
    for angle in range(0, 73, 3):
        posed = wheel.rotate(tuple(at), tuple(at + axis), angle)
        overlap = posed.intersect(pinion)
        print(angle, overlap.isValid(), overlap.Volume(), flush=True)
