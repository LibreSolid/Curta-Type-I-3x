"""Explicit assembly fitting; upstream STEP and STL files remain untouched."""

import cadquery as cq
from solid_node.parameters import Length
from simulation.standard.parts import (TransmissionGear0_5, TransmissionGearTip,
    Part1_8mmSpacer, Part1_5mmSpacer, Part1_6mmSpacer, Part1mmSpacer,
    Part4_7mmOnesSleeve, Part2_5mmLockoutSleeve, Part5_8Sleeve)

CARRIAGE_CENTER = (0.537721035, -0.038177283, 0)
CARRIAGE_CLOCKING = 0.549916905
PINION_SEATING_DROP = 1.2
TENS_SHAFT_X_CORRECTION = -0.079764273
INPUT_CLOCKING = 4


class FittedBevelTip(TransmissionGearTip):
    """Trial seating established across all seventeen recentered dial meshes."""
    seating_drop = Length(PINION_SEATING_DROP, min=0)

    def adjust(self, shape):
        return shape.translate((0, 0, -self.seating_drop))


def relieve_outline(shape, amount):
    """Sand only the extruded outside profile; retain the keyed bore and height."""
    face = max((face for face in shape.Faces() if face.geomType() == 'PLANE'),
               key=lambda face: face.Area())
    outline, = face.outerWire().offset2D(-amount)
    outline = outline.translate((0, 0, -face.Center().z))
    envelope = cq.Solid.extrudeLinear(outline, [], cq.Vector(0, 0, shape.BoundingBox().zlen))
    return shape.intersect(envelope)


class FittedInputPinion(TransmissionGear0_5):
    """0.35 mm outer-profile sanding measured by the one-tooth passage probe.

    The unsanded source interferes at every possible phase near tooth center.
    This is a simulation's explicit fitting assumption, not a recommendation
    about print strength or manufacturing tolerances. The keyed bore is intact.
    """
    flank_relief = Length(0.35, min=0)

    def adjust(self, shape):
        return relieve_outline(shape, self.flank_relief) if self.flank_relief else shape


class InputSleeveFit:
    """3.85 mm outside radius: 40.5 shaft radius minus 36.6 drum minus .05 gap.

    The source's 3.97 mm radius intersects the ten-tooth drum even with digit
    zero. Only its outside circular profile is sanded; the keyed bore stays.
    """

    def adjust(self, shape):
        box = shape.BoundingBox()
        envelope = cq.Solid.makeCylinder(3.85, box.zlen, cq.Vector(0, 0, box.zmin))
        return shape.intersect(envelope)


class FittedInputSpacer(InputSleeveFit, Part1_8mmSpacer):
    pass


class FittedOnesSpacer(InputSleeveFit, Part1_5mmSpacer):
    pass


class FittedSlidingSpacer(InputSleeveFit, Part1_6mmSpacer):
    pass


class FittedCounterSpacer(InputSleeveFit, Part1mmSpacer):
    pass


class FittedOnesSleeve(InputSleeveFit, Part4_7mmOnesSleeve):
    pass


class FittedInputSleeve(InputSleeveFit, Part2_5mmLockoutSleeve):
    pass


class FittedCounterSleeve(InputSleeveFit, Part5_8Sleeve):
    pass
