"""A digit detent follows its dial and deflects its spring finger."""

from solid_node.test import TestCase
from simulation.dial_detents import DialDetentBench


class DialDetentTest(TestCase):
    node = DialDetentBench

    def rest(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)

    def test_first_ball_clears_its_dial_at_zero(self):
        self.rest()
        ball = self.node.carriage.registers.dial_detents.p_6mm_ball_419241_12
        dial = self.node.carriage.registers.result_register.p_10203_1.results_dial_type_1
        self.assertNotIntersecting(ball, dial)

    def test_spider_finger_is_deflected_above_its_ball(self):
        self.rest()
        detents = self.node.carriage.registers.dial_detents
        finger = detents.spider_spring.result_1
        for patch in (finger.arm, finger.tip):
            self.assertNotIntersecting(detents.p_6mm_ball_419241_12, patch)

    def test_first_ball_rises_between_digit_detents(self):
        self.rest()
        ball = self.node.carriage.registers.dial_detents.p_6mm_ball_419241_12
        before = ball.mesh.vertices[:, 2].mean()
        self.node.set_state(operand=1, crank_turns=(124.75 - 11.25/2)/360)
        self.assertGreater(ball.mesh.vertices[:, 2].mean(), before)

    def test_first_finger_and_ball_clear_through_a_whole_digit_pitch(self):
        self.rest()
        carriage = self.node.carriage.registers
        ball = carriage.dial_detents.p_6mm_ball_419241_12
        dial = carriage.result_register.p_10203_1.results_dial_type_1
        finger = carriage.dial_detents.spider_spring.result_1
        cover = carriage.clearing_ring.clearing_cover
        carrier = carriage.carrier.upper_carriage_body_1.counter_body
        for step in range(73):
            self.node.set_state(operand=1, crank_turns=(113.5 + 11.25*step/72)/360)
            self.assertNotIntersecting(ball, dial)
            for patch in (finger.arm, finger.tip):
                for neighbour in (ball, cover, carrier):
                    self.assertNotIntersecting(patch, neighbour)

    def test_ball_is_seated_between_dial_and_finger(self):
        self.rest()
        carriage = self.node.carriage.registers
        ball = carriage.dial_detents.p_6mm_ball_419241_12
        dial = carriage.result_register.p_10203_1.results_dial_type_1
        tip = carriage.dial_detents.spider_spring.result_1.tip
        for neighbour in (dial, tip):
            self.assertFreeWithin(ball, .01, against=neighbour, along=(0, 0, 1))
        # The source sphere is placed upside down: its local +Z is world -Z.
        self.assertBlockedBeyond(ball, .2, against=dial, along=(0, 0, 1), directions='forward')
        self.assertBlockedBeyond(ball, .2, against=tip, along=(0, 0, -1), directions='forward')
