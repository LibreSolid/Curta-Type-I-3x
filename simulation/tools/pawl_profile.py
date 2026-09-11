"""Measure the ratchet follower in the source's shared contact plane.

The ratchet and pawl have constant profiles across Z -145.8 mm. Their mesh
sections provide a fast 2D exploratory gauge; the actual 3D solids must still
pass the installed contact contract. No part is repaired by this probe.
"""

import json
import argparse
from solid_node.node.adapters.step import StepAssembly
from simulation.source import STEP
from simulation.standard.parts import ZeroPositioningDisc, ReverseRotationPreventionPawl
from simulation.tools.carry_phase import solid

PIVOT = (-51.702407033, 9.116529328)


def profile(part, source):
    item = next(item for item in source.occurrences if item.product_name == part.part)
    part.rotate(item.angle_deg, item.axis).translate(item.translation)
    part.assemble()
    part.build_stls()
    return solid(part.mesh).slice(-145.8)


def swung(pawl, angle):
    return pawl.translate(tuple(-value for value in PIVOT)).rotate(angle).translate(PIVOT)


def probe(gap=0.05):
    source = StepAssembly(STEP)
    disc = profile(ZeroPositioningDisc(), source)
    pawl = profile(ReverseRotationPreventionPawl(), source)
    for angle in (-10, -5, -1, 0, 1, 5, 10):
        print(json.dumps({'trial_deflection': angle,
                          'overlap_mm2': (disc ^ swung(pawl, angle)).area()}), flush=True)
    # A positive angle swings the inward-pointing arm clear of the ratchet.
    gauge = pawl.offset(gap)
    samples = sorted(set([index / 10 for index in range(3601)] +
                         [index / 100 for index in range(401)] +
                         [index / 100 for index in range(29800, 30501)]))
    for crank in samples:
        cam = disc.rotate(-crank)
        low, high = -5, 10
        assert (cam ^ swung(gauge, high)).area() == 0, crank
        for _ in range(18):
            mid = (low + high) / 2
            if (cam ^ swung(gauge, mid)).area() > 0:
                low = mid
            else:
                high = mid
        print(json.dumps({'crank': crank, 'pawl': high}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gap', type=float, default=.05)
    probe(parser.parse_args().gap)
