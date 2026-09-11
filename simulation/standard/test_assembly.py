"""Every placed mesh must reproduce its STEP occurrence's full world frame."""

import numpy as np
import trimesh

from solid_node.node.adapters.step import StepAssembly
from solid_node.test import TestCase

from simulation.source import STEP
from simulation.standard.assembly import CurtaAssembly


def rigid_leaves(node):
    if node.rigid:
        yield node
    else:
        for child in node.children:
            yield from rigid_leaves(child)


class SourcePlacementTest(TestCase):
    node = CurtaAssembly

    def test_every_source_occurrence_keeps_its_world_placement(self):
        source = StepAssembly(STEP)
        part_names = {part.name for part in source.products if part.kind == "part"}
        occurrences = [item for item in source.occurrences
                       if item.product_name in part_names]
        actual = list(rigid_leaves(self.node))
        self.assertEqual(len(actual), len(occurrences))
        self.assertEqual(len(actual), 547)
        local_meshes = {}
        for part, occurrence in zip(actual, occurrences):
            self.assertEqual(part.part, occurrence.product_name)
            if part.stl_file not in local_meshes:
                local_meshes[part.stl_file] = trimesh.load_mesh(part.stl_file)
            local = local_meshes[part.stl_file].vertices
            expected = local @ occurrence.world_matrix[:3, :3].T
            expected += occurrence.world_matrix[:3, 3]
            error = np.max(np.linalg.norm(part.mesh.vertices - expected, axis=1))
            self.assertLess(error, 0.00001,
                            f"{occurrence.identity} {part.part}: {error} mm drift")
