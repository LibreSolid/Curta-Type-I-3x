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

    def test_subtraction_lifts_crank_and_drum_nine_millimeters(self):
        import numpy as np
        self.node.set_state(subtract=0, crank_turns=0)
        crank = self.node.main_drive.crank.crank_handle_1.main_crank
        drum = self.node.main_drive.stepped_drum.main_axle_step_drum_1.main_axle_step_drum_top_1
        before = [part.mesh.vertices.copy() for part in (crank, drum)]
        self.node.set_state(subtract=1)
        for part, vertices in zip((crank, drum), before):
            self.assertLess(np.max(np.abs(part.mesh.vertices - vertices - [0, 0, 9])), .00001)

    def test_positive_crank_turn_is_clockwise_from_above(self):
        import numpy as np
        self.node.set_state(crank_turns=0)
        crank = self.node.main_drive.crank.crank_handle_1.main_crank
        before = crank.mesh.vertices.copy()
        self.node.set_state(crank_turns=.25)
        rotation = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
        self.assertLess(np.max(np.abs(crank.mesh.vertices - before @ rotation.T)), .00001)

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
