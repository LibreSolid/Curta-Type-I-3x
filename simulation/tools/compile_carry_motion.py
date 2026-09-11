"""Emit measured pin-approach and rising-cam profiles as ordinary Python data."""

import json
import argparse
from pathlib import Path


def records(name):
    path = Path('_build_evidence') / name
    return [json.loads(line) for line in path.read_text().splitlines() if line.startswith('{')]


def compact(points, error=.001):
    if len(points) < 3:
        return points
    (x0, y0), (x1, y1) = points[0], points[-1]
    deviations = [abs(y - y0 - (y1-y0)*(x-x0)/(x1-x0)) for x, y in points[1:-1]]
    worst = max(deviations)
    if worst <= error:
        return [points[0], points[-1]]
    index = deviations.index(worst) + 1
    return compact(points[:index+1], error)[:-1] + compact(points[index:], error)


def emit(half_input='carry-half-trigger-assembled.jsonl'):
    profiles = []
    for name in (half_input, 'carry-full-trigger-final-tip.jsonl'):
        rows = records(name)
        assert rows and all(row['minimum_drop_mm'] is not None for row in rows)
        profiles.append({row['digit']: row['minimum_drop_mm'] for row in rows})
    assert profiles[0].keys() == profiles[1].keys()
    digits = sorted(profiles[0])
    points = [(0, 0), (digits[0]-.02, 0)]
    points += [(digit, max(profile[digit] for profile in profiles) + .05) for digit in digits]
    points += [(digits[-1]+.02, 0), (10, 0)]
    tables = {'PIN_DROP': compact(points)}
    rows = [row for row in records('carry-reset-profile.jsonl') if row['bank'] == 'result']
    rising = {row['angle'] + (360 if row['angle'] < 30 else 0): row['required_lift_mm']
              for row in rows if row['angle'] >= 330 or row['angle'] <= 3}
    points = [(min(rising)-1, 0)] + [(angle, lift + .05) for angle, lift in sorted(rising.items())]
    tables['RESET_LIFT'] = compact(points)
    lines = ['"""Measured carry contact profiles; .05 mm gauges, .001 mm knot compression.',
             'PIN_DROP is the envelope of the installed half and full pins.',
             '', 'Reproduce with tools/carry_trigger.py, carry_reset_profile.py and compile_carry_motion.py.',
             'These are prescribed contact coordinates, not a spring-force or friction solver.',
             '"""', '']
    for name, points in tables.items():
        lines.extend(['', name + ' = ('])
        lines.extend(f'    ({x:.6f}, {y:.6f}),' for x, y in points)
        lines.append(')')
    target = Path(__file__).resolve().parents[1] / 'carry_profiles.py'
    print('*** Begin Patch')
    print(f'*** Add File: {target}')
    print('\n'.join('+' + line for line in lines))
    print('*** End Patch')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--half-input', default='carry-half-trigger-assembled.jsonl')
    emit(**vars(parser.parse_args()))
