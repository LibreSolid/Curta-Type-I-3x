"""Emit a compact motion profile from the native carry-hook gauge readings.

Compression bounds ordinate interpolation error at .0005 mm; it is not a
geometry-test epsilon. Installed wire contact remains independently tested.
"""

import json
import sys
from pathlib import Path


def compact(points):
    if len(points) < 3:
        return points
    x0, y0 = points[0]
    x1, y1 = points[-1]
    errors = [abs(y - (y0 + (y1-y0)*(x-x0)/(x1-x0))) for x, y in points]
    index = max(range(len(points)), key=errors.__getitem__)
    if errors[index] <= .0005:
        return [points[0], points[-1]]
    return compact(points[:index+1])[:-1] + compact(points[index:])


def emit(path):
    readings = [json.loads(line) for line in Path(path).read_text().splitlines()]
    lines = ['"""Measured .05 mm carry-hook gauge profiles; see tools/carry_profile.py."""', '',
             'from solid_node.math import piecewise', '', '']
    for bank in ('Results', 'Turns'):
        points = compact([(row['engaged'], row['spread']) for row in readings if row['bank'] == bank])
        lines.append(bank.upper() + ' = (')
        lines.extend(f'    ({x:g}, {y:.6f}),' for x, y in points)
        lines.extend([')', '', ''])
    lines.extend(['def spreading(counter=False):',
                  '    points = TURNS if counter else RESULTS',
                  '    def law(source, target):',
                  '        return lambda engaged: piecewise(engaged, points)',
                  '    return law', ''])
    target = Path(__file__).resolve().parents[1] / 'detents.py'
    print('*** Begin Patch')
    print(f'*** Add File: {target}')
    print('\n'.join('+' + line for line in lines))
    print('*** End Patch')


if __name__ == '__main__':
    emit(sys.argv[1])
