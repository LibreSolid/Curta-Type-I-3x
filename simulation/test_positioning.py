"""Measured spring seats, not a translated rigid coil, govern carriage lift."""

import numpy as np
from solid_node.test import TestCase
from simulation.positioning import PositioningBench


class PositioningTest(TestCase):
    node = PositioningBench

    def test_lower_seat_and_coil_rise_but_upper_seat_stays(self):
        self.node.set_state(travel=0)
        lower = self.node.thrust_ring.mesh.vertices.copy()
        upper = self.node.carriage_spring_sleeve.mesh.vertices.copy()
        # Molejo's public mesh layout ends with the two cap centers. Unlike
        # bounding extents, these measure the seats independently of pitch.
        spring = self.node.carriage_spring.wire.mesh.vertices[-2:].copy()
        for lift in (1.5, 3, 4.5, 6):
            self.node.set_state(travel=lift)
            self.assertLess(np.max(np.abs(self.node.thrust_ring.mesh.vertices - lower - [0, 0, lift])), .00001)
            np.testing.assert_array_equal(self.node.carriage_spring_sleeve.mesh.vertices, upper)
            caps = self.node.carriage_spring.wire.mesh.vertices[-2:]
            self.assertLess(np.max(np.abs(caps[0] - spring[0] - [0, 0, lift])), .00001)
            self.assertLess(np.max(np.abs(caps[1] - spring[1])), .00001)

    def test_coil_stays_valid_through_compression(self):
        for lift in (0, 1.5, 3, 4.5, 6):
            self.node.set_state(travel=lift)
            spring = self.node.carriage_spring.wire
            self.assertTrue(spring.mesh.is_watertight)
            self.assertGreater(spring.mesh.volume, 0)
            if spring.exact:
                self.assertTrue(spring.shape().isValid())
                self.assertEqual(len(spring.shape().Solids()), 1)
