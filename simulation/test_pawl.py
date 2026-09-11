"""Ratchet motion must lift the pawl instead of passing through it."""

import numpy as np
from solid_node.test import TestCase
from simulation.pawl import PawlBench
from simulation.pawl import RELEASE, TOOTH_PITCH, CLOSING_RELEASE


class PawlTest(TestCase):
    node = PawlBench

    def test_pawl_follows_the_ramp(self):
        pawl = self.node.pawl.reverse_rotation_prevention_pawl
        self.node.set_state(crank_turns=1/360)
        first = pawl.mesh.vertices.copy()
        self.node.set_state(crank_turns=3/360)
        self.assertGreater(np.max(np.abs(pawl.mesh.vertices - first)), .5)

    def test_pawl_clears_a_complete_ratchet_turn(self):
        angles = list(range(361))
        for tooth in (0, 1, 20, 60, 97):
            release = RELEASE + tooth * TOOTH_PITCH
            angles += [release + offset / 100 for offset in range(-12, 13)]
        angles += [CLOSING_RELEASE + offset / 100 for offset in range(-12, 13)]
        for angle in angles:
            self.node.set_state(crank_turns=angle/360)
            self.assertNotIntersecting(self.node.disc,
                                       self.node.pawl.reverse_rotation_prevention_pawl)

    def test_spring_and_pawl_clear_the_mounting_plate(self):
        for angle in (0, 1, 3, 100, 301.83, 301.84):
            self.node.set_state(crank_turns=angle/360)
            self.assertNotIntersecting(self.node.pawl.reverse_rotation_prevention_pawl,
                                       self.node.bearing_plate.bearing_plate)
            self.assertNotIntersecting(self.node.pawl.documented_spring.wire,
                                       self.node.bearing_plate.bearing_plate)

    def test_engaged_pawl_blocks_reverse_and_can_release_clear_of_the_tooth(self):
        pawl = self.node.pawl.reverse_rotation_prevention_pawl
        for tooth in (0, 40, 90):
            release = RELEASE + tooth * TOOTH_PITCH
            self.node.set_state(crank_turns=(release + 1)/360)
            self.assertFreeWithin(self.node.disc, .01, against=pawl)
            # The source disc is inverted: local -Z is world counter-clockwise.
            # There is tooth-pitch backlash, not an ideal zero-play one-way clutch.
            self.assertBlockedBeyond(self.node.disc, 1.2, against=pawl,
                                     axis=(0, 0, -1), directions='forward')
            self.node.set_state(crank_turns=(release + .005)/360)
            self.assertFreeWithin(pawl, [.5, 1, 2, 3], against=self.node.disc,
                                  axis=(0, 0, -1), directions='forward')

    def test_spring_stays_in_its_mounts_as_the_pawl_moves(self):
        from simulation.fit import PAWL_PIVOT, PAWL_SPRING_ANCHOR, PAWL_SPRING_HOLE
        from solid_node.math import turn
        wire = self.node.pawl.documented_spring.wire
        pawl = self.node.pawl.reverse_rotation_prevention_pawl
        for angle in (0, 1, 3, 100, 301.83, 301.84):
            self.node.set_state(crank_turns=angle/360)
            point = turn(PAWL_SPRING_HOLE[:2], pawl.turn.value, about=PAWL_PIVOT[:2])
            expected = (PAWL_SPRING_ANCHOR, (*point, PAWL_SPRING_HOLE[2]))
            self.assertLess(np.max(np.abs(wire.mesh.vertices[-2:] - expected)), .001)
            shape = wire.shape()
            self.assertTrue(shape.isValid())
            self.assertEqual(len(shape.Solids()), 1)
            self.assertNotIntersecting(wire, pawl)
            self.assertNotIntersecting(wire, self.node.pawl.anti_reversal_m5_bolt_sleeve)

    def test_documented_wire_and_preview_budget(self):
        from math import pi
        self.node.set_state(crank_turns=0)
        wire = self.node.pawl.documented_spring.wire
        self.assertLess(len(wire.mesh.faces), 50000)
        caps = [face for face in wire.shape().Faces() if face.geomType() == 'PLANE']
        self.assertEqual(len(caps), 2)
        for cap in caps:
            self.assertAlmostEqual(cap.Area(), pi*.3**2, places=5)
