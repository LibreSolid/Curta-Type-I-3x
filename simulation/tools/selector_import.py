"""Emit ordinary motion declarations for the eight measured source variants."""

import ast
from math import atan2, degrees
from pathlib import Path
from simulation.tools.layer_import import CLASSES, members


def emit():
    lines = ['"""Eight input channels: 6 mm detents, 36 degree number-roll steps.',
             '', 'Source-specific axes and child types are deliberately explicit.',
             '"""', 'from solid_node.motion.joints import Revolute, Prismatic',
             'from solid_node.motion.ports import Port',
             'from solid_node.math import floor',
             'from solid_node.simulation import Driver',
             'from simulation.standard.assembly import *',
             'from simulation.standard.layers import InputSelectors', '',
             'def digit_at(place):',
             '    return lambda source, target: lambda value: (',
             '        floor(value / 10 ** place) - 10 * floor(value / 10 ** (place + 1)))', '']
    places = {}
    for number in range(1, 9):
        name = f'DigitSelectorAxle{number}'
        children = members(name)
        bottom = 'selector_shaft_bottom'
        top = next(key for key in children if key.startswith('selector_shaft_top'))
        knob = next(key for key in children if key.startswith('selector_knob'))
        render = next(n for n in CLASSES[name].body if isinstance(n, ast.FunctionDef))
        move = next(n.value for n in render.body if ast.unparse(n).startswith(f'self.{bottom}.translate'))
        x, y, _ = ast.literal_eval(move.args[0])
        places[number] = round(-degrees(atan2(y, x)) / 20)
        lines.extend([f'class Selector{number}({name}):', '    setting = Port()',
                      f'    {bottom} = SelectorShaftBottom(turn=Revolute(axis=(0, 0, 1), at=({x}, {y}, 0)))',
                      f'    {top} = {children[top].value.func.id}(turn=Revolute(axis=(0, 0, 1), at=({x}, {y}, 0)))',
                      f'    {knob} = {children[knob].value.func.id}(travel=Prismatic(axis=(0, 0, -1), range=(0, 54)))',
                      f'    setting.drives({knob}.travel, ratio=6)',
                      f'    setting.drives({bottom}.turn, ratio=36)',
                      f'    {bottom}.turn.drives({top}.turn)', '', ''])
    lines.extend(['class Selectors(InputSelectors):', '    operand = Port()'])
    for number in range(1, 9):
        lines.append(f'    digit_selector_axle_{number} = Selector{number}()')
    assert sorted(places.values()) == list(range(8))
    for number in range(1, 9):
        lines.append(f'    operand.drives(digit_selector_axle_{number}.setting, law=digit_at({places[number]}))')
    lines.extend(['', '', 'class SelectorBank(Selectors):',
                  '    input_number = Driver(default=0, range=(0, 99999999), dtype=int)',
                  '    input_number.drives(Selectors.operand)'])
    path = Path(__file__).resolve().parents[1] / 'selectors.py'
    print('*** Begin Patch')
    print(f'*** Add File: {path}')
    print('\n'.join('+' + line for line in lines))
    print('*** End Patch')


if __name__ == '__main__':
    emit()
