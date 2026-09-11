"""The analytic patches remain one original spring, including at maximum bend."""

from solid_node.test import TestCase
from simulation.spider_bank import SpiderBankBench
from simulation.standard.parts import SpiderSpring
from simulation.tools.interference import world_solids


class SpiderBankTest(TestCase):
    node = SpiderBankBench

    def physical_spring(self):
        shapes = list(world_solids(self.node, include_flexible=True).values())
        self.assertEqual(len(shapes), 35)
        for shape in shapes:
            self.assertTrue(shape.isValid())
            self.assertEqual(len(shape.Solids()), 1)
        united = shapes[0].fuse(*shapes[1:])
        self.assertTrue(united.isValid())
        self.assertEqual(len(united.Solids()), 1)
        return united

    def test_unloaded_bank_retains_native_ring_and_tips(self):
        self.node.set_state(rise=0)
        original = SpiderSpring().shape()
        reconstructed = self.physical_spring()
        self.assertEqual(reconstructed.cut(original).Volume(), 0)
        missing = original.cut(reconstructed)
        self.assertGreater(missing.Volume(), 0)
        self.assertLess(missing.Volume(), 17*.54)
        skin = original.cut(original.translate((0, 0, -.007)))
        self.assertEqual(missing.cut(skin).Volume(), 0)

    def test_installed_and_crest_bends_keep_every_finger_connected(self):
        for rise in (1.4, 2.2, 3):
            self.node.set_state(rise=rise)
            self.physical_spring()
