"""Compile native sphere-to-dial measurements into one periodic follower law."""

import json
import sys
from pathlib import Path
from simulation.tools.compile_detents import compact


def emit(path):
    rows = [json.loads(line) for line in Path(path).read_text().splitlines()
            if line.startswith('{')]
    envelope = {}
    for row in rows:
        angle = row['angle']
        envelope[angle] = max(envelope.get(angle, 0), row['rise'])
    points = compact(sorted(envelope.items()))
    lines = ['"""Native dial-detent envelope, with .05 mm vertical seating allowance.',
             '', 'Both source dial types; see tools/dial_detent.py and compile_dial_detent.py.',
             '"""', '', 'from simulation.dial_cam import rise', '', '', 'BALL_RISE = (']
    lines.extend(f'    ({x:g}, {y:.6f}),' for x, y in points)
    lines.extend([')', '', '', 'def following(zero_angle):',
                  '    def law(source, target):',
                  '        return lambda turn: rise(zero_angle - turn)',
                  '    return law'])
    target = Path(__file__).resolve().parents[1] / 'dial_detent_motion.py'
    print('*** Begin Patch')
    print(f'*** Add File: {target}')
    print('\n'.join('+' + line for line in lines))
    print('*** End Patch')


if __name__ == '__main__':
    emit(sys.argv[1])
