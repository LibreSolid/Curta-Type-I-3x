"""The omitted strips must be bent into the measured cover groove."""

import numpy as np
from solid_node.test import TestCase
from simulation.clearing import ClearingBench, GROOVE_FLOOR, SEAT_GAP
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
            self.assertGreater(part.mesh.bounds[0, 2], GROOVE_FLOOR)
            self.assertAlmostEqual(part.mesh.bounds[0, 2], GROOVE_FLOOR + SEAT_GAP, places=5)
            self.assertNotIntersecting(part, self.node.cover)

    def test_layers_do_not_interpenetrate(self):
        self.assertNoSolidInterference(self.node.teeth)

    def test_screw_relief_changes_only_the_small_back_region(self):
        import trimesh
        from simulation.tools.clearing_relief import faces
        for part in self.node.teeth.children:
            formed = part.form(trimesh.load_mesh(part.stl_source))
            self.assertGreater(formed.volume - part.mesh.volume, 0)
            # Audit every changed face directly. A second boolean between
            # coincident copies invents slivers (including after float32 STL
            # export); no epsilon is used to hide them. Faces outside this
            # small back region must be bit-for-bit identical to the source.
            changed = np.array(list(faces(formed) ^ faces(part.mesh))).reshape(-1, 3)
            self.assertGreater(len(changed), 0)
            reach = float(part.retaining_bore) + 1  # at most one refined source edge
            lower = (.13205562 - reach, -53.5, GROOVE_FLOOR)
            upper = (.13205562 + reach, -48, GROOVE_FLOOR + 3.5)
            self.assertTrue(np.all(changed >= lower))
            self.assertTrue(np.all(changed <= upper))
