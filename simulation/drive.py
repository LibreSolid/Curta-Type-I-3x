"""Crank, stepped drum and one input channel, using the source's rest frames."""

from solid_node.node import AssemblyNode
from solid_node.simulation import Driver
from solid_node.motion.joints import Revolute, Prismatic
from solid_node.motion.ports import Port
from simulation.standard.assembly import (
    CrankHandle1, MainAxleStepDrum1, DigitSelectorAxle1,
    SelectorShaftTop1_419054, SelectorKnob1_419057,
)
from simulation.standard.parts import SelectorShaftBottom


class Crank(CrankHandle1):
    turn = Revolute(axis=(0, 0, 1))


class Selector(DigitSelectorAxle1):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(
        turn=Revolute(axis=(0, 0, 1), at=(58.5, 0, 0)))
    selector_shaft_top_1_419054 = SelectorShaftTop1_419054(
        turn=Revolute(axis=(0, 0, 1), at=(58.5, 0, 0)))
    selector_knob_1_419057 = SelectorKnob1_419057(
        travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))

    setting.drives(selector_knob_1_419057.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419054.turn)


class DriveTrain(AssemblyNode):
    crank_angle = Driver(default=0, range=(0, 360), unit='deg')
    digit = Driver(default=0, range=(0, 9), dtype=int)
    crank = Crank()
    drum = MainAxleStepDrum1(turn=Revolute(axis=(0, 0, 1)))
    selector = Selector()

    crank_angle.drives(crank.turn)
    crank.turn.drives(drum.turn)
    digit.drives(selector.setting)
