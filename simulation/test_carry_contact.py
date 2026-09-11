"""A carry must be physically trippable, transferable and resettable."""

from solid_node.test import TestCase
from simulation.carry_contact import CarryContactBench
from simulation.tools.interference import rigid_leaves


class CarryContactTest(TestCase):
    node = CarryContactBench

    def clear_pair(self, first, second, enabled, angle):
        try:
            self.assertNotIntersecting(first, second)
        except AssertionError as error:
            raise AssertionError(f'carry={enabled}, crank={angle}: {error}') from error

    def pairs(self):
        return (
            (self.node.results_lever.tens_slider_for_results,
             self.node.results_dials.p_10203_1.number_roll_carry_pin_half,
             self.node.result),
            (self.node.turns_lever.tens_slider_for_turns_counter,
             self.node.turns_dials.p_10203_3.number_roll_carry_pin_half,
             self.node.counter),
        )

    def test_dial_pins_clear_the_sliders_during_a_carry(self):
        for enabled in (0, 1):
            for angle in range(721):
                self.node.set_state(enabled=enabled, crank_turns=angle/360)
                for slider, pin, _ in self.pairs():
                    self.clear_pair(slider, pin, enabled, angle)

    def test_reset_bell_clears_both_sliders(self):
        for enabled in (0, 1):
            for angle in range(721):
                self.node.set_state(enabled=enabled, crank_turns=angle/360)
                for slider, _, _ in self.pairs():
                    self.clear_pair(slider, self.node.bell, enabled, angle)

    def test_forks_clear_their_keyed_shaft_stacks(self):
        for enabled in (0, 1):
            for angle in range(721):
                self.node.set_state(enabled=enabled, crank_turns=angle/360)
                for slider, _, shaft in self.pairs():
                    for _, part in rigid_leaves(shaft):
                        self.clear_pair(slider, part, enabled, angle)

    def test_forks_capture_the_flanged_gears_with_axial_play(self):
        self.node.set_state(enabled=0, crank_turns=0)
        for slider, shaft in (
            (self.node.results_lever.tens_slider_for_results,
             self.node.result.p_10220_410003_1_419227),
            (self.node.turns_lever.tens_slider_for_turns_counter,
             self.node.counter.p_10220_410003_1_419081),
        ):
            self.assertFreeWithin(slider, .01, against=shaft, along=(1, 0, 0))
            self.assertBlockedBeyond(slider, .2, against=shaft, along=(1, 0, 0))

    def test_the_dial_pins_drive_the_approaching_levers(self):
        for angle, bank in ((117, 0), (168.25, 1)):
            self.node.set_state(enabled=1, crank_turns=angle/360)
            slider, pin, _ = self.pairs()[bank]
            self.assertFreeWithin(slider, .01, against=pin, along=(1, 0, 0))
            self.assertBlockedBeyond(slider, .2, against=pin, along=(1, 0, 0), directions='forward')
            self.assertFreeWithin(slider, .2, against=pin, along=(-1, 0, 0), directions='forward')

    def test_the_reset_cam_drives_both_banks_in_their_actual_cycles(self):
        for angle, bank in ((350, 0), (400, 1)):
            self.node.set_state(enabled=1, crank_turns=angle/360)
            slider, _, _ = self.pairs()[bank]
            self.assertFreeWithin(slider, .01, against=self.node.bell, along=(1, 0, 0))
            self.assertBlockedBeyond(slider, .2, against=self.node.bell,
                                     along=(-1, 0, 0), directions='forward')
            self.assertFreeWithin(slider, .2, against=self.node.bell,
                                  along=(1, 0, 0), directions='forward')
