"""A carry must be physically trippable, transferable and resettable."""

from solid_node.test import TestCase
from simulation.carry_contact import CarryContactBench
from simulation.tools.interference import rigid_leaves


class CarryContactTest(TestCase):
    node = CarryContactBench

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
            for angle in range(361):
                self.node.set_state(enabled=enabled, crank_turns=angle/360)
                for slider, pin, _ in self.pairs():
                    self.assertNotIntersecting(slider, pin)

    def test_reset_bell_clears_both_sliders(self):
        for enabled in (0, 1):
            for angle in range(361):
                self.node.set_state(enabled=enabled, crank_turns=angle/360)
                for slider, _, _ in self.pairs():
                    self.assertNotIntersecting(slider, self.node.bell)

    def test_forks_clear_their_keyed_shaft_stacks(self):
        for enabled in (0, 1):
            for angle in range(361):
                self.node.set_state(enabled=enabled, crank_turns=angle/360)
                for slider, _, shaft in self.pairs():
                    for _, part in rigid_leaves(shaft):
                        self.assertNotIntersecting(slider, part)
