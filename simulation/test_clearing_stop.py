"""Clearance and follower motion of the documented clearing-ring stop."""

from solid_node.test import TestCase
from simulation.clearing_stop import ClearingStopBench


class ClearingStopTest(TestCase):
    node = ClearingStopBench

    def test_the_clearing_cover_does_not_pass_through_its_stop_pin(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)
        carriage = self.node.carriage.registers
        pin = carriage.carrier.upper_carriage_body_1.clearing_pin
        cover = carriage.clearing_ring.clearing_cover
        # Half-degree cam samples include both short rising/falling ramps.
        for step in range(721):
            self.node.set_state(clear=.1 + .8*step/720)
            try:
                self.assertNotIntersecting(pin, cover)
            except AssertionError as error:
                raise AssertionError(f'clearing cam at {step/2} degrees: {error}') from error

    def test_cover_drives_the_pin_with_bounded_vertical_play(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)
        carriage = self.node.carriage.registers
        pin = carriage.carrier.upper_carriage_body_1.clearing_pin
        cover = carriage.clearing_ring.clearing_cover
        for angle in (0, 5, 14, 200, 218, 230, 240, 360):
            self.node.set_state(clear=.1 + .8*angle/360)
            self.assertFreeWithin(pin, .01, against=cover, along=(0, 0, 1))
            self.assertBlockedBeyond(pin, .2, against=cover,
                                     along=(0, 0, 1), directions='forward')

    def test_clearing_changes_the_pin_height_relative_to_its_sleeve(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)
        carrier = self.node.carriage.registers.carrier.upper_carriage_body_1
        pin, sleeve = carrier.clearing_pin, carrier.clearing_stop_pin_sleeve
        offsets = []
        for clear in (0, .2, .4, .6, .8, 1):
            self.node.set_state(clear=clear)
            offsets.append(pin.mesh.centroid[2] - sleeve.mesh.centroid[2])
        self.assertGreater(max(offsets) - min(offsets), .1)

    def test_spring_clears_the_pin_and_its_sleeve(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)
        carrier = self.node.carriage.registers.carrier.upper_carriage_body_1
        spring = getattr(carrier.clearing_pin_spring, 'wire', carrier.clearing_pin_spring)
        for step in range(37):
            self.node.set_state(clear=step/36)
            self.assertNotIntersecting(spring, carrier.clearing_pin)
            self.assertNotIntersecting(spring, carrier.clearing_stop_pin_sleeve)

    def test_spring_stays_seated_through_compression(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)
        carrier = self.node.carriage.registers.carrier.upper_carriage_body_1
        spring = getattr(carrier.clearing_pin_spring, 'wire', carrier.clearing_pin_spring)
        for clear in (0, .25, .5, .75, 1):
            self.node.set_state(clear=clear)
            for neighbour in (carrier.clearing_pin, carrier.clearing_stop_pin_sleeve):
                self.assertFreeWithin(spring, .01, against=neighbour, along=(0, 0, 1))
            self.assertBlockedBeyond(spring, .2, against=carrier.clearing_pin,
                                     along=(0, 0, -1), directions='forward')
            self.assertBlockedBeyond(spring, .2, against=carrier.clearing_stop_pin_sleeve,
                                     along=(0, 0, 1), directions='forward')

    def test_top_follows_the_pin_while_the_lower_coil_endpoint_stays_fixed(self):
        import numpy as np
        self.node.set_state(**self.node.instructions['Rest'].targets)
        carrier = self.node.carriage.registers.carrier.upper_carriage_body_1
        pin, sleeve = carrier.clearing_pin, carrier.clearing_stop_pin_sleeve
        spring = carrier.clearing_pin_spring.wire
        before = spring.mesh.vertices[-2:].copy() - sleeve.mesh.centroid
        pin_before = pin.mesh.centroid - sleeve.mesh.centroid
        for clear in (.2, .4, .6, .8, 1):
            self.node.set_state(clear=clear)
            caps = spring.mesh.vertices[-2:] - sleeve.mesh.centroid
            travel = pin.mesh.centroid - sleeve.mesh.centroid - pin_before
            self.assertLess(np.max(np.abs(caps[0] - before[0] - travel)), .00001)
            self.assertLess(np.max(np.abs(caps[1] - before[1])), .00001)

    def test_spring_remains_one_valid_point_six_mm_wire(self):
        from math import pi
        self.node.set_state(**self.node.instructions['Rest'].targets)
        spring = self.node.carriage.registers.carrier.upper_carriage_body_1.clearing_pin_spring.wire
        for clear in (0, .25, .5, .75, 1):
            self.node.set_state(clear=clear)
            native = spring.shape()
            self.assertTrue(native.isValid())
            self.assertEqual(len(native.Solids()), 1)
            caps = [face.Area() for face in native.Faces() if face.geomType() == 'PLANE']
            self.assertEqual(len(caps), 2)
            for area in caps:
                self.assertAlmostEqual(area, pi*.3**2, places=5)
