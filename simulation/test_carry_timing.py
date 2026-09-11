"""A carried lever stays down until its own reset cam reaches that station."""

import unittest
from simulation.transmission import channel_values
from simulation.cycle import dial_positions


class CarryTimingTest(unittest.TestCase):
    def engage(self, value, turns, channel=1, counter=False):
        pose = channel_values(6 if counter else 11, counter)(None, None)
        return pose(value, 1, turns, 0, 0)[3*channel+2]

    def test_first_result_carry_remains_latched_until_the_late_cam(self):
        self.assertEqual(self.engage(9, .8), 1)
        self.assertEqual(self.engage(10, 1), 0)

    def test_counter_carry_survives_the_cycle_boundary_until_its_cam(self):
        self.assertEqual(self.engage(9, .99, counter=True), 1)
        self.assertEqual(self.engage(10, 1.01, counter=True), 1)
        self.assertEqual(self.engage(10, 1.2, counter=True), 0)

    def test_later_result_station_resets_in_the_next_revolution(self):
        self.assertEqual(self.engage(99, .99, channel=2), 1)
        self.assertEqual(self.engage(100, 1, channel=2), 1)
        self.assertEqual(self.engage(100, 1.15, channel=2), 0)

    def test_a_parked_nine_preloads_the_pin_without_latching(self):
        pose = channel_values(11)(None, None)
        for channel in (1, 5):
            value = 9 * 10 ** (channel-1)
            engagement = pose(value, 0, 0, 0, 0)[3*channel+2]
            self.assertGreater(engagement, 0)
            self.assertLess(engagement, .61)
            self.assertEqual(pose(value, 0, 0, 0, 0, 6)[3*channel+2], 0)

    def test_pins_below_the_selected_carriage_place_stay_at_integer_detents(self):
        for counter, places in ((False, 11), (True, 6)):
            for shift in range(1, 6):
                for subtract in (0, 1):
                    for step in range(121):
                        positions = dial_positions(22222222222 % 10**places, 99999999,
                                                   step/120, subtract, shift, 0, places, counter)
                        self.assertEqual(positions[:shift], (2,)*shift)
