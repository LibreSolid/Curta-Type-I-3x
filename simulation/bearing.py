"""The bevel fit must retain clearance to the frame's shaft bearing."""

from solid_node.node import AssemblyNode
from solid_node.simulation import Driver
from simulation.standard.parts import MainBody
from simulation.standard.channels import ResultOnes


class ShaftBearing(AssemblyNode):
    turn = Driver(default=0, range=(0, 360), unit='deg')
    body = MainBody()
    shaft = ResultOnes()
    turn.drives(shaft.turn)
    turn.drives(shaft.setting, ratio=0)
    turn.drives(shaft.carry, ratio=0)
