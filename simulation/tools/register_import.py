"""Emit declarative dial joints from the source placements and phase probe."""

import json
from pathlib import Path
from math import atan2, degrees, radians, sin, cos
import numpy as np
from simulation.tools.layer_import import members


def emit():
    root = Path(__file__).resolve().parents[2]
    rows = json.loads((root / '_build_evidence/bevel-bank-centered.json').read_text())
    declarations = members('Carriage1')
    angle = radians(.549916905)
    rotation = np.array([[cos(angle), -sin(angle), 0],
                         [sin(angle), cos(angle), 0], [0, 0, 1]])
    lines = ['"""Dial joints and source-specific clocking; one port per register value."""', '',
             'from solid_node.node import AssemblyNode',
             'from solid_node.motion.joints import Revolute',
             'from solid_node.motion.ports import Port',
             'from solid_node.simulation import Driver',
             'from simulation.arithmetic import digit',
             'from simulation.fit import CARRIAGE_CENTER, CARRIAGE_CLOCKING',
             'from simulation.standard.assembly import *',
             'import simulation.standard.layers as source', '', '',
             'def dial_values(phases):',
             '    return lambda sources, targets: lambda value: tuple(',
             '        phase - 36 * digit(value, place) for place, phase in enumerate(phases))', '', '']
    for bank, cls in [('result_register', 'ResultRegister'), ('turns_register', 'TurnsRegister')]:
        def place(row):
            at = row['at']
            theta = degrees(atan2(at[1], at[0]))
            return round((-theta % 360) / 20) if bank == 'result_register' else round((130 - theta) / 20)
        channels = sorted((row for row in rows if f'.{bank}.' in row['dial']), key=place)
        assert [place(row) for row in channels] == list(range(len(channels)))
        lines.extend([f'class {cls}(source.{cls}):', '    value = Port()', ''])
        names, phases = [], []
        for row in channels:
            name = row['dial'].split('.')[2]
            child_cls = declarations[name].value.func.id
            raw_axis = rotation @ row['axis']
            raw_at = rotation @ row['at'] + np.array([.537721035, -.038177283, 0])
            axis = tuple(round(float(v), 10) for v in raw_axis)
            at = tuple(round(float(v), 9) for v in raw_at)
            lines.extend([f'    {name} = {child_cls}(turn=Revolute(',
                          f'        axis={axis}, at={at}))'])
            names.append(name)
            phases.append(round(row['dial_phase'], 8))
        lines.extend(['', '    value.drives((', *[f'        {name}.turn,' for name in names],
                      f'    ), law=dial_values({tuple(phases)}))', '',
                      '    def render(self):', '        super().render()',
                      '        self.translate(tuple(-value for value in CARRIAGE_CENTER))',
                      '        self.rotate(-CARRIAGE_CLOCKING, (0, 0, 1))', '', ''])
    lines.extend(['class RegisterBench(AssemblyNode):',
                  '    result = Driver(default=0, range=(0, 99999999999), dtype=int)',
                  '    registers = ResultRegister()',
                  '    result.drives(registers.value)'])
    print('*** Begin Patch')
    print(f'*** Add File: {root / "simulation/registers.py"}')
    print('\n'.join('+' + line for line in lines))
    print('*** End Patch')


if __name__ == '__main__':
    emit()
