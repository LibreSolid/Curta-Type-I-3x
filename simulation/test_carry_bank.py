"""First-pair calibration must also hold at every installed carry station."""

from solid_node.test import TestCase
from simulation.carry_bank import CarryBank
from simulation.carry_heads import ResultsSlider, TurnsSlider
from simulation.standard.parts import NumberRollCarryPinHalf, NumberRollCarryPinFull
from simulation.tools.interference import rigid_leaves, world_solids


class CarryBankTest(TestCase):
    node = CarryBank

    def parts(self):
        parts = list(rigid_leaves(self.node))
        sliders = [(path, part) for path, part in parts
                   if isinstance(part, (ResultsSlider, TurnsSlider))]
        pins = [(path, part) for path, part in parts
                if isinstance(part, (NumberRollCarryPinHalf, NumberRollCarryPinFull))]
        self.assertEqual(len(sliders), 15)
        self.assertEqual(len(pins), 15)
        return sliders, pins

    def pins_clear(self, sliders, pins, context):
        for slider_path, slider in sliders:
            for pin_path, pin in pins:
                try:
                    self.assertNotIntersecting(slider, pin)
                except AssertionError as error:
                    raise AssertionError(f'{context}: {slider_path} / {pin_path}: {error}') from error

    def test_every_pin_clears_through_a_two_turn_carry_cascade(self):
        sliders, pins = self.parts()
        for angle in range(0, 721, 2):
            self.node.set_state(initial_result=99999999999, initial_turns=999999,
                                operand=1, crank_turns=angle/360, subtract=0,
                                carriage_position=0, carriage_lift=0, clear=0)
            self.pins_clear(sliders, pins, f'crank={angle}')

    def test_all_digits_clear_at_every_carriage_detent_and_lifted_transit(self):
        sliders, pins = self.parts()
        for shift in range(6):
            for digit in range(10):
                self.node.set_state(initial_result=digit*11111111111,
                                    initial_turns=digit*111111, operand=0,
                                    crank_turns=0, subtract=0, carriage_position=shift,
                                    carriage_lift=0, clear=0)
                self.pins_clear(sliders, pins, f'shift={shift}, digit={digit}')
        for shift in (.5, 1.5, 2.5, 3.5, 4.5):
            self.node.set_state(carriage_lift=1, carriage_position=shift)
            self.pins_clear(sliders, pins, f'lifted shift={shift}')

    def test_cascades_at_every_shift_leave_the_other_banks_parked_pins_clear(self):
        sliders, pins = self.parts()
        for shift in range(1, 6):
            lower_digits = 7 * ((10**shift-1)//9)  # parked twos below the selected place
            for angle in range(0, 721, 3):
                self.node.set_state(initial_result=99999999999-lower_digits,
                                    initial_turns=999999-lower_digits, operand=1,
                                    crank_turns=angle/360, subtract=0, carriage_position=shift,
                                    carriage_lift=0, clear=0)
                self.pins_clear(sliders, pins, f'shift={shift}, crank={angle}')

    def test_all_eight_half_pin_flats_match_the_manual(self):
        import numpy as np
        from math import asin, degrees
        self.node.set_state(initial_result=0, initial_turns=0, operand=0,
                            crank_turns=0, subtract=0, carriage_position=0,
                            carriage_lift=0, clear=0)
        _, pins = self.parts()
        half = {path for path, pin in pins if isinstance(pin, NumberRollCarryPinHalf)}
        self.assertEqual(len(half), 8)
        for path, shape in world_solids(self.node, selected=half).items():
            flat = max((face for face in shape.Faces() if face.geomType() == 'PLANE'),
                       key=lambda face: face.Area())
            # The cylindrical cap at the mounting end supplies the pin axis;
            # its normal is radial to the machine, independent of clocking.
            cap = max((face for face in shape.Faces() if face.geomType() == 'PLANE'
                       and face.Area() < 5), key=lambda face: face.Area())
            normal = np.array(cap.normalAt().toTuple())
            center = np.array(flat.Center().toTuple())
            radial = np.array((normal[0], normal[1], 0))
            radial /= np.linalg.norm(radial)
            offset = center - (0, 0, 33.9)
            offset -= radial * np.dot(offset, radial)
            cosine = abs(np.dot(flat.normalAt().toTuple(), offset) / np.linalg.norm(offset))
            self.assertAlmostEqual(degrees(asin(cosine)), 36, places=5, msg=path)
