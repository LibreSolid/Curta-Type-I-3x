"""The measured ball cam must also stay small enough to publish seventeen times."""

from unittest import TestCase
from solid_node.node import AssemblyNode
from simulation.dial_detent_motion import BALL_RISE, following


class AngleProbe(AssemblyNode):
    def render(self):
        return []


class DialCamLawTest(TestCase):
    def test_cam_expression_has_a_bounded_symbolic_size(self):
        probe = AngleProbe()
        probe.assemble()
        expression = following(0)(None, None)(probe.time)
        self.assertLess(len(str(expression)), 1500)

    def test_cam_tracks_the_native_upper_bracket_within_fifty_nanometers(self):
        law = following(0)(None, None)
        for angle, rise in BALL_RISE:
            self.assertGreaterEqual(law(-angle), rise, angle)
            self.assertLessEqual(law(-angle)-rise, .00005, angle)

    def test_cam_is_periodic_across_the_digit_zero(self):
        law = following(0)(None, None)
        for angle in (0, .01, 13.5, 18.5, 32, 34, 35.99):
            for turn in range(-3, 4):
                self.assertAlmostEqual(law(-angle), law(-angle-36*turn), places=10)
