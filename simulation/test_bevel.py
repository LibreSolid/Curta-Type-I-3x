"""A correct ratio must also produce a seated, engaged, non-overlapping pair."""

from solid_node.test import TestCase
from simulation.bevel import BevelPair


class BevelPairTest(TestCase):
    node = BevelPair

    def test_one_complete_tooth_period(self):
        for angle in range(0, 73, 6):
            self.node.set_state(pinion_angle=angle)
            self.assertNotIntersecting(self.node.shaft.transmission_gear_tip,
                                       self.node.dial.results_dial_type_1)

    def test_tooth_flanks_transmit_motion(self):
        for angle in (0, 18, 36, 54, 72):
            self.node.set_state(pinion_angle=angle)
            gear = self.node.shaft.transmission_gear_tip
            dial = self.node.dial.results_dial_type_1
            self.assertFreeWithin(gear, 0.1, against=dial)
            self.assertBlockedBeyond(gear, 12, against=dial)
