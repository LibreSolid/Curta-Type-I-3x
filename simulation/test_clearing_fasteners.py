"""Restoring omitted prints cannot introduce unexamined hardware collisions."""

from solid_node.test import TestCase
from simulation.clearing_fasteners import ClearingFastenerBench


class ClearingFastenerTest(TestCase):
    node = ClearingFastenerBench

    def test_formed_strips_clear_the_original_screw_and_rivets(self):
        hardware = (self.node.m4x10_419010_1, self.node.clearing_ring_rivet_1,
                    self.node.clearing_ring_rivet_2)
        for strip in self.node.tooth_stack.children:
            for part in hardware:
                self.assertNotIntersecting(strip, part)
