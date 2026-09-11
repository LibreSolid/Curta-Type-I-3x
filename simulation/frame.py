"""Measured source corrections, kept separate from the untouched STEP map."""

from simulation.flexibles import FIXED_PIN, ZeroSpring
from simulation.standard.assembly import LowerFrame1


class LowerFrame(LowerFrame1):
    """Replace only the invalid spring; preserve all rigid source placements."""

    documented_spring = ZeroSpring()

    def render(self):
        super().render()
        self.zero_positioning_spring.omit()
        self.documented_spring.translate(FIXED_PIN)
