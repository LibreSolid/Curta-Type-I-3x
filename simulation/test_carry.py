"""Carry motion is vertical travel within a fixed bearing, not an axle rotation."""

import numpy as np
from solid_node.test import TestCase
from simulation.carry import CarryBench


class CarryBenchTest(TestCase):
    node = CarryBench

    def test_engaging_lowers_the_lever_four_point_two_mm(self):
        self.node.set_state(engaged=0)
        lever, bearing = self.node.tens_slider_for_results, self.node.tens_slide_bearing
        before, fixed = lever.mesh.vertices.copy(), bearing.mesh.vertices.copy()
        self.node.set_state(engaged=1)
        self.assertLess(np.max(np.abs(lever.mesh.vertices - before - [0, 0, -4.2])), .00001)
        np.testing.assert_array_equal(bearing.mesh.vertices, fixed)

    def test_reset_revisits_the_identical_rest_mesh(self):
        self.node.set_state(engaged=0)
        before = self.node.tens_slider_for_results.mesh.vertices.copy()
        self.node.set_state(engaged=1)
        self.node.set_state(engaged=0)
        np.testing.assert_array_equal(self.node.tens_slider_for_results.mesh.vertices, before)
