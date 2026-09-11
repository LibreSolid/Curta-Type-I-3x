"""Measure the zero cam's roller-follower lift against a .05 mm radial gauge.

The source roller is 20.7 mm diameter, its arm is 33.6 mm long and its pivot
is (40.5, 33.6). The spring presses it inward. Binary search finds the smallest
outward lever angle clearing the inflated roller, not an assumed sine cam.
"""

from math import asin, atan2, degrees, hypot
import json
import cadquery as cq
import numpy as np
from solid_node.node.adapters.step import StepAssembly
from simulation.source import STEP
from simulation.standard.parts import ZeroPositioningDisc


def probe():
    source = StepAssembly(STEP)
    part = ZeroPositioningDisc()
    occurrence = next(item for item in source.occurrences if item.product_name == part.part)
    assert np.allclose(occurrence.world_matrix, occurrence.matrix)
    disc = part.shape().rotate((0, 0, 0), occurrence.axis, occurrence.angle_deg)
    disc = disc.translate(occurrence.translation)
    gauge = cq.Solid.makeCylinder(10.35 + .05, 4.6, cq.Vector(40.5, 0, -153.1))
    pivot, axis = (40.5, 33.6, 0), (40.5, 33.6, 1)
    a, b = 2 * 40.5 * 33.6, 2 * 33.6**2
    c = (34.5 + 10.4)**2 - 40.5**2 - 2 * 33.6**2
    maximum = degrees(asin(c / hypot(a, b)) + atan2(b, a))
    print(json.dumps({'full_lift_deg': maximum}), flush=True)
    for crank in [*range(33), 180, *range(328, 361)]:
        cam = disc.rotate((0, 0, 0), (0, 0, 1), -crank)

        def blocked(angle):
            overlap = cam.intersect(gauge.rotate(pivot, axis, angle))
            assert overlap.isValid(), (crank, angle)
            return sum(solid.Volume() for solid in overlap.Solids()) > 0

        low, high = 0, maximum + .01
        assert not blocked(high), crank
        if blocked(0):
            for _ in range(17):
                mid = (low + high) / 2
                if blocked(mid):
                    low = mid
                else:
                    high = mid
        else:
            high = 0
        print(json.dumps({'crank': crank, 'lever': high}), flush=True)


if __name__ == '__main__':
    probe()
