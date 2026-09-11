"""Eight input channels: 6 mm detents, 36 degree number-roll steps.

Source-specific axes and child types are deliberately explicit.
"""
from solid_node.motion.joints import Revolute, Prismatic
from solid_node.motion.ports import Port
from solid_node.math import floor
from solid_node.simulation import Driver
from simulation.standard.assembly import *
from simulation.standard.layers import InputSelectors

def digit_at(place):
    return lambda source, target: lambda value: (
        floor(value / 10 ** place) - 10 * floor(value / 10 ** (place + 1)))

class Selector1(DigitSelectorAxle1):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=(58.5, 0.0, 0)))
    selector_shaft_top_1_419054 = SelectorShaftTop1_419054(turn=Revolute(axis=(0, 0, 1), at=(58.5, 0.0, 0)))
    selector_knob_1_419057 = SelectorKnob1_419057(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))
    setting.drives(selector_knob_1_419057.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419054.turn)


class Selector2(DigitSelectorAxle2):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=(54.972018316, -20.008178385, 0)))
    selector_shaft_top_1_419153 = SelectorShaftTop1_419153(turn=Revolute(axis=(0, 0, 1), at=(54.972018316, -20.008178385, 0)))
    selector_knob_1_419152 = SelectorKnob1_419152(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))
    setting.drives(selector_knob_1_419152.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419153.turn)


class Selector3(DigitSelectorAxle3):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=(44.813599922, -37.603075167, 0)))
    selector_shaft_top_1_419224 = SelectorShaftTop1_419224(turn=Revolute(axis=(0, 0, 1), at=(44.813599922, -37.603075167, 0)))
    selector_knob_1_419225 = SelectorKnob1_419225(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))
    setting.drives(selector_knob_1_419225.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419224.turn)


class Selector4(DigitSelectorAxle4):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=(29.25, -50.662486121, 0)))
    selector_shaft_top_1_419083 = SelectorShaftTop1_419083(turn=Revolute(axis=(0, 0, 1), at=(29.25, -50.662486121, 0)))
    selector_knob_1_419084 = SelectorKnob1_419084(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))
    setting.drives(selector_knob_1_419084.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419083.turn)


class Selector5(DigitSelectorAxle5):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=(10.158418394, -57.611253551, 0)))
    selector_shaft_top_1_419178 = SelectorShaftTop1_419178(turn=Revolute(axis=(0, 0, 1), at=(10.158418394, -57.611253551, 0)))
    selector_knob_1_419177 = SelectorKnob1_419177(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))
    setting.drives(selector_knob_1_419177.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419178.turn)


class Selector6(DigitSelectorAxle6):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=(-10.158418394, -57.611253551, 0)))
    selector_shaft_top_1_419142 = SelectorShaftTop1_419142(turn=Revolute(axis=(0, 0, 1), at=(-10.158418394, -57.611253551, 0)))
    selector_knob_1_419141 = SelectorKnob1_419141(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))
    setting.drives(selector_knob_1_419141.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419142.turn)


class Selector7(DigitSelectorAxle7):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=(-29.25, -50.662486121, 0)))
    selector_shaft_top_1_419103 = SelectorShaftTop1_419103(turn=Revolute(axis=(0, 0, 1), at=(-29.25, -50.662486121, 0)))
    selector_knob_1_419102 = SelectorKnob1_419102(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))
    setting.drives(selector_knob_1_419102.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419103.turn)


class Selector8(DigitSelectorAxle8):
    setting = Port()
    selector_shaft_bottom = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=(-44.813599922, -37.603075167, 0)))
    selector_shaft_top_1_419156 = SelectorShaftTop1_419156(turn=Revolute(axis=(0, 0, 1), at=(-44.813599922, -37.603075167, 0)))
    selector_knob_1_419155 = SelectorKnob1_419155(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))
    setting.drives(selector_knob_1_419155.travel, ratio=6)
    setting.drives(selector_shaft_bottom.turn, ratio=36)
    selector_shaft_bottom.turn.drives(selector_shaft_top_1_419156.turn)


class Selectors(InputSelectors):
    operand = Port()
    digit_selector_axle_1 = Selector1()
    digit_selector_axle_2 = Selector2()
    digit_selector_axle_3 = Selector3()
    digit_selector_axle_4 = Selector4()
    digit_selector_axle_5 = Selector5()
    digit_selector_axle_6 = Selector6()
    digit_selector_axle_7 = Selector7()
    digit_selector_axle_8 = Selector8()
    operand.drives(digit_selector_axle_1.setting, law=digit_at(0))
    operand.drives(digit_selector_axle_2.setting, law=digit_at(1))
    operand.drives(digit_selector_axle_3.setting, law=digit_at(2))
    operand.drives(digit_selector_axle_4.setting, law=digit_at(3))
    operand.drives(digit_selector_axle_5.setting, law=digit_at(4))
    operand.drives(digit_selector_axle_6.setting, law=digit_at(5))
    operand.drives(digit_selector_axle_7.setting, law=digit_at(6))
    operand.drives(digit_selector_axle_8.setting, law=digit_at(7))


class SelectorBank(Selectors):
    """Standalone teaching bench for the eight input digits."""
    input_number = Driver(default=0, range=(0, 99999999), dtype=int)
    input_number.drives(Selectors.operand)
