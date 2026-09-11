"""A local tip fit must leave the guide, detents, fork and reset shoe intact."""

import cadquery as cq
from solid_node.test import TestCase
from simulation.carry_heads import ResultsSlider, TurnsSlider
from simulation.carry_fits import FittedResultsSlider, FittedTurnsSlider, in_first_result_station


class CarryHeadTest(TestCase):
    node = ResultsSlider
    original = FittedResultsSlider
    counter = False

    def test_one_valid_slider_with_only_the_contact_tip_changed(self):
        original, fitted = self.original().shape(), self.node.shape()
        self.assertTrue(fitted.isValid())
        self.assertEqual(len(fitted.Solids()), 1)
        self.assertEqual(fitted.cut(original).Volume(), 0)
        removed = in_first_result_station(original.cut(fitted), self.counter)
        floor = 16.45 if self.counter else 31.15
        allowed = cq.Solid.makeBox(12, 12, 3, cq.Vector(51, -13, floor))
        self.assertGreater(removed.Volume(), 0)
        self.assertEqual(removed.cut(allowed).Volume(), 0)


class TurnsCarryHeadTest(CarryHeadTest):
    node = TurnsSlider
    original = FittedTurnsSlider
    counter = True
