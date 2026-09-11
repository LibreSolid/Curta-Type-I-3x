"""The input gear slides on its keyed shaft; rotation carries the whole stack."""

import numpy as np
from math import cos, sin, radians
from solid_node.test import TestCase
from simulation.transmission import TransmissionBench


class TransmissionBenchTest(TestCase):
    node = TransmissionBench

    def test_selected_digit_lowers_the_input_gear_only(self):
        self.node.set_state(digit=0, advance=0)
        gear = self.node.p_10219_410002_1.transmission_gear_0_5_1
        shaft = self.node.p_10208_1.ones_transmission_shaft
        before, fixed = gear.mesh.vertices.copy(), shaft.mesh.vertices.copy()
        self.node.set_state(digit=9)
        self.assertLess(np.max(np.abs(gear.mesh.vertices - before - [0, 0, -54])), .00001)
        np.testing.assert_array_equal(shaft.mesh.vertices, fixed)

    def test_one_digit_rotates_the_keyed_stack_seventy_two_degrees(self):
        self.node.set_state(digit=0, advance=0)
        shaft = self.node.p_10208_1.ones_transmission_shaft
        before = shaft.mesh.vertices.copy()
        self.node.set_state(advance=1)
        angle = radians(72)
        rotation = np.array([[cos(angle), -sin(angle), 0],
                             [sin(angle), cos(angle), 0], [0, 0, 1]])
        at = np.array([40.5, 0, 0])
        expected = (before-at) @ rotation.T + at
        self.assertLess(np.max(np.abs(shaft.mesh.vertices - expected)), .00001)
