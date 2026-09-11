"""Check the installed parts; an isolated first-pair bench cannot prove a bank."""

import numpy as np
from solid_node.test import TestCase
from simulation.bevel_bank import BevelBank
from simulation.fit import FittedBevelTip
from simulation.standard.parts import ResultsDialType1, ResultsDialType2
from simulation.tools.interference import rigid_leaves


class BevelBankTest(TestCase):
    node = BevelBank

    def parts(self):
        parts = list(rigid_leaves(self.node))
        tips = [part for _, part in parts if isinstance(part, FittedBevelTip)]
        dials = [part for _, part in parts if isinstance(part, (ResultsDialType1, ResultsDialType2))]
        self.assertEqual(len(tips), 17)
        self.assertEqual(len(dials), 17)
        return tips, dials

    def test_every_installed_bevel_pair_transmits_motion(self):
        self.node.set_state(initial_result=0, initial_turns=0, operand=0,
                            crank_turns=0, carriage_position=0, carriage_lift=0, clear=0)
        tips, dials = self.parts()
        for tip in tips:
            dial = min(dials, key=lambda part: np.linalg.norm(part.mesh.centroid[:2] - tip.mesh.centroid[:2]))
            self.assertFreeWithin(tip, .1, against=dial)
            self.assertBlockedBeyond(tip, 12, against=dial)

    def test_bank_clearance_at_every_shift_and_during_lifted_travel(self):
        tips, dials = self.parts()
        for shift in range(6):
            for lift, turn in [(0, 0), (0, .37), (1, 0)]:
                self.node.set_state(initial_result=12345678901, initial_turns=123456,
                                    operand=87654321, crank_turns=turn, subtract=1,
                                    carriage_position=shift, carriage_lift=lift, clear=0)
                for tip in tips:
                    for dial in dials:
                        self.assertNotIntersecting(tip, dial)
        for shift in (.5, 1.5, 2.5, 3.5, 4.5):
            self.node.set_state(crank_turns=0, carriage_lift=1, carriage_position=shift)
            for tip in tips:
                for dial in dials:
                    self.assertNotIntersecting(tip, dial)
