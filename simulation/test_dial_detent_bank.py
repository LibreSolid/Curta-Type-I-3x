"""Every source ball follows the correct dial and its own spider finger."""

from solid_node.test import TestCase
from simulation.dial_detent_bank import DialDetentBank

# Independent source occurrence map, ordered by decimal place.
RESULTS = (
    ('p_10203_1.results_dial_type_1', 12), ('p_10203_2.results_dial_type_1', 1),
    ('p_10205_1.results_dial_type_2', 13), ('p_10205_2.results_dial_type_2', 16),
    ('p_10204_1.results_dial_type_2', 11), ('p_10204_2.results_dial_type_2', 3),
    ('p_10204_3.results_dial_type_2', 7), ('p_10204_4.results_dial_type_2', 4),
    ('p_10204_5.results_dial_type_2', 17), ('p_10204_6.results_dial_type_2', 8),
    ('results_dial_type_2_1', 5),
)
TURNS = (
    ('p_10203_3.results_dial_type_1', 2), ('p_10203_4.results_dial_type_1', 14),
    ('p_10205_3.results_dial_type_2', 9), ('p_10205_4.results_dial_type_2', 10),
    ('p_10204_7.results_dial_type_2', 6), ('results_dial_type_2_2', 15),
)


def stations(root):
    carriage = root.carriage.registers
    detents = carriage.dial_detents
    for bank, records in (('result', RESULTS), ('turns', TURNS)):
        register = getattr(carriage, bank + '_register')
        for index, (path, ball_id) in enumerate(records, 1):
            dial = register
            for name in path.split('.'):
                dial = getattr(dial, name)
            ball = getattr(detents, f'p_6mm_ball_419241_{ball_id}')
            finger = getattr(detents.spider_spring, f'{bank}_{index}')
            yield f'{bank} {index}', dial, ball, finger


class DialDetentBankTest(TestCase):
    node = DialDetentBank

    def clear_bank(self, context):
        carriage = self.node.carriage.registers
        cover = carriage.clearing_ring.clearing_cover
        carrier = carriage.carrier.upper_carriage_body_1.counter_body
        for station, dial, ball, finger in stations(self.node):
            try:
                self.assertNotIntersecting(ball, dial)
                self.assertNotIntersecting(ball, carrier)
                for patch in (finger.arm, finger.tip):
                    for neighbour in (ball, cover, carrier):
                        self.assertNotIntersecting(patch, neighbour)
            except AssertionError as error:
                raise AssertionError(f'{context}, {station}: {error}') from error

    def test_all_integer_digits_at_all_carriage_positions(self):
        for shift in range(6):
            for digit in range(10):
                self.node.set_state(initial_result=digit*11111111111,
                                    initial_turns=digit*111111, operand=0, crank_turns=0,
                                    subtract=0, carriage_position=shift, carriage_lift=0, clear=0)
                self.clear_bank(f'shift={shift}, digit={digit}')

    def test_each_ball_is_captured_by_its_own_dial_and_finger(self):
        self.node.set_state(**self.node.instructions['Rest'].targets)
        for _, dial, ball, finger in stations(self.node):
            for neighbour in (dial, finger.tip):
                self.assertFreeWithin(ball, .01, against=neighbour, along=(0, 0, 1))
            self.assertBlockedBeyond(ball, .2, against=dial, along=(0, 0, 1), directions='forward')
            self.assertBlockedBeyond(ball, .2, against=finger.tip, along=(0, 0, -1), directions='forward')

    def test_carry_and_subtraction_cascades(self):
        for subtract in (0, 1):
            for angle in range(0, 361, 2):
                self.node.set_state(initial_result=0 if subtract else 99999999999,
                                    initial_turns=0 if subtract else 999999, operand=1,
                                    crank_turns=angle/360, subtract=subtract,
                                    carriage_position=0, carriage_lift=0, clear=0)
                self.clear_bank(f'subtract={subtract}, crank={angle}')

    def test_progressive_clearing(self):
        for step in range(101):
            self.node.set_state(initial_result=98765432109, initial_turns=987654,
                                operand=0, crank_turns=0, subtract=0,
                                carriage_position=0, carriage_lift=0, clear=step/100)
            self.clear_bank(f'clear={step/100}')
