"""Spring wire stays in its measured holes and outside the printed supports."""

from solid_node.test import TestCase
from simulation.frame import LowerFrame


class SpringMountTest(TestCase):
    node = LowerFrame

    def test_spring_clearance(self):
        frame = self.node
        for support in (frame.zero_positioning_lever,
                        frame.zero_positioning_m5_bolt_sleeve,
                        frame.bearing_plate):
            self.assertNotIntersecting(frame.documented_spring, support)

    def test_terminal_seating(self):
        # Both legs occupy the mounting bores, not merely a nearby free space.
        from simulation.flexibles import FIXED_PIN, LEVER_PIN
        import numpy as np
        shape = self.node.documented_spring.shape()
        centers = [np.array(face.Center().toTuple()) + FIXED_PIN
                   for face in shape.Faces() if face.geomType() == 'PLANE']
        self.assertEqual(len(centers), 2)
        for pin in (FIXED_PIN, LEVER_PIN):
            self.assertLess(min(np.linalg.norm(center - pin)
                                for center in centers), 0.001)
