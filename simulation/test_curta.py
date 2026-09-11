"""Assembly contracts, including the source interfaces not yet implemented."""

from solid_node.test import TestCase

from simulation.curta import Curta


def leaves(node):
    if node.rigid:
        yield node
    else:
        for child in node.children:
            yield from leaves(child)


class CurtaTest(TestCase):
    node = Curta

    def test_source_inventory(self):
        self.assertEqual(len(list(leaves(self.node))), 547)

    def test_solid_integrity(self):
        self.assertNoDisconnectedSolids(self.node)

    def test_source_shapes_valid(self):
        invalid = sorted({part.part for part in leaves(self.node)
                          if not part.shape().isValid()})
        self.assertEqual(invalid, [])

    def test_assembly_integrity(self):
        self.assertNoSolidInterference(self.node)
