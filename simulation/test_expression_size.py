"""Keep repeated calculator laws algebraic, including between shift detents."""

from unittest import TestCase
from simulation.test_dial_cam_law import AngleProbe
from simulation.arithmetic import decimal_shift
from simulation.cycle import tooth_passage
from simulation.carry_motion import engagement


class ExpressionSizeTest(TestCase):
    def test_decimal_shift_preserves_the_lifted_interpolation(self):
        for step in range(501):
            shift = step/100
            expected = sum(10**place * max(0, 1-abs(shift-place)) for place in range(6))
            self.assertAlmostEqual(decimal_shift(shift), expected, places=8)

    def test_tooth_passage_preserves_fractional_and_complete_counts(self):
        for count in (0, .001, .25, .999, 1, 2, 9, 10):
            denominator = count + 1 - min(1, max(0, count))
            for angle in range(0, 181):
                expected = count * min(1, max(0, (angle-125+11.25*count)/(11.25*denominator)))
                self.assertAlmostEqual(tooth_passage(angle, count, 125), expected, places=10)

    def test_repeated_decimal_shift_expression_stays_small(self):
        probe = AngleProbe()
        probe.assemble()
        self.assertLess(len(str(decimal_shift(probe.time))), 200)

    def test_carry_uses_a_direct_maximum_without_copying_both_branches(self):
        probe = AngleProbe()
        probe.assemble()
        self.assertLess(len(str(engagement(probe.time, 1, 0, probe.time, 2))), 9000)
