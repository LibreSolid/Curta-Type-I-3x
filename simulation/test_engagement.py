"""Use the complete printed drum, not an isolated tooth or arithmetic proxy."""

from solid_node.test import TestCase
from simulation.engagement import Engagement


class EngagementTest(TestCase):
    node = Engagement

    def test_every_selected_row(self):
        pinion = self.node.result.p_10219_410002_1
        drum = self.node.drum.main_axle_step_drum_bottom_1
        for subtract in (0, 1):
            for digit in range(10):
                for angle in range(0, 361, 3):
                    self.node.set_state(digit=digit, subtract=subtract, crank_turns=angle/360)
                    try:
                        self.assertNotIntersecting(drum, pinion)
                    except AssertionError as error:
                        raise AssertionError(f'digit={digit}, subtract={subtract}, crank={angle}: {error}') from error

    def test_counter_addition_and_complement(self):
        pinion = self.node.counter.p_10218_1
        drum = self.node.drum.main_axle_step_drum_top_1
        for subtract in (0, 1):
            for angle in range(0, 361, 3):
                self.node.set_state(digit=0, subtract=subtract, crank_turns=angle/360)
                try:
                    self.assertNotIntersecting(drum, pinion)
                except AssertionError as error:
                    raise AssertionError(f'counter, subtract={subtract}, crank={angle}: {error}') from error
