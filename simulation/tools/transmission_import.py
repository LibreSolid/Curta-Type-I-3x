"""Emit explicit moving channel declarations from the immutable STEP map.

Only declarations and measured placements are generated. The machine's
behavior is hand-written in transmission.py and cycle.py.
"""

import ast
from math import atan2, degrees
from pathlib import Path
from simulation.tools.layer_import import CLASSES, members


def translation(owner, child):
    render = next(n for n in CLASSES[owner].body
                  if isinstance(n, ast.FunctionDef) and n.name == 'render')
    move = next(n.value for n in render.body
                if ast.unparse(n).startswith(f'self.{child}.translate('))
    return ast.literal_eval(move.args[0])


def channels():
    for attribute, declaration in members('CurtaAssembly').items():
        name = declaration.value.func.id
        if not name.startswith(('Part10236_', 'Part10237_', 'Part10238_', 'Part10239_')):
            continue
        children = {key: node.value.func.id for key, node in members(name).items()}
        shaft = next(key for key, cls in children.items()
                     if cls.startswith(('Part10207_', 'Part10208_', 'Part10209_', 'Part10216_')))
        x, y, _ = translation(children[shaft], 'transmission_gear_tip')
        angle = round(degrees(atan2(y, x)))
        counter = 20 < angle < 150
        place = (130-angle)//20 if counter else (-angle % 360)//20
        input_gear = next(key for key, cls in children.items()
                         if cls.startswith(('Part10218_', 'Part10219_', 'Part10230_')))
        carry = next(key for key, cls in children.items()
                     if cls.startswith(('Part10220_', 'Part10221_', 'Part10222_')))
        suffix = ('Ones', 'Tens', 'Hundreds')[place] if place < 3 else f'Digit{place+1}'
        label = ('Turns' if counter else 'Result') + suffix
        yield dict(label=label, source=name, shaft=shaft, x=x, y=y,
                   input=input_gear, carry=carry, children=children,
                   angle=angle, counter=counter, place=place)


def emit():
    data = sorted(channels(), key=lambda item: (item['counter'], item['place']))
    lines = ['"""Source-specific keyed shafts, separated into sliding printed groups."""', '',
             'from solid_node.motion.joints import Revolute, Prismatic',
             'from solid_node.motion.ports import Port',
             'from simulation.fit import FittedBevelTip, TENS_SHAFT_X_CORRECTION',
             'import simulation.standard.assembly as source',
             'import simulation.standard.printed as printed', '', '']
    for item in data:
        label, children = item['label'], item['children']
        lines.extend([f'class {label}Shaft(source.{children[item["shaft"]]}):',
                      '    transmission_gear_tip = FittedBevelTip()', '', '',
                      f'class {label}(source.{item["source"]}):',
                      f'    turn = Revolute(axis=(0, 0, 1), at=({item["x"]}, {item["y"]}, 0))',
                      '    setting = Port()', '    carry = Port()',
                      f'    {item["shaft"]} = {label}Shaft()',
                      f'    {item["input"]} = printed.{children[item["input"]]}(',
                      '        travel=Prismatic(axis=(0, 0, -1)))',
                      f'    {item["carry"]} = printed.{children[item["carry"]]}(',
                      '        travel=Prismatic(axis=(0, 0, -1)))',
                      f'    setting.drives({item["input"]}.travel, ratio=6)'])
        carry_class = children[item['carry']]
        if carry_class.startswith('Part10220_'):
            z = translation(carry_class, 'transmission_gear_0_6')[2]
            upper_z = -14.7 if item['counter'] else -29.4
            lines.append(f'    carry.drives({item["carry"]}.travel, ratio=4.2, offset={round(z-upper_z, 9)})')
        else:
            lines.append(f'    carry.drives({item["carry"]}.travel, ratio=0)')
        if item['source'] == 'Part10236_1':
            lines.extend(['', '    def render(self):', '        super().render()',
                          '        self.translate((TENS_SHAFT_X_CORRECTION, 0, 0))'])
        lines.extend(['', ''])
    target = Path(__file__).resolve().parents[1] / 'standard/channels.py'
    print('*** Begin Patch')
    print(f'*** Add File: {target}')
    print('\n'.join('+' + line for line in '\n'.join(lines).rstrip().splitlines()))
    print('*** End Patch')


if __name__ == '__main__':
    emit()
