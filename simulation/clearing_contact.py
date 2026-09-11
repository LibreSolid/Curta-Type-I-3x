"""The installed clearing rows and seventeen dials, without common carriage lift."""

from solid_node.node import AssemblyNode
from solid_node.motion.joints import Revolute
from solid_node.simulation import Driver
from simulation.registers import ResultRegister, TurnsRegister
from simulation.mechanism import ClearingAssembly, clearing_turn


def idle(source, targets):
    return lambda digit: (0, 0, 0, 0)


class ClearingContactBench(AssemblyNode):
    digit = Driver(default=0, range=(0, 9), dtype=int)
    clear = Driver(default=0, range=(0, 1))
    results = ResultRegister()
    turns = TurnsRegister()
    clearing = ClearingAssembly(turn=Revolute(axis=(0, 0, 1)))
    digit.drives(results.value, ratio=11111111111)
    digit.drives(turns.value, ratio=111111)
    digit.drives((results.operand, results.crank_turns, results.subtract,
                  results.carriage_position), law=idle)
    digit.drives((turns.operand, turns.crank_turns, turns.subtract,
                  turns.carriage_position), law=idle)
    clear.drives(results.clear)
    clear.drives(turns.clear)
    clear.drives(clearing.turn, law=clearing_turn)
