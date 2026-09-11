"""The cam turns, its retained height stays fixed, and the roller follows it."""

import numpy as np
from solid_node.test import TestCase
from simulation.zero import ZeroCamBench
from simulation.flexibles import FIXED_PIN, LEVER_PIN, ZERO_PIVOT
from solid_node.math import turn


def find(node, name):
    if node.name == name:
        return node
    for child in node.children:
        found = find(child, name)
        if found is not None:
            return found


class ZeroCamTest(TestCase):
    node = ZeroCamBench

    def test_disc_turns_clockwise_without_subtraction_lift(self):
        self.node.set_state(crank_turns=0, subtract=0)
        disc = find(self.node, 'zero_positioning_disc')
        before = disc.mesh.vertices.copy()
        self.node.set_state(crank_turns=.25, subtract=1)
        rotation = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
        self.assertLess(np.max(np.abs(disc.mesh.vertices - before @ rotation.T)), .00001)

    def test_follower_leaves_and_returns_to_the_zero_detent(self):
        self.node.set_state(crank_turns=0, subtract=0)
        roller = find(self.node, 'zero_positioning_disc_roller')
        before = roller.mesh.vertices.copy()
        self.node.set_state(crank_turns=.25)
        self.assertGreater(roller.mesh.centroid[0] - before.mean(axis=0)[0], 4)
        self.node.set_state(crank_turns=1)
        self.assertLess(np.max(np.abs(roller.mesh.vertices - before)), .00001)

    def test_roller_clears_the_complete_cam_turn(self):
        disc = find(self.node, 'zero_positioning_disc')
        roller = find(self.node, 'zero_positioning_disc_roller')
        # Quarter-degree samples include the interpolation between measured knots.
        angles = [index / 4 for index in range(61)]
        angles += list(range(15, 339, 3))
        angles += [index / 4 for index in range(1356, 1441)]
        for angle in angles:
            self.node.set_state(crank_turns=angle/360, subtract=0)
            self.assertNotIntersecting(roller, disc)

    def test_drive_pin_slides_in_the_retained_disc_slots(self):
        disc = find(self.node, 'zero_positioning_disc')
        pin = find(self.node, 'zero_positioning_disc_pin')
        self.node.set_state(crank_turns=0, subtract=0)
        before = pin.mesh.vertices.copy()
        self.node.set_state(subtract=1)
        self.assertLess(np.max(np.abs(pin.mesh.vertices - before - (0, 0, 9))), .00001)
        for raised in (0, .25, .5, .75, 1):
            self.node.set_state(subtract=raised)
            self.assertNotIntersecting(pin, disc)

    def test_roller_is_seated_on_the_cam_not_floating_away(self):
        disc = find(self.node, 'zero_positioning_disc')
        roller = find(self.node, 'zero_positioning_disc_roller')
        for angle in (4, 14, 90, 340, 350, 356):
            self.node.set_state(crank_turns=angle/360, subtract=0)
            # At the steep detent flank, radial-X motion is almost tangential.
            # Measure the actual nearest contact normal, then express it in the
            # roller's own frame, as the perturbation API requires.
            from OCP.BRepExtrema import BRepExtrema_DistShapeShape
            from simulation.tools.interference import world_solids
            solids = world_solids(self.node)
            a = next(shape for path, shape in solids.items()
                     if path.endswith('.zero_positioning_disc_roller'))
            b = next(shape for path, shape in solids.items()
                     if path.endswith('.zero_positioning_disc'))
            contact = BRepExtrema_DistShapeShape(a.wrapped, b.wrapped)
            self.assertTrue(contact.IsDone())
            first, second = contact.PointOnShape1(1), contact.PointOnShape2(1)
            direction = np.array((second.X()-first.X(), second.Y()-first.Y(),
                                  second.Z()-first.Z())) / contact.Value()
            local = turn(direction[:2], -self.node.mechanism.follower.turn.value)
            along = tuple(float(value) for value in (*local, direction[2]))
            self.assertLess(contact.Value(), .08, f'crank={angle}')
            self.assertFreeWithin(roller, .01, against=disc, along=along)
            self.assertBlockedBeyond(roller, .2, against=disc, along=along,
                                     directions='forward')

    def test_spring_terminals_follow_the_two_mounts(self):
        mechanism = self.node.mechanism
        wire = mechanism.documented_spring.wire
        for angle in (0, 2, 5, 10, 90, 345, 355, 360):
            self.node.set_state(crank_turns=angle/360, subtract=0)
            point = turn(LEVER_PIN[:2], mechanism.follower.turn.value, about=ZERO_PIVOT)
            expected = (FIXED_PIN, (*point, LEVER_PIN[2]))
            caps = wire.mesh.vertices[-2:]
            self.assertLess(np.max(np.abs(caps - expected)), .001)
            shape = wire.shape()
            self.assertTrue(shape.isValid())
            self.assertEqual(len(shape.Solids()), 1)
            self.assertNotIntersecting(wire, mechanism.follower.zero_positioning_lever)
            self.assertNotIntersecting(wire, mechanism.zero_positioning_m5_bolt_sleeve)
            self.assertNotIntersecting(wire, self.node.bearing_plate.bearing_plate)
