"""The source defect must fail before its documented replacement can pass."""

from solid_node.test import TestCase
from simulation.flexibles import ZeroSpring


class ZeroSpringTest(TestCase):
    node = ZeroSpring

    def test_preview_resolution_matches_the_small_wire(self):
        mesh = self.node.mesh
        self.assertLess(len(mesh.faces), 50000)
        # The 24-sided inscribed circular profile accounts for ~1.14% deficit;
        # this bound also limits centerline faceting without demanding a huge mesh.
        self.assertGreater(mesh.volume / self.node.shape().Volume(), .98)

    def test_valid_single_wire(self):
        shape = self.node.shape()
        self.assertTrue(shape.isValid())
        self.assertEqual(len(shape.Solids()), 1)

    def test_documented_wire(self):
        # End cap area measures the wire independently of any model parameter.
        from math import pi
        caps = [face.Area() for face in self.node.shape().Faces()
                if face.geomType() == 'PLANE']
        self.assertEqual(len(caps), 2)
        for area in caps:
            self.assertAlmostEqual(area, pi * 0.55 ** 2, places=5)
