"""Fit the dial-pin contact tips to the measured 4.2 mm carry stroke."""

import cadquery as cq
from solid_node.parameters import Length
from simulation.carry_fits import FittedResultsSlider, FittedTurnsSlider, in_first_result_station


class DialPinHeadFit:
    tip_height = Length(31.15)

    def adjust(self, shape):
        fitted = super().adjust(shape)
        # The full pin otherwise needs about 5.4 mm of lever depression. A
        # 31.15 mm installed tip also lets the reset cam pass with a dial
        # parked at nine: pin depression then remains below the cam's 1.25 mm
        # available drop at its crest. Only the pin-contact tip is filed.
        height = self.tip_height - (14.7 if self.counter else 0)
        above_tip = cq.Solid.makeBox(140, 140, 50, cq.Vector(-70, -70, height))
        return fitted.cut(in_first_result_station(above_tip, self.counter, inverse=True))


class ResultsSlider(DialPinHeadFit, FittedResultsSlider):
    pass


class TurnsSlider(DialPinHeadFit, FittedTurnsSlider):
    pass
