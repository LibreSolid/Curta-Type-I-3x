"""Colors distinguish mechanical roles on real leaves, not empty assemblies."""

from solid_node.test import TestCase
from simulation.display import DisplayBench
from simulation.tools.interference import rigid_leaves


class DisplayTest(TestCase):
    node = DisplayBench

    def test_housing_structure_gears_and_readouts_have_distinct_colors(self):
        from simulation.standard import parts, printed
        expected = {
            parts.BottomHousing: '#222831',
            parts.SelectorKnob: '#222831',
            parts.MainBody: '#b9c5cd',
            printed.MainAxleStepDrumTop1: '#b9c5cd',
            printed.Part10230_410008_1_419032: '#b68a46',
            parts.NumberRoll: '#eadfc6',
            parts.ResultsDialType1: '#eadfc6',
            parts.Part6mmBall419241: '#96a8b8',
        }
        found = set()
        for _, node in rigid_leaves(self.node):
            for kind, color in expected.items():
                if isinstance(node, kind):
                    self.assertEqual(node.color, color, type(node).__name__)
                    found.add(kind)
        self.assertEqual(found, set(expected))

    def test_source_stl_covers_and_flexible_springs_join_the_palette(self):
        carriage = self.node.carriage.registers
        self.assertEqual(carriage.covers.digits_cover.color, '#222831')
        self.assertEqual(carriage.covers.upper_housing.color, '#222831')
        self.assertEqual(carriage.dial_detents.spider_spring.result_1.arm.color, '#96a8b8')
        self.assertEqual(carriage.carrier.upper_carriage_body_1.clearing_pin_spring.wire.color,
                         '#96a8b8')
