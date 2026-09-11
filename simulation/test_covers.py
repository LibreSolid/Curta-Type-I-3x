"""A correct dial needs room to rotate inside its visible housing."""

from solid_node.test import TestCase
from simulation.covers import CoverClearanceBench
from simulation.standard.parts import ResultsDialType1, ResultsDialType2
from simulation.tools.interference import rigid_leaves


class CoverClearanceTest(TestCase):
    node = CoverClearanceBench

    def clear_dials(self):
        carriage = self.node.carriage.registers
        dials = [part for _, part in rigid_leaves(carriage)
                 if isinstance(part, (ResultsDialType1, ResultsDialType2))]
        self.assertEqual(len(dials), 17)
        for dial in dials:
            self.assertNotIntersecting(dial, carriage.covers.digits_cover)
            self.assertNotIntersecting(dial, carriage.covers.upper_housing)

    def test_every_integer_digit_clears_both_covers(self):
        for digit in range(10):
            self.node.set_state(**(self.node.instructions['Rest'].targets |
                                dict(initial_result=digit*11111111111, initial_turns=digit*111111)))
            self.clear_dials()

    def test_carry_and_clearing_turns_clear_both_covers(self):
        for angle in range(0, 361, 2):
            self.node.set_state(**(self.node.instructions['Rest'].targets |
                                dict(initial_result=99999999999, initial_turns=999999,
                                     operand=1, crank_turns=angle/360)))
            self.clear_dials()

        for step in range(101):
            self.node.set_state(**(self.node.instructions['Rest'].targets |
                                dict(initial_result=98765432109, initial_turns=987654,
                                     clear=step/100, carriage_position=5)))
            self.clear_dials()

    def test_cover_fit_preserves_every_author_supplied_print_vertex(self):
        from math import radians
        import trimesh
        from scipy.spatial import cKDTree
        self.node.set_state(**self.node.instructions['Rest'].targets)
        covers = self.node.carriage.registers.covers
        for node, angle, axis, height in (
            (covers.digits_cover, -180, (.168920173, .985629735, 0), 31.65),
            (covers.upper_housing, 160.549916905, (0, 0, 1), -4.35),
        ):
            expected = trimesh.load_mesh(node.stl_source)
            expected.apply_transform(trimesh.transformations.rotation_matrix(radians(angle), axis))
            expected.apply_translation((0, 0, height))
            expected.apply_transform(trimesh.transformations.rotation_matrix(radians(-.549916905), (0, 0, 1)))
            actual = node.mesh
            self.assertEqual(len(actual.faces), len(expected.faces))
            self.assertLess(cKDTree(expected.vertices).query(actual.vertices)[0].max(), .00001)
            self.assertLess(cKDTree(actual.vertices).query(expected.vertices)[0].max(), .00001)
