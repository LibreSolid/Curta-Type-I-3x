"""A moving tapered finger must retain its source shape and continuous body."""

from solid_node.test import TestCase
from simulation.spider_shape import SpiderShapeBench
from simulation.standard.parts import SpiderSpring
from simulation.tools.interference import world_solids


class SpiderShapeTest(TestCase):
    node = SpiderShapeBench

    def physical_spring(self):
        shapes = list(world_solids(self.node, include_flexible=True).values())
        self.assertEqual(len(shapes), 3)
        for shape in shapes:
            self.assertTrue(shape.isValid())
            self.assertEqual(len(shape.Solids()), 1)
        united = shapes[0].fuse(*shapes[1:])
        self.assertTrue(united.isValid())
        self.assertEqual(len(united.Solids()), 1)
        return united

    def test_unloaded_finger_preserves_source_except_thin_cone_skin(self):
        self.node.set_state(rise=0)
        original = SpiderSpring().shape()
        reconstructed = self.physical_spring()
        self.assertEqual(reconstructed.cut(original).Volume(), 0)
        missing = original.cut(reconstructed)
        self.assertGreater(missing.Volume(), 0)
        self.assertLess(missing.Volume(), .54)  # 17.1 × 4.5 × .007 mm skin bound
        skin = original.cut(original.translate((0, 0, -.007)))
        self.assertEqual(missing.cut(skin).Volume(), 0)

    def test_bent_finger_stays_one_valid_physical_body(self):
        for step in range(7):
            self.node.set_state(rise=step/2)
            self.physical_spring()
