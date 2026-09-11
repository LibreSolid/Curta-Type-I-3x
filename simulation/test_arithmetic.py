"""The author's page-53 checks, plus direct calculator operations."""

from unittest import TestCase
from simulation.arithmetic import calculate


class ArithmeticTest(TestCase):
    def test_manual_successive_carries(self):
        result, counter = 0, 0
        for operand, expected in ((0, 0), (1, 1), (9, 10), (90, 100),
                                  (900, 1000), (9000, 10000)):
            result, counter = calculate(result, counter, operand, 1)
            self.assertEqual(result, expected)
        self.assertEqual(counter, 6)

    def test_complete_overflow(self):
        self.assertEqual(calculate(99999999999, 999999, 1, 1), (0, 0))

    def test_add_then_subtract_one(self):
        result, counter = calculate(0, 0, 1, 1)
        self.assertEqual(calculate(result, counter, 1, 1, subtract=1), (0, 0))

    def test_multiplication_and_decimal_shift(self):
        self.assertEqual(calculate(0, 0, 123, 4), (492, 4))
        self.assertEqual(calculate(492, 4, 123, 2, shift=1), (2952, 24))

    def test_borrow(self):
        self.assertEqual(calculate(0, 0, 1, 1, subtract=1), (99999999999, 999999))

    def test_clearing(self):
        self.assertEqual(calculate(12345678901, 123456, 0, 0, clear=1), (0, 0))
