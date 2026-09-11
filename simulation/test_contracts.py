"""A cavity is empty space, while a separate positive shell is another body."""

import unittest
import trimesh
from simulation.contracts import assert_connected_material


class MaterialConnectivityTest(unittest.TestCase):
    def test_enclosed_void_is_not_another_material_body(self):
        outside = trimesh.creation.box((10, 10, 10))
        cavity = trimesh.creation.box((2, 2, 2))
        cavity.invert()
        assert_connected_material(trimesh.util.concatenate([outside, cavity]))

    def test_detached_material_is_rejected(self):
        first = trimesh.creation.box((2, 2, 2))
        second = first.copy().apply_translation((5, 0, 0))
        with self.assertRaisesRegex(AssertionError, 'detached'):
            assert_connected_material(trimesh.util.concatenate([first, second]))

    def test_uncontained_negative_shell_is_rejected(self):
        first = trimesh.creation.box((2, 2, 2))
        second = first.copy().apply_translation((5, 0, 0))
        second.invert()
        with self.assertRaisesRegex(AssertionError, 'not enclosed'):
            assert_connected_material(trimesh.util.concatenate([first, second]))
