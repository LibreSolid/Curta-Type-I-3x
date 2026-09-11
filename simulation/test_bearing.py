"""A locally successful gear fit must not enter the stationary bearing plate."""

from solid_node.test import TestCase
from simulation.bearing import ShaftBearing


class ShaftBearingTest(TestCase):
    node = ShaftBearing

    def test_tip_clears_frame_through_a_turn(self):
        for angle in range(0, 361, 30):
            self.node.set_state(turn=angle)
            self.assertNotIntersecting(self.node.body,
                                       self.node.shaft.p_10208_1.transmission_gear_tip)
