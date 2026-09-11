"""An input tooth must pass without overlap and actually constrain the pinion."""

from solid_node.test import TestCase
from simulation.input_mesh import InputMesh


class InputMeshTest(TestCase):
    node = InputMesh

    def test_complete_tooth_passage(self):
        for half_degree in range(210, 271):
            self.node.set_state(crank_angle=half_degree / 2)
            self.assertNotIntersecting(self.node.drum_row, self.node.pinion)

    def test_engaged_tooth_constrains_pinion(self):
        self.node.set_state(crank_angle=120)
        self.assertFreeWithin(self.node.pinion, 0.1, against=self.node.drum_row)
        self.assertBlockedBeyond(self.node.pinion, 12, against=self.node.drum_row)
