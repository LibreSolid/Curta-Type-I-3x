"""World-space geometry checks, independent of the declared joint values."""

import numpy as np
from solid_node.test import TestCase
from simulation.drive import DriveTrain


class DriveTrainTest(TestCase):
    node = DriveTrain

    def test_crank_and_drum_turn_about_main_axis(self):
        machine = self.node
        machine.set_state(crank_angle=0)
        crank = machine.crank.main_crank.mesh.vertices.copy()
        drum = machine.drum.main_axle_step_drum_top_1.step_drum_frame_top.mesh.vertices.copy()
        machine.set_state(crank_angle=90)
        # Positive quarter turn in the source's world frame.
        rotation = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        for before, after in ((crank, machine.crank.main_crank.mesh.vertices),
                              (drum, machine.drum.main_axle_step_drum_top_1.step_drum_frame_top.mesh.vertices)):
            self.assertLess(np.max(np.abs(after - before @ rotation.T)), 0.00001)

    def test_selector_detent_travel(self):
        machine = self.node
        machine.set_state(digit=0)
        knob = machine.selector.selector_knob_1_419057.selector_knob
        before = knob.mesh.vertices.copy()
        machine.set_state(digit=9)
        self.assertLess(np.max(np.abs(knob.mesh.vertices - before - [0, 0, -54])), 0.00001)
