"""Declare the author's printed groups as exact fusions of source ingredients."""

from pathlib import Path
import ast
from simulation.tools.layer_import import CLASSES, members


def emit():
    fixed = {'MainAxleStepDrumTop1', 'MainAxleStepDrumBottom1', 'TensBell1'}
    prefixes = ('Part10218_', 'Part10219_', 'Part10220_', 'Part10221_', 'Part10222_', 'Part10230_')
    lines = ['"""Printed groups from the standard STL assembly stages, using exact STEP ingredients.',
             '', 'Placements are transcribed from the untouched source map. Gear fitting is',
             'explicit in fit.py; nothing is copied from the problematic grouped print STLs.',
             '"""', '', 'from solid_node.node import FusionNode',
             'from simulation.standard.parts import *',
             'from simulation.fit import (FittedInputPinion, FittedInputSpacer, FittedOnesSpacer,',
             '    FittedSlidingSpacer, FittedCounterSpacer, FittedOnesSleeve,',
             '    FittedInputSleeve, FittedCounterSleeve)', '', '']
    for name in CLASSES:
        if name not in fixed and not name.startswith(prefixes):
            continue
        lines.extend([f'class {name}(FusionNode):', "    color = '#d3d5cb'",
                      '    angular_deflection = 0.5'])
        for child, declaration in members(name).items():
            cls = declaration.value.func.id
            assert cls not in CLASSES, (name, child, 'a print cannot contain an assembly')
            if name.startswith(('Part10218_', 'Part10219_', 'Part10230_')):
                cls = {'TransmissionGear0_5': 'FittedInputPinion',
                       'Part1_8mmSpacer': 'FittedInputSpacer',
                       'Part1_5mmSpacer': 'FittedOnesSpacer',
                       'Part1_6mmSpacer': 'FittedSlidingSpacer',
                       'Part1mmSpacer': 'FittedCounterSpacer',
                       'Part4_7mmOnesSleeve': 'FittedOnesSleeve',
                       'Part2_5mmLockoutSleeve': 'FittedInputSleeve',
                       'Part5_8Sleeve': 'FittedCounterSleeve'}.get(cls, cls)
            lines.append(f'    {child} = {cls}()')
        render = next(node for node in CLASSES[name].body
                      if isinstance(node, ast.FunctionDef) and node.name == 'render')
        lines.append('')
        lines.extend('    ' + line for line in ast.unparse(render).splitlines())
        lines.extend(['', ''])
    path = Path(__file__).resolve().parents[1] / 'standard/printed.py'
    print('*** Begin Patch')
    print(f'*** Add File: {path}')
    print('\n'.join('+' + line for line in '\n'.join(lines).rstrip().splitlines()))
    print('*** End Patch')


if __name__ == '__main__':
    emit()
