"""Complete stepped drum and both first-channel transmission stacks."""

from solid_node.node import AssemblyNode
from solid_node.motion.joints import Revolute, Prismatic
from solid_node.simulation import Driver
from simulation.cycle import dial_positions
from simulation.fit import INPUT_CLOCKING
from simulation.prints import PrintedDrum
from simulation.standard.channels import ResultOnes, TurnsOnes


def passage(counter=False):
    return lambda sources, targets: lambda digit, turn, subtract: (
        (130 if counter else 0) + INPUT_CLOCKING +
        72 * dial_positions(0, digit, turn, subtract, 0, 0, 6 if counter else 11, counter)[0])


class Engagement(AssemblyNode):
    digit = Driver(default=0, range=(0, 9), dtype=int)
    crank_turns = Driver(default=0, range=(0, 1), unit='rev')
    subtract = Driver(default=0, range=(0, 1), dtype=int)
    drum = PrintedDrum(turn=Revolute(axis=(0, 0, 1)),
                       lift=Prismatic(axis=(0, 0, 1)))
    result = ResultOnes()
    counter = TurnsOnes()

    crank_turns.drives(drum.turn, ratio=-360)
    subtract.drives(drum.lift, ratio=9)
    digit.drives(result.setting)
    digit.drives(result.carry, ratio=0)
    digit.drives(counter.setting, ratio=0, offset=-.75)
    digit.drives(counter.carry, ratio=0)
    (digit & crank_turns & subtract).drives(result.turn, law=passage())
    (digit & crank_turns & subtract).drives(counter.turn, law=passage(counter=True))
