"""The first carry in both banks: dial pin, slider, shaft flange and reset bell."""

from simulation.carry_mesh import CarryMesh
from simulation.standard.carry import ResultsLever1, TurnsLever1
from simulation.registers import ResultRegister, TurnsRegister


def unit_operation(source, targets):
    return lambda enabled: (1, 0, 0, 0)


class CarryContactBench(CarryMesh):
    results_lever = ResultsLever1()
    turns_lever = TurnsLever1()
    results_dials = ResultRegister()
    turns_dials = TurnsRegister()

    CarryMesh.result.carry.drives(results_lever.engage)
    CarryMesh.counter.carry.drives(turns_lever.engage)
    CarryMesh.enabled.drives(results_dials.value, ratio=9)
    CarryMesh.enabled.drives(turns_dials.value, ratio=9)
    CarryMesh.crank_turns.drives(results_dials.crank_turns)
    CarryMesh.crank_turns.drives(turns_dials.crank_turns)
    CarryMesh.enabled.drives((results_dials.operand, results_dials.subtract,
                              results_dials.carriage_position, results_dials.clear),
                             law=unit_operation)
    CarryMesh.enabled.drives((turns_dials.operand, turns_dials.subtract,
                              turns_dials.carriage_position, turns_dials.clear),
                             law=unit_operation)
