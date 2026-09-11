"""Assembly contracts, including the source interfaces not yet implemented."""

from solid_node.test import TestCase

from simulation.curta import Curta
from simulation.contracts import assert_connected_material


def leaves(node):
    if not node.children:
        yield node
    else:
        for child in node.children:
            yield from leaves(child)


class CurtaTest(TestCase):
    node = Curta

    def test_carry_bell_follows_crank_but_stays_at_its_bearing_height(self):
        import numpy as np
        self.node.set_state(crank_turns=0, subtract=0)
        bell = self.node.carry_mechanism.tens_bell.tens_bell_1
        before = bell.mesh.vertices.copy()
        self.node.set_state(crank_turns=.25, subtract=1)
        rotation = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
        self.assertLess(np.max(np.abs(bell.mesh.vertices - before @ rotation.T)), .00001)

    def test_carriage_advances_twenty_degrees_per_decimal_position(self):
        import numpy as np
        from math import sin, cos, radians
        self.node.set_state(carriage_position=0, carriage_lift=0, clear=0, crank_turns=0)
        carrier = self.node.carriage.registers.carrier.upper_carriage_body_1.counter_body
        before = carrier.mesh.vertices.copy()
        self.node.set_state(carriage_position=1)
        angle = radians(20)
        rotation = np.array([[cos(angle), -sin(angle), 0],
                             [sin(angle), cos(angle), 0], [0, 0, 1]])
        self.assertLess(np.max(np.abs(carrier.mesh.vertices - before @ rotation.T)), .00001)

    def test_lifting_carriage_moves_dials_six_mm_and_leaves_shafts_fixed(self):
        import numpy as np
        self.node.set_state(carriage_position=0, carriage_lift=0, clear=0, crank_turns=0)
        dial = self.node.carriage.registers.result_register.p_10203_1.results_dial_type_1
        shaft = self.node.transmission.result.ones.p_10208_1.transmission_gear_tip
        before, fixed = dial.mesh.vertices.copy(), shaft.mesh.vertices.copy()
        self.node.set_state(carriage_lift=1)
        self.assertLess(np.max(np.abs(dial.mesh.vertices - before - [0, 0, 6])), .00001)
        np.testing.assert_array_equal(shaft.mesh.vertices, fixed)
        self.assertNotIntersecting(dial, shaft)

    def test_clearing_turns_the_plate_with_carriage_lifted(self):
        import numpy as np
        self.node.set_state(carriage_position=0, carriage_lift=0, clear=0, crank_turns=0)
        plate = next(part for part in leaves(self.node) if part.name == 'clearing_cover')
        before = plate.mesh.vertices.copy()
        self.node.set_state(clear=.5)
        expected = before * [-1, -1, 1] + [0, 0, 6]
        self.assertLess(np.max(np.abs(plate.mesh.vertices - expected)), .00001)

    def test_lower_decimal_markers_stay_fixed_when_carriage_moves(self):
        import numpy as np
        self.node.set_state(carriage_position=0, carriage_lift=0, clear=0)
        markers = [part for part in leaves(self.node)
                   if part.name == 'position_marker' and part.mesh.centroid[2] < 0]
        self.assertEqual(len(markers), 5)
        before = [part.mesh.vertices.copy() for part in markers]
        self.node.set_state(carriage_position=1, carriage_lift=1, clear=.5)
        for marker, points in zip(markers, before):
            np.testing.assert_array_equal(marker.mesh.vertices, points)

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
        from simulation.clearing import ClearingTeeth, ClearingSpacer
        from simulation.retaining_spring import RetainingSpring

        def occurrences(node):
            if isinstance(node, RetainingSpring):
                # The native union contract proves these five material patches
                # are one original printed part, not five source occurrences.
                self.assertEqual(len(list(leaves(node))), 5)
                yield node
            elif not node.children:
                yield node
            else:
                for child in node.children:
                    yield from occurrences(child)

        parts = list(occurrences(self.node))
        self.assertEqual(sum(isinstance(part, RetainingSpring) for part in parts), 1)
        supplement = [part for part in parts if isinstance(part, (ClearingTeeth, ClearingSpacer))]
        self.assertEqual(len(supplement), 3)  # Manual page 38: absent from STEP, present as STLs.
        self.assertEqual(len(parts) - len(supplement), 547)

    def test_solid_integrity(self):
        def check(node):
            if node.rigid or not node.children:
                try:
                    assert_connected_material(node.mesh)
                    if node.exact:
                        self.assertEqual(len(node.shape().Solids()), 1)
                except AssertionError as error:
                    raise AssertionError(f'{node.name}: {error}') from error
            else:
                for child in node.children:
                    check(child)
        check(self.node)

    def test_source_shapes_valid(self):
        invalid = sorted({part.name for part in leaves(self.node)
                          if not (part.shape().isValid() if part.exact
                                  else part.mesh.is_watertight and part.mesh.volume > 0)})
        self.assertEqual(invalid, [])

    def test_assembly_integrity(self):
        self.assertNoSolidInterference(self.node)
