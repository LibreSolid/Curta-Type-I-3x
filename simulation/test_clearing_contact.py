"""Clearing must follow the two physical tooth rows, not a global zeroing tween."""

import numpy as np
from math import degrees
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

    def row_interfaces(self):
        return (
            (self.node.clearing.tooth_stack.outer_teeth,
             self.node.results.p_10203_1.results_dial_type_1, 9.75, degrees(3.75/52)),
            (self.node.clearing.tooth_stack.inner_teeth,
             self.node.results.p_10205_1.results_dial_type_2, 10.5, degrees(3.75/49.55)),
        )

    def test_each_row_clears_at_eighth_tooth_intervals(self):
        for _, dial, start, pitch in self.row_interfaces():
            for digit in range(1, 10):
                # Include one tooth before and after the entire active passage.
                for eighth in range(-8, (11 - digit)*8 + 1):
                    angle = start + pitch * eighth/8
                    self.node.set_state(digit=digit, clear=.1 + .8*angle/360)
                    for strip in self.node.clearing.tooth_stack.children:
                        self.assertNotIntersecting(strip, dial)

    def test_both_rows_transmit_motion_with_bounded_backlash(self):
        for row, dial, start, pitch in self.row_interfaces():
            angle = start + 4.5*pitch
            self.node.set_state(digit=1, clear=.1 + .8*angle/360)
            self.assertFreeWithin(dial, .1, against=row)
            self.assertBlockedBeyond(dial, 12, against=row)
