"""The complete rotating tens bell against the first carry in each register."""

from solid_node.node import AssemblyNode
from solid_node.motion.joints import Revolute
from solid_node.simulation import Driver
from solid_node.math import floor
from simulation.standard.printed import TensBell1
from simulation.standard.channels import ResultTens, TurnsTens
from simulation.transmission import channel_values


def first_carry(counter=False):
    channels = channel_values(6 if counter else 11, counter)(None, None)
    return lambda sources, targets: lambda turn, enabled: channels(
        9 * enabled + floor(turn), 1, turn, 0, 0)[3:6]


class CarryMesh(AssemblyNode):
    crank_turns = Driver(default=0, range=(0, 2), unit='rev')
    enabled = Driver(default=0, range=(0, 1), dtype=int)
    bell = TensBell1(turn=Revolute(axis=(0, 0, 1)))
    result = ResultTens()
    counter = TurnsTens()
    crank_turns.drives(bell.turn, ratio=-360)
    (crank_turns & enabled).drives((result.turn, result.setting, result.carry),
                                  law=first_carry())
    (crank_turns & enabled).drives((counter.turn, counter.setting, counter.carry),
                                  law=first_carry(counter=True))
