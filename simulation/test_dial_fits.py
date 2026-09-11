"""Clearing fits cannot silently alter the already-proven bevel or axle bore."""

import cadquery as cq
from solid_node.test import TestCase
from simulation.dial_fits import FittedDialType1, FittedDialType2
from simulation.standard.parts import ResultsDialType1, ResultsDialType2


class DialFitTest(TestCase):
    node = FittedDialType1
    original = ResultsDialType1

    def test_one_valid_body_with_only_material_removed(self):
        current = self.node.shape()
        original = self.original().shape()
        self.assertTrue(current.isValid())
        self.assertEqual(len(current.Solids()), 1)
        self.assertGreater(original.Volume(), current.Volume())
        self.assertEqual(current.cut(original).Volume(), 0)

    def test_change_is_confined_to_clearing_flanks(self):
        removed = self.original().shape().cut(self.node.shape())
        start, height = self.node.cam_band
        permitted = cq.Solid.makeCylinder(8, height, cq.Vector(0, 0, start))
        self.assertEqual(removed.cut(permitted).Volume(), 0)
        protected_bore = cq.Solid.makeCylinder(3.5, 31)
        self.assertEqual(removed.intersect(protected_bore).Volume(), 0)


class DialType2FitTest(DialFitTest):
    node = FittedDialType2
    original = ResultsDialType2
