"""Regrouping must neither lose a part nor change a single source placement."""

from collections import defaultdict
import numpy as np
from solid_node.test import TestCase
from simulation.assemblies import LayeredSource
from simulation.standard.assembly import CurtaAssembly


def inventory(node):
    found = defaultdict(list)

    def visit(part):
        if part.rigid:
            found[part.part].append(part.mesh.vertices)
        else:
            for child in part.children:
                visit(child)

    visit(node)
    return {name: sorted(meshes, key=lambda v: tuple(v.mean(axis=0).round(4)))
            for name, meshes in found.items()}


class EducationalLayersTest(TestCase):
    node = LayeredSource

    def test_all_source_placements_preserved(self):
        source = CurtaAssembly()
        source.assemble()
        source.build_stls()
        expected, actual = inventory(source), inventory(self.node)
        self.assertEqual(expected.keys(), actual.keys())
        self.assertEqual(sum(map(len, actual.values())), 547)
        for name, meshes in expected.items():
            self.assertEqual(len(meshes), len(actual[name]), name)
            for before, after in zip(meshes, actual[name]):
                self.assertLess(np.max(np.abs(before - after)), 0.00001, name)

    def test_readable_layers_and_register_banks(self):
        self.assertEqual([node.name for node in self.node.children], [
            'enclosure', 'frame', 'input_selectors', 'main_drive',
            'transmission', 'carry_mechanism', 'carriage'])
        carriage = self.node.carriage.registers
        self.assertEqual(len(carriage.result_register.children), 11)
        self.assertEqual(len(carriage.turns_register.children), 6)
