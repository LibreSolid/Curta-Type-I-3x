"""Compile the measured clearing-cover cam into an axial follower relation."""

import json
import sys
from pathlib import Path
from simulation.tools.compile_detents import compact


def emit(path):
    rows = [json.loads(line) for line in Path(path).read_text().splitlines()
            if line.startswith('{')]
    points = compact([(row['angle'], row['drop']) for row in rows])
    lines = ['"""Native clearing-stop depression for .05 mm minimum surface separation."""',
             '', 'from solid_node.math import piecewise', '', '', 'PIN_DROP = (']
    lines.extend(f'    ({x:g}, {y:.6f}),' for x, y in points)
    lines.extend([')', '', '', 'def following(source, target):',
                  '    return lambda turn: piecewise((-turn) % 360, PIN_DROP)'])
    target = Path(__file__).resolve().parents[1] / 'clearing_stop_motion.py'
    print('*** Begin Patch')
    print(f'*** Add File: {target}')
    print('\n'.join('+' + line for line in lines))
    print('*** End Patch')


if __name__ == '__main__':
    emit(sys.argv[1])
