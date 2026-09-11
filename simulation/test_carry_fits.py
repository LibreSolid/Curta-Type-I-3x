"""Filing a fork cannot erase its guide, detents or material connectivity."""

import cadquery as cq
from solid_node.test import TestCase
from simulation.carry_fits import FittedResultsSlider, FittedTurnsSlider, in_first_result_station
from simulation.standard.parts import TensSliderForResults, TensSliderForTurnsCounter


class CarryFitTest(TestCase):
    node = FittedResultsSlider
    original = TensSliderForResults
    counter = False

    def test_slider_remains_one_valid_body_without_added_material(self):
        original, fitted = self.original().shape(), self.node.shape()
        self.assertTrue(fitted.isValid())
        self.assertEqual(len(fitted.Solids()), 1)
        self.assertEqual(fitted.cut(original).Volume(), 0)
        self.assertGreater(original.Volume() - fitted.Volume(), 0)

    def test_built_shape_matches_the_current_adjustment(self):
        direct = self.node.adjust(self.original().shape())
        self.assertAlmostEqual(self.node.shape().Volume(), direct.Volume(), places=7)

    def test_removal_is_confined_to_the_documented_contact_regions(self):
        removed = in_first_result_station(self.original().shape().cut(self.node.shape()), self.counter)
        # Independent limits from the measured sleeve, flange, locking disc
        # and carry-ring base. These replace a provisional 25 mm³ mass budget:
        # where material is removed is the actual geometry contract.
        sleeve = cq.Solid.makeCylinder(4.02, 5.55, cq.Vector(38.057551142, -13.851815805, -27.6))
        flange = cq.Solid.makeCylinder(6.22, .05, cq.Vector(38.057551142, -13.851815805, -27.6))
        disc = cq.Solid.makeCylinder(35.45, 30, cq.Vector(0, 0, -25.55))
        sole = cq.Solid.makeCylinder(36.53, .35, cq.Vector(0, 0, -27.6))
        for permitted in (sleeve, flange, disc, sole):
            removed = removed.cut(permitted)
        self.assertEqual(removed.Volume(), 0)

    def test_guide_and_detents_are_unchanged(self):
        removed = self.original().shape().cut(self.node.shape())
        removed = in_first_result_station(removed, self.counter)
        # All fitted surfaces are inside the 45 mm radius. The guide, detents
        # and dial-pin head lie outside, around the measured 57.3 mm station.
        permitted = cq.Solid.makeCylinder(45, 100, cq.Vector(0, 0, -50))
        self.assertEqual(removed.cut(permitted).Volume(), 0)


class TurnsCarryFitTest(CarryFitTest):
    node = FittedTurnsSlider
    original = TensSliderForTurnsCounter
    counter = True
