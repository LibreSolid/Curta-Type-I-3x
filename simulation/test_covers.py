"""A correct dial needs room to rotate inside its visible housing."""

from solid_node.test import TestCase
from simulation.covers import CoverClearanceBench
from simulation.standard.parts import ResultsDialType1, ResultsDialType2
from simulation.tools.interference import rigid_leaves


class CoverClearanceTest(TestCase):
    node = CoverClearanceBench

    def test_clearing_ring_clears_the_stationary_digit_cover(self):
        carriage = self.node.carriage.registers
        for step in range(101):
            self.node.set_state(**(self.node.instructions['Rest'].targets |
                                dict(clear=step/100)))
            self.assertNotIntersecting(carriage.covers.digits_cover,
                                       carriage.clearing_ring.clearing_cover)

    def test_fixed_digit_axles_clear_both_cover_seats(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)
        carriage = self.node.carriage.registers
        for index in range(1, 18):
            axle = getattr(carriage.carrier.upper_carriage_body_1, f'digits_axle_{index}')
            self.assertNotIntersecting(axle, carriage.covers.digits_cover)
            self.assertNotIntersecting(axle, carriage.covers.upper_housing)
            self.assertNotIntersecting(axle, carriage.carrier.upper_carriage_body_1.counter_body)
            self.assertNotIntersecting(axle, carriage.carrier.crank_collar)

    def test_clearing_ring_has_an_axial_seat_gap_not_an_unbounded_lift(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)
        carriage = self.node.carriage.registers
        ring = carriage.clearing_ring.clearing_cover
        cover = carriage.covers.digits_cover
        self.assertFreeWithin(ring, .04, against=cover, along=(0, 0, 1))
        # The source ring is upside down: local +Z is down toward this seat.
        self.assertBlockedBeyond(ring, .1, against=cover, along=(0, 0, 1), directions='forward')

    def clear_dials(self):
        carriage = self.node.carriage.registers
        dials = [part for _, part in rigid_leaves(carriage)
                 if isinstance(part, (ResultsDialType1, ResultsDialType2))]
        self.assertEqual(len(dials), 17)
        for dial in dials:
            self.assertNotIntersecting(dial, carriage.covers.digits_cover)
            self.assertNotIntersecting(dial, carriage.covers.upper_housing)

    def test_every_integer_digit_clears_both_covers(self):
        for digit in range(10):
            self.node.set_state(**(self.node.instructions['Rest'].targets |
                                dict(initial_result=digit*11111111111, initial_turns=digit*111111)))
            self.clear_dials()

    def test_carry_and_clearing_turns_clear_both_covers(self):
        for angle in range(0, 361, 2):
            self.node.set_state(**(self.node.instructions['Rest'].targets |
                                dict(initial_result=99999999999, initial_turns=999999,
                                     operand=1, crank_turns=angle/360)))
            self.clear_dials()

        for step in range(101):
            self.node.set_state(**(self.node.instructions['Rest'].targets |
                                dict(initial_result=98765432109, initial_turns=987654,
                                     clear=step/100, carriage_position=5)))
            self.clear_dials()

    def test_cover_fits_preserve_source_outside_the_named_seats(self):
        import numpy as np
        import trimesh
        from simulation.tools.clearing_relief import faces
        from simulation.contracts import assert_connected_material
        from scipy.spatial import cKDTree
        covers = self.node.carriage.registers.covers
        for node in (covers.digits_cover, covers.upper_housing):
            expected = trimesh.load_mesh(node.stl_source)
            actual = trimesh.load_mesh(node.stl_file)
            assert_connected_material(actual)
            removed = expected.volume - actual.volume
            if node is covers.digits_cover:
                self.assertGreater(removed, 180)
                self.assertLess(removed, 190)  # .1 mm facing of the conical inner land.
                quad = expected.vertices[np.all(expected.vertices >= (1.4206, -73.9, -.0436), axis=1) &
                                         np.all(expected.vertices <= (2.2065, -73.8238, .00001), axis=1)]
                self.assertEqual(len(quad), 4)
                self.assertLess(cKDTree(actual.vertices).query(quad)[0].max(), .00001)
            else:
                self.assertGreater(removed, 50)
                self.assertLess(removed, 60)  # Seventeen shallow outer axle seats.
            # The boolean can retriangulate coplanar source faces elsewhere.
            # Audit BOTH directions, including face interiors, at STL coordinate
            # precision. This is a surface-fidelity length, never an overlap
            # epsilon; the independent clearance checks admit no positive volume.
            for first, second in ((expected, actual), (actual, expected)):
                changed = np.array(list(faces(first) - faces(second)), dtype=float).reshape(-1, 3, 3)
                samples = np.concatenate((changed.reshape(-1, 3), changed.mean(axis=1)))
                radius = np.linalg.norm(samples[:, :2], axis=1)
                if node is covers.digits_cover:
                    permitted = (samples[:, 2] >= -12.00001) & (samples[:, 2] <= -11.89999) & (radius < 61.56)
                else:
                    permitted = ((radius > 71.9) & (radius < 73.8) &
                                 (samples[:, 2] > 35.24) & (samples[:, 2] < 36.01))
                protected = samples[~permitted]
                for start in range(0, len(protected), 128):
                    points = protected[start:start+128]
                    _, distances, _ = trimesh.proximity.closest_point(second, points)
                    limits = np.full(len(points), .00001)
                    if node is covers.digits_cover:
                        # Importing this STL into Manifold, even without a cut,
                        # flips one nonplanar quad's diagonal. Its four source
                        # vertices do not move; the two interiors differ by
                        # <.0002 mm. This one measured encoding region is not
                        # permission to relax other surfaces or collision tests.
                        diagonal = (np.all(points >= (1.4206, -73.9, -.0436), axis=1) &
                                    np.all(points <= (2.2065, -73.8238, .00001), axis=1))
                        limits[diagonal] = .0002
                    self.assertTrue(np.all(distances < limits), (distances.max(), points[distances.argmax()]))

    def test_axle_fit_only_lengthens_its_retaining_flat(self):
        import cadquery as cq
        from simulation.standard.parts import DigitsAxle
        current = self.node.carriage.registers.carrier.upper_carriage_body_1.digits_axle_1.shape()
        source = DigitsAxle().shape()
        removed = source.cut(current)
        self.assertTrue(current.isValid())
        self.assertEqual(len(current.Solids()), 1)
        self.assertGreater(removed.Volume(), 0)
        self.assertEqual(current.cut(source).Volume(), 0)
        permitted = cq.Solid.makeBox(3.1, 6, .15, cq.Vector(-4, -3, 1.8))
        self.assertEqual(removed.cut(permitted).Volume(), 0)
        self.assertAlmostEqual(current.BoundingBox().zlen, 54, places=5)
