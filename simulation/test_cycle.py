"""Sub-turn motion conserves arithmetic and exposes the carry sequence."""

import unittest
from simulation.arithmetic import calculate, digit
from simulation.cycle import dial_positions


class DecimalCycleTest(unittest.TestCase):
    def test_carry_follows_the_input_tooth(self):
        wheels = dial_positions(9, 1, .36, 0, 0, 0, 11)
        self.assertAlmostEqual(wheels[0], 10)
        self.assertEqual(wheels[1], 0)
        wheels = dial_positions(9, 1, .46, 0, 0, 0, 11)
        self.assertAlmostEqual(wheels[1], 1)

    def test_completed_cycle_matches_calculator_arithmetic(self):
        for shift in range(6):
            for subtract in (0, 1):
                for value, operand in [(0, 0), (9, 1), (99, 1), (12345, 678), (99999999999, 1)]:
                    for places, counter in [(11, False), (6, True)]:
                        before = value % 10 ** places
                        actual = dial_positions(before, operand, .999999, subtract, shift, 0, places, counter)
                        result, turns = calculate(before, before, operand, 1, subtract, shift)
                        expected = turns if counter else result
                        self.assertEqual(tuple(round(wheel) % 10 for wheel in actual),
                                         tuple(digit(expected, place) for place in range(places)),
                                         (before, operand, shift, subtract, counter))

    def test_subtraction_uses_complement_not_reverse_rotation(self):
        wheels = dial_positions(1, 1, .999999, 1, 0, 0, 11)
        self.assertEqual(wheels, (10,) * 11)

    def test_cycle_starts_at_the_current_settled_register(self):
        for turns in (0, 1, 2):
            self.assertEqual(dial_positions(123, 9, turns, 0, 0, 0, 11)[:3], (3, 2, 1))
