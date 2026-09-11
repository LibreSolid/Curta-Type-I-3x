"""Explicit assembly fitting; upstream STEP and STL files remain untouched."""

import cadquery as cq
from solid_node.parameters import Length
from simulation.standard.parts import (TransmissionGear0_5, TransmissionGear0_6, TransmissionGearTip,
    Part1_8mmSpacer, Part1_5mmSpacer, Part1_6mmSpacer, Part1mmSpacer,
    Part4_7mmOnesSleeve, Part2_5mmLockoutSleeve, Part5_8Sleeve, PentagonalLockout,
    BearingPlate, ReverseRotationPreventionPawl)

CARRIAGE_CENTER = (0.537721035, -0.038177283, 0)
CARRIAGE_CLOCKING = 0.549916905
PINION_SEATING_DROP = 1.2
TENS_SHAFT_X_CORRECTION = -0.079764273
INPUT_CLOCKING = 4
BEVEL_DIAL_CLOCKING = -3
PAWL_PIVOT = (-51.702407033, 9.116529328, 0)
PAWL_SPRING_ANCHOR = (-54.476590334, 16.420391800, -132.6)
PAWL_SPRING_HOLE = (-44.100577738, 13.347627455, -145.2)


class FittedBearingPlate(BearingPlate):
    """Drill the missing .70 mm bore where the source spring tail enters.

    The .60 mm wire then has the named .05 mm radial seat allowance. The
    source tail penetrates 1.637549 mm³ of unbored plate. No other bore moves.
    """

    def adjust(self, shape):
        x, y, _ = PAWL_SPRING_ANCHOR
        bore = cq.Solid.makeCylinder(.35, 6.1, cq.Vector(x, -y, 14.05))
        return shape.cut(bore)


class FittedPawl(ReverseRotationPreventionPawl):
    """Trim .20 mm off the collar's top face, leaving .05 mm below the plate."""

    def adjust(self, shape):
        box = shape.BoundingBox()
        retained = cq.Solid.makeBox(box.xlen + 2, box.ylen + 2, box.zlen,
                                   cq.Vector(box.xmin - 1, box.ymin - 1, -5.2))
        return shape.intersect(retained)


class FittedBevelTip(TransmissionGearTip):
    """Trial seating established across all seventeen recentered dial meshes."""
    seating_drop = Length(PINION_SEATING_DROP, min=0)

    def adjust(self, shape):
        # Lowering the head also lowers the stem into the frame. Shorten only
        # that newly protruding end, retaining the source's bearing-plane datum
        # and keyed bore. No frame holes or mating tooth flanks are changed.
        box = shape.BoundingBox()
        seated = shape.translate((0, 0, -self.seating_drop))
        above_bearing = cq.Solid.makeBox(box.xlen + 2, box.ylen + 2, box.zlen + 2,
                                        cq.Vector(box.xmin - 1, box.ymin - 1, box.zmin))
        return seated.intersect(above_bearing)


def relieve_outline(shape, amount, clocking=0):
    """Sand only the extruded outside profile; retain the keyed bore and height."""
    face = max((face for face in shape.Faces() if face.geomType() == 'PLANE'),
               key=lambda face: face.Area())
    outline, = face.outerWire().offset2D(-amount)
    box = shape.BoundingBox()
    outline = outline.translate((0, 0, box.zmin - face.Center().z))
    if clocking:
        outline = outline.rotate((0, 0, 0), (0, 0, 1), clocking)
    envelope = cq.Solid.extrudeLinear(outline, [], cq.Vector(0, 0, box.zlen))
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


class FittedCounterPinion(FittedInputPinion):
    """The eccentric upper drum needs another .01 mm at the complement row.

    At 84° the exact sweep found 0.000010359 mm³ overlap missed by the
    faceted sweep. This remains a profile fit, never a test volume epsilon.
    """
    flank_relief = Length(.36, min=0)


class FittedCarryLockout(PentagonalLockout):
    """Center the locking flats while retaining the source keyed bore.

    Uniform .4 mm relief cleared the bell but left biased backlash. Clipping
    to an outline clocked back by the input's 4° phase centers the locking
    faces without moving or enlarging the keyway. This only removes material.
    """
    flank_relief = Length(.15, min=0)

    def adjust(self, shape):
        return relieve_outline(shape, self.flank_relief, clocking=-INPUT_CLOCKING)


class FittedCarryPinion(TransmissionGear0_6):
    """Trial outer-flank fit for the .6 carry tooth, retaining its keyway.

    .42 mm scales the measured .35 mm input-tooth fit with the .6/.5 tooth
    size. Full-bell sweeps and flank engagement, not that scaling alone,
    decide whether this candidate fit works.
    """
    flank_relief = Length(.42, min=0)

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
