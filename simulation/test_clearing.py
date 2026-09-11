"""The omitted strips must be bent into the measured cover groove."""

import numpy as np
from solid_node.test import TestCase
from simulation.clearing import ClearingBench
from simulation.contracts import assert_connected_material


class ClearingBenchTest(TestCase):
    node = ClearingBench

    def test_three_upstream_prints_form_the_stack(self):
        self.assertEqual(len(self.node.teeth.children), 3)
        for part in self.node.teeth.children:
            assert_connected_material(part.mesh)

    def test_stack_fits_the_cover_groove(self):
        for part in self.node.teeth.children:
            radius = np.linalg.norm(part.mesh.vertices[:, :2], axis=1)
            self.assertGreater(radius.min(), 49.05)
            self.assertLess(radius.max(), 52.5)
            self.assertGreater(part.mesh.bounds[0, 2], 9)
            self.assertNotIntersecting(part, self.node.cover)

    def test_layers_do_not_interpenetrate(self):
        self.assertNoSolidInterference(self.node.teeth)
