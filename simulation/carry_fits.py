"""Local fork and reset-shoe filing; the slider's detents and guide stay intact."""

import cadquery as cq
from solid_node.parameters import Length
from simulation.standard.parts import TensSliderForResults, TensSliderForTurnsCounter


def in_first_result_station(shape, counter=False, inverse=False):
    """Measured source placements, with counter fork height reduced by 14.7 mm."""
    angle = -152.009109282 if counter else -120
    axis = (0.684791079, 0.249243569, 0.684791079) if counter else (1, 1, 1)
    at = (-31.302472974, 48.436038605, -26.1) if counter else (57.225, -7.89, 2.1)
    if inverse:
        if counter:
            shape = shape.translate((0, 0, 14.7)).rotate((0, 0, 0), (0, 0, 1), 130)
        return shape.translate(tuple(-v for v in at)).rotate((0, 0, 0), axis, -angle)
    shape = shape.rotate((0, 0, 0), axis, angle).translate(at)
    return shape.rotate((0, 0, 0), (0, 0, 1), -130).translate((0, 0, -14.7)) if counter else shape


class CarrySliderFit:
    fork_radius = Length(4.02)
    flange_radius = Length(6.22)
    ring_tip_radius = Length(36.48)
    seat_gap = Length(.05)
    counter = False

    def adjust(self, shape):
        # The 3.97 mm sleeve rubs the fork throughout its 5.55 mm axial band.
        sleeve = cq.Solid.makeCylinder(self.fork_radius, 5.55,
                                       cq.Vector(38.057551142, -13.851815805, -27.6))
        # The fitted lower flange reaches radius 6.164278 mm; 6.22 bounds its
        # contact region without shaving the fork's free, overhanging ends.
        lower_flange = cq.Solid.makeCylinder(self.flange_radius, 20,
            cq.Vector(38.057551142, -13.851815805, -47.6 + self.seat_gap))
        lower_flange = lower_flange.intersect(cq.Solid.makeCylinder(
            45, 20, cq.Vector(0, 0, -47.6 + self.seat_gap)))
        # The shoe must lie below the fixed-height locking discs, not inside
        # them. Its underside still follows the separate, lower reset cam.
        disc = cq.Solid.makeCylinder(35.4 + self.seat_gap, 30,
                                     cq.Vector(0, 0, -25.5 - self.seat_gap))
        # At the lower detent the original shoe enters the carry-ring base by
        # .3 mm. Shorten only its sole, retaining .05 mm above that base.
        sole = cq.Solid.makeCylinder(self.ring_tip_radius + self.seat_gap, 20,
                                     cq.Vector(0, 0, -47.3 + self.seat_gap))
        for tool in (sleeve, lower_flange, disc, sole):
            shape = shape.cut(in_first_result_station(tool, self.counter, inverse=True))
        return shape


class FittedResultsSlider(CarrySliderFit, TensSliderForResults):
    pass


class FittedTurnsSlider(CarrySliderFit, TensSliderForTurnsCounter):
    counter = True
