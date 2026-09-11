"""Measure a builder's tooth-outline relief, without changing the source file."""

import cadquery as cq
import numpy as np
from simulation.standard.parts import OneToothStepDrumSegment, TransmissionGear0_5
from simulation.tools.input_contact import solid


def relieved(shape, amount):
    face = max((f for f in shape.Faces() if f.geomType() == 'PLANE'), key=lambda f: f.Area())
    wire, = face.outerWire().offset2D(-amount)
    wire = wire.translate((0, 0, -face.Center().z))
    envelope = cq.Solid.extrudeLinear(wire, [], cq.Vector(0, 0, shape.BoundingBox().zlen))
    return shape.intersect(envelope)


def probe():
    tooth = solid(OneToothStepDrumSegment()).rotate((0, 0, 170.104082802))
    tooth = tooth.translate((0, 0, -70.8))
    source = TransmissionGear0_5().shape()
    class Sample:
        def shape(self):
            return relieved(source, relief)
    for relief in (.1, .15, .2, .25, .3, .35, .4):
        gear = solid(Sample())
        for home in (0, 4, 8, 12, 16):
            for start in np.arange(112, 117.01, .25):
                maximum = 0
                for angle in np.arange(105, 135.01, .5):
                    phase = home + 72 * np.clip((angle - start) / 11.25, 0, 1)
                    overlap = (tooth.rotate((0, 0, -angle)) ^
                               gear.rotate((0, 0, phase)).translate((40.5, 0, -70.92499975)))
                    maximum = max(maximum, overlap.volume())
                print(relief, home, start, maximum, flush=True)


if __name__ == '__main__':
    probe()
