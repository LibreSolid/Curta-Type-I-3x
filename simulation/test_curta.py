"""Assembly contracts, including the source interfaces not yet implemented."""

from solid_node.test import TestCase

from simulation.curta import Curta


def leaves(node):
    if not node.children:
        yield node
    else:
        for child in node.children:
            yield from leaves(child)


class CurtaTest(TestCase):
    node = Curta

    def test_calculator_register_state(self):
        self.node.set_state(initial_result=492, initial_turns=4, operand=123,
                            crank_turns=2, carriage_position=1, subtract=0, clear=0)
        self.assertEqual(self.node.result.value, 2952)
        self.assertEqual(self.node.turns_counter.value, 24)
        self.node.set_state(initial_result=0, initial_turns=0, operand=0,
                            crank_turns=0, carriage_position=0)

    def test_controls_leave_frame_fixed(self):
        import numpy as np
        body = self.node.frame.upper_frame.main_body
        before = body.mesh.vertices.copy()
        self.node.set_state(operand=99999999, crank_turns=0.25)
        np.testing.assert_array_equal(body.mesh.vertices, before)
        self.node.set_state(operand=0, crank_turns=0)

    def test_source_inventory(self):
        self.assertEqual(len(list(leaves(self.node))), 547)

    def test_solid_integrity(self):
        self.assertNoDisconnectedSolids(self.node)

    def test_source_shapes_valid(self):
        invalid = sorted({part.name for part in leaves(self.node)
                          if not (part.shape().isValid() if part.exact
                                  else part.mesh.is_watertight and part.mesh.volume > 0)})
        self.assertEqual(invalid, [])

    def test_assembly_integrity(self):
        self.assertNoSolidInterference(self.node)
