"""Carry motion is vertical travel within a fixed bearing, not an axle rotation."""

import numpy as np
from solid_node.test import TestCase
from simulation.carry import CarryBench, TurnsCarryBench


class CarryBenchTest(TestCase):
    node = CarryBench

    def slider(self):
        return next(child for child in self.node.children if child.name.startswith('tens_slider_'))

    def test_engaging_lowers_the_lever_four_point_two_mm(self):
        self.node.set_state(engaged=0)
        lever, bearing = self.slider(), self.node.tens_slide_bearing
        before, fixed = lever.mesh.vertices.copy(), bearing.mesh.vertices.copy()
        self.node.set_state(engaged=1)
        self.assertLess(np.max(np.abs(lever.mesh.vertices - before - [0, 0, -4.2])), .00001)
        np.testing.assert_array_equal(bearing.mesh.vertices, fixed)

    def test_reset_revisits_the_identical_rest_mesh(self):
        self.node.set_state(engaged=0)
        before = self.slider().mesh.vertices.copy()
        self.node.set_state(engaged=1)
        self.node.set_state(engaged=0)
        np.testing.assert_array_equal(self.slider().mesh.vertices, before)

    def test_spring_clears_its_bearing(self):
        for engaged in (0, .25, .5, .75, 1):
            self.node.set_state(engaged=engaged)
            self.assertNotIntersecting(self.node.carry_lever_spring.wire, self.node.tens_slide_bearing)

    def test_spring_is_one_documented_wire_and_its_closed_fold_stays_seated(self):
        from math import pi
        self.node.set_state(engaged=0)
        wire = self.node.carry_lever_spring.wire
        # Circle-profile vertices can rotate around the same fixed centerline
        # as the transported frame changes. Ring centers measure the mount,
        # independently of that harmless faceted cross-section phase.
        def centers():
            return wire.mesh.vertices[:-2].reshape(-1, 24, 3).mean(axis=1)
        before = centers()
        held = before[:, 2] < before[:, 2].min() + .5
        self.assertGreater(held.sum(), 20)
        for engaged in (0, .25, .5, .75, 1):
            self.node.set_state(engaged=engaged)
            shape = wire.shape()
            self.assertTrue(shape.isValid())
            self.assertEqual(len(shape.Solids()), 1)
            self.assertLess(len(wire.mesh.faces), 20000)
            caps = [face for face in shape.Faces() if face.geomType() == 'PLANE']
            self.assertEqual(len(caps), 2)
            for cap in caps:
                self.assertAlmostEqual(cap.Area(), pi*.3**2, places=5)
            self.assertLess(np.max(np.abs(centers()[held] - before[held])), .00001)

    def test_hooks_remain_close_enough_to_retain_the_slider(self):
        for engaged in (.5, .6, 1):
            self.node.set_state(engaged=engaged)
            self.assertFreeWithin(self.node.carry_lever_spring.wire, .01,
                                  against=self.slider(), along=(1, 0, 0))
            self.assertBlockedBeyond(self.node.carry_lever_spring.wire, .2,
                                     against=self.slider(), along=(1, 0, 0))

    def test_spring_follows_the_slider_detents_without_cutting_them(self):
        for index in range(41):
            self.node.set_state(engaged=index/40)
            self.assertNotIntersecting(self.node.carry_lever_spring.wire,
                                       self.slider())


class TurnsCarryBenchTest(CarryBenchTest):
    node = TurnsCarryBench
