"""Emit source-specific vertical carry sliders without moving their bearings."""

from pathlib import Path
from simulation.tools.transmission_import import translation


def emit():
    lines = ['"""Carry sliders at their source bearing stations; the spring fit is separate."""', '',
             'from solid_node.motion.joints import Prismatic',
             'from solid_node.motion.ports import Port',
             'from simulation.standard.parts import TensSliderForResults, TensSliderForTurnsCounter',
             'import simulation.standard.assembly as source',
             'import simulation.standard.layers as layers', '', '']
    for bank, count, slider, cls, upper in [
        ('Results', 10, 'tens_slider_for_results', 'TensSliderForResults', 2.1),
        ('Turns', 5, 'tens_slider_for_turns_counter', 'TensSliderForTurnsCounter', -26.1),
    ]:
        for index in range(1, count+1):
            name = f'{bank}TensLeverAssembly{index}'
            z = translation(name, slider)[2]
            lines.extend([f'class {bank}Lever{index}(source.{name}):',
                          '    engage = Port()',
                          f'    {slider} = {cls}(travel=Prismatic(axis=(0, 0, -1)))',
                          f'    engage.drives({slider}.travel, ratio=4.2, offset={round(z-upper, 9)})',
                          '', ''])
        lines.append(f'class {bank}Carry(layers.{"ResultCarry" if bank == "Results" else "TurnsCarry"}):')
        for index in range(1, count+1):
            lines.append(f'    {bank.lower()}_tens_lever_assembly_{index} = {bank}Lever{index}()')
        lines.extend(['', ''])
    target = Path(__file__).resolve().parents[1] / 'standard/carry.py'
    print('*** Begin Patch')
    print(f'*** Add File: {target}')
    print('\n'.join('+' + line for line in '\n'.join(lines).rstrip().splitlines()))
    print('*** End Patch')


if __name__ == '__main__':
    emit()
