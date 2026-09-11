"""Register values must change the actual dial meshes, not only output ports."""

from math import cos, sin, radians
import numpy as np
from solid_node.test import TestCase
from simulation.registers import RegisterBench


class RegisterBenchTest(TestCase):
    node = RegisterBench

    def test_every_result_dial_turns_about_its_radial_axle(self):
        names = ['p_10203_1', 'p_10203_2', 'p_10205_1', 'p_10205_2',
                 'p_10204_1', 'p_10204_2', 'p_10204_3', 'p_10204_4',
                 'p_10204_5', 'p_10204_6', 'results_dial_type_2_1']
        for place, name in enumerate(names):
            self.node.set_state(result=0, crank_turns=0)
            group = getattr(self.node.registers, name)
            dial = next((child for child in group.children
                         if child.name.startswith('results_dial')), group)
            before = dial.mesh.vertices.copy()
            self.node.set_state(result=10 ** place)
            theta, angle = radians(-20 * place), radians(36)
            axis = np.array([cos(theta), sin(theta), 0])
            x, y, z = axis
            skew = np.array([[0, -z, y], [z, 0, -x], [-y, x, 0]])
            rotation = cos(angle) * np.eye(3) + (1-cos(angle)) * np.outer(axis, axis) + sin(angle) * skew
            at = 71.474057463 * axis + [0, 0, 33.9]
            expected = (before - at) @ rotation.T + at
            self.assertLess(np.max(np.abs(dial.mesh.vertices - expected)), .00001, name)

    def test_visible_input_precedes_visible_carry(self):
        self.node.set_state(result=9, operand=1, crank_turns=0)
        ones = self.node.registers.p_10203_1.results_dial_type_1
        tens = self.node.registers.p_10203_2.results_dial_type_1
        before = ones.mesh.vertices.copy()
        tens_before = tens.mesh.vertices.copy()
        self.node.set_state(crank_turns=.36)
        angle = radians(36)
        rotation = np.array([[1, 0, 0], [0, cos(angle), -sin(angle)],
                             [0, sin(angle), cos(angle)]])
        at = np.array([71.474057463, 0, 33.9])
        self.assertLess(np.max(np.abs(ones.mesh.vertices - ((before-at) @ rotation.T + at))), .00001)
        np.testing.assert_array_equal(tens.mesh.vertices, tens_before)
        self.node.set_state(crank_turns=.46)
        self.assertGreater(np.max(np.abs(tens.mesh.vertices - tens_before)), 1)

    def test_ones_dial_advances_one_tenth_turn(self):
        self.node.set_state(result=0)
        dial = self.node.registers.p_10203_1.results_dial_type_1
        before = dial.mesh.vertices.copy()
        self.node.set_state(result=1)
        angle = radians(36)
        rotation = np.array([[1, 0, 0], [0, cos(angle), -sin(angle)],
                             [0, sin(angle), cos(angle)]])
        axis_point = np.array([71.474057463, 0, 33.9])
        expected = (before - axis_point) @ rotation.T + axis_point
        self.assertLess(np.max(np.abs(dial.mesh.vertices - expected)), .00001)
