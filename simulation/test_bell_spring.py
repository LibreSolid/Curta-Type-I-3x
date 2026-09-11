"""The bell's spring is attached to the bell and follows the sliding drum."""

import numpy as np
from solid_node.test import TestCase
from simulation.bell_spring import BellSpringBench, BellLeafFitBench, BellLeafContactBench
from simulation.tools.interference import rigid_leaves, world_solids


def material_leaves(node):
    if not node.children:
        yield node
    else:
        for child in node.children:
            yield from material_leaves(child)


class BellSpringTest(TestCase):
    node = BellSpringBench

    def rest(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)

    def test_spring_fasteners_follow_the_bell(self):
        self.rest()
        names = {'m4x10_419159_1', 'm4x10_419159_2'}
        screws = [part for _, part in rigid_leaves(self.node) if part.name in names]
        self.assertEqual(len(screws), 2)
        before = [part.mesh.vertices.copy() for part in screws]
        self.node.set_state(crank_turns=.25)
        rotation = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
        for screw, vertices in zip(screws, before):
            self.assertLess(np.max(np.abs(screw.mesh.vertices - vertices @ rotation.T)), .00001)

    def test_spring_mount_follows_the_bell(self):
        self.rest()
        spring = self.node.carry_mechanism.tens_bell.tens_bell_spring
        mount = getattr(spring, 'mount', spring)
        before = mount.mesh.vertices.copy()
        held = before[:, 2] > -8.71
        self.assertGreater(held.sum(), 20)
        self.node.set_state(crank_turns=.25)
        rotation = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
        self.assertLess(np.max(np.abs(mount.mesh.vertices[held] - before[held] @ rotation.T)), .00001)

    def test_leaf_spring_clears_the_drum_through_subtraction_travel(self):
        self.rest()
        spring = self.node.carry_mechanism.tens_bell.tens_bell_spring
        drum = [part for _, part in rigid_leaves(self.node.main_drive.stepped_drum)]
        for step in range(37):
            self.node.set_state(subtract=step/36)
            for leaf in material_leaves(spring):
                for body in drum:
                    self.assertNotIntersecting(leaf, body)


class BellLeafShapeTest(TestCase):
    node = BellLeafFitBench

    def physical_spring(self, spread=0):
        patches = [shape for path, shape in world_solids(self.node, include_flexible=True).items()
                   if '.spring.' in path]
        self.assertEqual(len(patches), 5)
        for shape in patches:
            self.assertTrue(shape.isValid())
            self.assertEqual(len(shape.Solids()), 1)
        united = patches[0].fuse(*patches[1:])
        self.assertTrue(united.isValid(), f'physical spring at {spread} mm spread')
        self.assertEqual(len(united.Solids()), 1)
        return united

    def test_unloaded_reconstruction_preserves_source_except_rib_chords(self):
        import cadquery as cq
        from simulation.standard.parts import TensBellSpring
        from simulation.retaining_spring import ROOT_X, ROOT_Z, ARM_LENGTH, JOIN, SINE, COSINE, MOUNT_Z
        self.node.set_state(spread=0, subtract=0)
        assembled = self.physical_spring()
        source = TensBellSpring().shape().translate((0, 0, MOUNT_Z))
        self.assertEqual(assembled.cut(source).Volume(), 0)
        missing = source.cut(assembled)
        self.assertGreater(missing.Volume(), 0)
        self.assertLess(missing.Volume(), .27)  # analytic bound for the two 24-chord R .9 ribs
        for side in (-1, 1):
            axis = (-side*SINE, 0, -COSINE)
            origin = (side*(ROOT_X + JOIN*SINE - .9*COSINE), 0,
                      ROOT_Z + JOIN*COSINE + .9*SINE + MOUNT_Z)
            scope = cq.Solid.makeCylinder(.901, ARM_LENGTH + 2*JOIN,
                                          cq.Vector(*origin), cq.Vector(*axis))
            missing = missing.cut(scope)
        self.assertEqual(missing.Volume(), 0)

    def test_five_patches_remain_one_physical_body_while_bending(self):
        for spread in (0, 2, 4, 6, 8):
            self.node.set_state(spread=spread, subtract=0)
            self.physical_spring(spread)


class BellLeafContactTest(TestCase):
    node = BellLeafContactBench

    def test_mount_is_seated_under_the_bell(self):
        self.node.set_state(subtract=0)
        mount = self.node.spring.mount
        self.assertFreeWithin(mount, .01, against=self.node.bell, along=(0, 0, 1))
        self.assertBlockedBeyond(mount, .1, against=self.node.bell,
                                 along=(0, 0, 1), directions='forward')

    def test_spring_clears_bell_and_drum_through_all_subtraction_travel(self):
        bodies = [self.node.bell, *(part for _, part in rigid_leaves(self.node.drum))]
        for step in range(37):
            self.node.set_state(subtract=step/36)
            for leaf in material_leaves(self.node.spring):
                for body in bodies:
                    self.assertNotIntersecting(leaf, body)

    def test_hooks_are_seated_on_the_drum_pockets(self):
        bodies = [part for _, part in rigid_leaves(self.node.drum)]
        for step in range(37):
            self.node.set_state(subtract=step/36)
            for side, hook in ((1, self.node.spring.right_hook),
                               (-1, self.node.spring.left_hook)):
                for body in bodies:
                    self.assertFreeWithin(hook, .01, against=body, along=(1, 0, 0))
                contact = (self.node.drum.main_axle_step_drum_top_1 if step/4 < 7.6
                           else self.node.drum.main_axle_step_drum_bottom_1)
                self.assertBlockedBeyond(hook, .2, against=contact,
                                         along=(-side, 0, 0), directions='forward')
