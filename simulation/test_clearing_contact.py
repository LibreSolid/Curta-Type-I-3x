"""Clearing must follow the two physical tooth rows, not a global zeroing tween."""

import numpy as np
from solid_node.test import TestCase
from simulation.clearing_contact import ClearingContactBench
from simulation.standard.parts import ResultsDialType1, ResultsDialType2
from simulation.tools.interference import rigid_leaves


class ClearingContactTest(TestCase):
    node = ClearingContactBench

    def dials(self):
        return [part for _, part in rigid_leaves(self.node)
                if isinstance(part, (ResultsDialType1, ResultsDialType2))]

    def test_lifting_does_not_begin_clearing_the_dials(self):
        self.node.set_state(digit=9, clear=0)
        dials = self.dials()
        before = [dial.mesh.vertices.copy() for dial in dials]
        self.node.set_state(clear=.05)
        for dial, vertices in zip(dials, before):
            np.testing.assert_array_equal(dial.mesh.vertices, vertices)

    def test_parked_teeth_do_not_obstruct_any_digit(self):
        for digit in range(10):
            self.node.set_state(digit=digit, clear=0)
            for dial in self.dials():
                for strip in self.node.clearing.tooth_stack.children:
                    self.assertNotIntersecting(strip, dial)

    def test_teeth_clear_every_dial_through_the_sweep(self):
        for digit in range(10):
            for sample in range(121):
                self.node.set_state(digit=digit, clear=sample/120)
                for dial in self.dials():
                    for strip in self.node.clearing.tooth_stack.children:
                        self.assertNotIntersecting(strip, dial)
