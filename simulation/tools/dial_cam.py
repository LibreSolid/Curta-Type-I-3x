"""Reproduce the circular dimensions behind the compact ball-follower law."""

import json
from math import hypot
from simulation.standard.parts import ResultsDialType1, ResultsDialType2
from simulation.dial_cam import rise, HALF_DWELL, MEASUREMENT_BRACKET
from simulation.dial_detent_motion import BALL_RISE


def probe():
    for kind in (ResultsDialType1, ResultsDialType2):
        dimensions = set()
        for edge in kind().shape().Edges():
            if edge.geomType() == 'CIRCLE':
                x, y, z = edge.arcCenter().toTuple()
                dimensions.add((round(edge.radius(), 6), round(hypot(x, y), 6), round(z, 6)))
        assert any(radius == 7.2 and center == 0 for radius, center, _ in dimensions)
        assert any(radius == 4.5 and center == 6 for radius, center, _ in dimensions)
        print(json.dumps(dict(dial=kind.__name__, circles=sorted(dimensions))), flush=True)
    errors = [rise(angle)-height for angle, height in BALL_RISE]
    print(json.dumps(dict(half_dwell_deg=HALF_DWELL,
                          measurement_bracket_mm=MEASUREMENT_BRACKET,
                          min_envelope_difference_mm=min(errors),
                          max_envelope_difference_mm=max(errors))), flush=True)


if __name__ == '__main__':
    probe()
