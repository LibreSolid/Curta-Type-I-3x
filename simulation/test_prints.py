"""One printed group is one connected solid, not its separate CAD ingredients."""

from solid_node.test import TestCase
from simulation.prints import PrintedDrive


def rigid_parts(node):
    if node.rigid:
        yield node
    else:
        for child in node.children:
            yield from rigid_parts(child)


class PrintedDriveTest(TestCase):
    node = PrintedDrive

    def test_six_rigid_parts(self):
        # Two drum halves, their three joining pins and one tens bell.
        self.assertEqual(len(list(rigid_parts(self.node))), 6)

    def test_every_print_is_one_body(self):
        self.assertNoDisconnectedSolids(self.node)

    def test_every_print_is_native_valid(self):
        for part in rigid_parts(self.node):
            self.assertTrue(part.shape().isValid(), part.name)
