"""Printed groups from the standard STL assembly stages, using exact STEP ingredients.

Placements are transcribed from the untouched source map. Gear fitting is
explicit in fit.py; nothing is copied from the problematic grouped print STLs.
"""

from solid_node.node import FusionNode
from simulation.standard.parts import *
from simulation.fit import (FittedInputPinion, FittedCounterPinion, FittedInputSpacer, FittedOnesSpacer,
    FittedSlidingSpacer, FittedCounterSpacer, FittedOnesSleeve,
    FittedInputSleeve, FittedCounterSleeve, FittedCarryLockout, FittedCarryPinion)


class Part10230_410008_1_419032(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_5 = FittedInputPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((-20.25, -35.074028853, -64.92499975))
        self.p_1_6mm_spacer.translate((-20.25, -35.074028853, -70.92499975))
        self.p_2_5mm_lockout_sleeve.translate((-20.25, -35.074028853, -63.42499975))


class Part10220_410003_1_419039(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    pentagonal_lockout = FittedCarryLockout()
    transmission_gear_0_6 = FittedCarryPinion()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_1_9mm_spacer = Part1_9mmSpacer()

    def render(self):
        self.pentagonal_lockout.translate((-20.25, -35.074028853, -26.1))
        self.transmission_gear_0_6.translate((-20.25, -35.074028853, -33.6))
        self.p_4_8mm_tens_ratchet_sleeve.translate((-20.25, -35.074028853, -24.6))
        self.p_1_3mm_spacer.translate((-20.25, -35.074028853, -39.0))
        self.p_1_9mm_spacer.translate((-20.25, -35.074028853, -31.8))


class Part10220_410003_1_419064(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    pentagonal_lockout = FittedCarryLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()
    transmission_gear_0_6 = FittedCarryPinion()
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()

    def render(self):
        self.pentagonal_lockout.translate((-7.032751196, -39.884713997, -21.9))
        self.p_1_3mm_spacer.translate((-7.032751196, -39.884713997, -34.8))
        self.transmission_gear_0_6.translate((-7.032751196, -39.884713997, -29.4))
        self.p_1_9mm_spacer.translate((-7.032751196, -39.884713997, -27.6))
        self.p_4_8mm_tens_ratchet_sleeve.translate((-7.032751196, -39.884713997, -20.4))


class Part10230_410008_1_419066(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_6mm_spacer = FittedSlidingSpacer()
    transmission_gear_0_5 = FittedInputPinion()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()

    def render(self):
        self.p_1_6mm_spacer.translate((-7.032751196, -39.884713997, -70.92499975))
        self.transmission_gear_0_5.translate((-7.032751196, -39.884713997, -64.92499975))
        self.p_2_5mm_lockout_sleeve.translate((-7.032751196, -39.884713997, -63.42499975))


class Part10230_410008_1_419068(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_5 = FittedCounterPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((0.0, 40.5, -44.85))
        self.p_1_6mm_spacer.translate((0.0, 40.5, -50.85))
        self.p_2_5mm_lockout_sleeve.translate((0.0, 40.5, -43.35))


class Part10220_410003_1_419070(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_3mm_spacer = Part1_3mmSpacer()
    pentagonal_lockout = FittedCarryLockout()
    transmission_gear_0_6 = FittedCarryPinion()
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()

    def render(self):
        self.p_1_3mm_spacer.translate((0.0, 40.5, -21.9))
        self.pentagonal_lockout.translate((0.0, 40.5, -9.0))
        self.transmission_gear_0_6.translate((0.0, 40.5, -16.5))
        self.p_1_9mm_spacer.translate((0.0, 40.5, -14.7))
        self.p_4_8mm_tens_ratchet_sleeve.translate((0.0, 40.5, -7.5))


class Part10220_410003_1_419074(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    transmission_gear_0_6 = FittedCarryPinion()
    pentagonal_lockout = FittedCarryLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()

    def render(self):
        self.p_1_9mm_spacer.translate((-31.024799946, -26.032898192, -27.6))
        self.p_4_8mm_tens_ratchet_sleeve.translate((-31.024799946, -26.032898192, -20.4))
        self.transmission_gear_0_6.translate((-31.024799946, -26.032898192, -29.4))
        self.pentagonal_lockout.translate((-31.024799946, -26.032898192, -21.9))
        self.p_1_3mm_spacer.translate((-31.024799946, -26.032898192, -34.8))


class Part10230_410008_1_419075(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_2_5mm_lockout_sleeve = FittedInputSleeve()
    transmission_gear_0_5 = FittedInputPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((-31.024799946, -26.032898192, -63.42499975))
        self.transmission_gear_0_5.translate((-31.024799946, -26.032898192, -64.92499975))
        self.p_1_6mm_spacer.translate((-31.024799946, -26.032898192, -70.92499975))


class Part10230_410008_1_419080(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_2_5mm_lockout_sleeve = FittedInputSleeve()
    transmission_gear_0_5 = FittedCounterPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((-13.851815805, 38.057551142, -43.35))
        self.transmission_gear_0_5.translate((-13.851815805, 38.057551142, -44.85))
        self.p_1_6mm_spacer.translate((-13.851815805, 38.057551142, -50.85))


class Part10220_410003_1_419081(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_9mm_spacer = Part1_9mmSpacer()
    transmission_gear_0_6 = FittedCarryPinion()
    pentagonal_lockout = FittedCarryLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((-13.851815805, 38.057551142, -7.5))
        self.p_1_9mm_spacer.translate((-13.851815805, 38.057551142, -14.7))
        self.transmission_gear_0_6.translate((-13.851815805, 38.057551142, -16.5))
        self.pentagonal_lockout.translate((-13.851815805, 38.057551142, -9.0))
        self.p_1_3mm_spacer.translate((-13.851815805, 38.057551142, -21.9))


class Part10220_410003_1_419086(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    transmission_gear_0_6 = FittedCarryPinion()
    p_1_3mm_spacer = Part1_3mmSpacer()
    pentagonal_lockout = FittedCarryLockout()

    def render(self):
        self.p_1_9mm_spacer.translate((31.024799946, -26.032898192, -27.6))
        self.p_4_8mm_tens_ratchet_sleeve.translate((31.024799946, -26.032898192, -20.4))
        self.transmission_gear_0_6.translate((31.024799946, -26.032898192, -29.4))
        self.p_1_3mm_spacer.translate((31.024799946, -26.032898192, -34.8))
        self.pentagonal_lockout.translate((31.024799946, -26.032898192, -21.9))


class Part10230_410008_1_419088(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_2_5mm_lockout_sleeve = FittedInputSleeve()
    p_1_6mm_spacer = FittedSlidingSpacer()
    transmission_gear_0_5 = FittedInputPinion()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((31.024799946, -26.032898192, -63.42499975))
        self.p_1_6mm_spacer.translate((31.024799946, -26.032898192, -70.92499975))
        self.transmission_gear_0_5.translate((31.024799946, -26.032898192, -64.92499975))


class Part10230_410008_1_419092(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_5 = FittedInputPinion()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()
    p_1_6mm_spacer = FittedSlidingSpacer()

    def render(self):
        self.transmission_gear_0_5.translate((7.032751196, -39.884713997, -64.92499975))
        self.p_2_5mm_lockout_sleeve.translate((7.032751196, -39.884713997, -63.42499975))
        self.p_1_6mm_spacer.translate((7.032751196, -39.884713997, -70.92499975))


class Part10220_410003_1_419093(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_1_3mm_spacer = Part1_3mmSpacer()
    transmission_gear_0_6 = FittedCarryPinion()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    pentagonal_lockout = FittedCarryLockout()

    def render(self):
        self.p_1_9mm_spacer.translate((7.032751196, -39.884713997, -27.6))
        self.p_1_3mm_spacer.translate((7.032751196, -39.884713997, -34.8))
        self.transmission_gear_0_6.translate((7.032751196, -39.884713997, -29.4))
        self.p_4_8mm_tens_ratchet_sleeve.translate((7.032751196, -39.884713997, -20.4))
        self.pentagonal_lockout.translate((7.032751196, -39.884713997, -21.9))


class Part10230_410008_1_419105(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_5 = FittedCounterPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((26.032898192, 31.024799946, -44.85))
        self.p_1_6mm_spacer.translate((26.032898192, 31.024799946, -50.85))
        self.p_2_5mm_lockout_sleeve.translate((26.032898192, 31.024799946, -43.35))


class Part10220_410003_1_419107(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_6 = FittedCarryPinion()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    pentagonal_lockout = FittedCarryLockout()
    p_1_9mm_spacer = Part1_9mmSpacer()

    def render(self):
        self.transmission_gear_0_6.translate((26.032898192, 31.024799946, -16.5))
        self.p_1_3mm_spacer.translate((26.032898192, 31.024799946, -21.9))
        self.p_4_8mm_tens_ratchet_sleeve.translate((26.032898192, 31.024799946, -7.5))
        self.pentagonal_lockout.translate((26.032898192, 31.024799946, -9.0))
        self.p_1_9mm_spacer.translate((26.032898192, 31.024799946, -14.7))


class Part10230_410008_1_419111(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_5 = FittedInputPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((-38.057551142, 13.851815805, -65.1))
        self.p_1_6mm_spacer.translate((-38.057551142, 13.851815805, -71.1))
        self.p_2_5mm_lockout_sleeve.translate((-38.057551142, 13.851815805, -63.6))


class Part10220_410003_1_419114(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_9mm_spacer = Part1_9mmSpacer()
    transmission_gear_0_6 = FittedCarryPinion()
    p_1_3mm_spacer = Part1_3mmSpacer()
    pentagonal_lockout = FittedCarryLockout()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((-38.057551142, 13.851815805, -24.6))
        self.p_1_9mm_spacer.translate((-38.057551142, 13.851815805, -31.8))
        self.transmission_gear_0_6.translate((-38.057551142, 13.851815805, -33.6))
        self.p_1_3mm_spacer.translate((-38.057551142, 13.851815805, -39.0))
        self.pentagonal_lockout.translate((-38.057551142, 13.851815805, -26.1))


class Part10220_410003_1_419117(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_9mm_spacer = Part1_9mmSpacer()
    transmission_gear_0_6 = FittedCarryPinion()
    pentagonal_lockout = FittedCarryLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((-40.5, 0.0, -24.6))
        self.p_1_9mm_spacer.translate((-40.5, 0.0, -31.8))
        self.transmission_gear_0_6.translate((-40.5, 0.0, -33.6))
        self.pentagonal_lockout.translate((-40.5, 0.0, -26.1))
        self.p_1_3mm_spacer.translate((-40.5, 0.0, -39.0))


class Part10230_410008_1_419118(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_5 = FittedInputPinion()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()
    p_1_6mm_spacer = FittedSlidingSpacer()

    def render(self):
        self.transmission_gear_0_5.translate((-40.5, 0.0, -65.1))
        self.p_2_5mm_lockout_sleeve.translate((-40.5, 0.0, -63.6))
        self.p_1_6mm_spacer.translate((-40.5, 0.0, -71.1))


class Part10222_1(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_2_5mm_sleeve = Part2_5mmSleeve()
    pentagonal_lockout = FittedCarryLockout()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.p_2_5mm_sleeve.translate((-26.032898192, 31.024799946, -6.15))
        self.pentagonal_lockout.translate((-26.032898192, 31.024799946, -7.65))
        self.p_1_6mm_spacer.translate((-26.032898192, 31.024799946, -13.65))


class Part10218_1(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_5_8_sleeve = FittedCounterSleeve()
    transmission_gear_0_5_1 = FittedCounterPinion()
    p_1mm_spacer_1 = FittedCounterSpacer()
    transmission_gear_0_5_2 = FittedCounterPinion()
    p_1mm_spacer_2 = FittedCounterSpacer()
    p_1_8mm_spacer = FittedInputSpacer()
    transmission_gear_0_5_3 = FittedCounterPinion()

    def render(self):
        self.p_5_8_sleeve.translate((-26.032898192, 31.024799946, -38.85))
        self.transmission_gear_0_5_1.translate((-26.032898192, 31.024799946, -49.35))
        self.p_1mm_spacer_1.translate((-26.032898192, 31.024799946, -47.85))
        self.transmission_gear_0_5_2.translate((-26.032898192, 31.024799946, -40.35))
        self.p_1mm_spacer_2.translate((-26.032898192, 31.024799946, -43.35))
        self.p_1_8mm_spacer.translate((-26.032898192, 31.024799946, -55.95))
        self.transmission_gear_0_5_3.translate((-26.032898192, 31.024799946, -44.85))


class Part10219_410002_1(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_8mm_spacer = FittedInputSpacer()
    p_4_7mm_ones_sleeve = FittedOnesSleeve()
    p_1_5mm_spacer = FittedOnesSpacer()
    transmission_gear_0_5_1 = FittedInputPinion()
    transmission_gear_0_5_2 = FittedInputPinion()

    def render(self):
        self.p_1_8mm_spacer.translate((40.5, 0.0, -71.52499975))
        self.p_4_7mm_ones_sleeve.translate((40.5, 0.0, -57.42499975))
        self.p_1_5mm_spacer.translate((40.5, 0.0, -63.42499975))
        self.transmission_gear_0_5_1.translate((40.5, 0.0, -64.92499975))
        self.transmission_gear_0_5_2.translate((40.5, 0.0, -58.92499975))


class Part10221_1(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    pentagonal_lockout = FittedCarryLockout()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((40.5, 0.0, -21.15))
        self.pentagonal_lockout.translate((40.5, 0.0, -22.65))
        self.p_1_6mm_spacer.translate((40.5, 0.0, -28.65))


class Part10230_410008_1_419137(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_5 = FittedInputPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((-38.057551142, -13.851815805, -65.1))
        self.p_1_6mm_spacer.translate((-38.057551142, -13.851815805, -71.1))
        self.p_2_5mm_lockout_sleeve.translate((-38.057551142, -13.851815805, -63.6))


class Part10220_410003_1_419139(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_9mm_spacer = Part1_9mmSpacer()
    transmission_gear_0_6 = FittedCarryPinion()
    p_1_3mm_spacer = Part1_3mmSpacer()
    pentagonal_lockout = FittedCarryLockout()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((-38.057551142, -13.851815805, -24.6))
        self.p_1_9mm_spacer.translate((-38.057551142, -13.851815805, -31.8))
        self.transmission_gear_0_6.translate((-38.057551142, -13.851815805, -33.6))
        self.p_1_3mm_spacer.translate((-38.057551142, -13.851815805, -39.0))
        self.pentagonal_lockout.translate((-38.057551142, -13.851815805, -26.1))


class TensBell1(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    results_locking_disc = ResultsLockingDisc()
    tens_turns_counter_locking_disc = TensTurnsCounterLockingDisc()
    tens_bell_body = TensBellBody()
    tens_results_locking_disc = TensResultsLockingDisc()
    turns_counter_carry_ring = TurnsCounterCarryRing()
    tens_bell_spacer_2_1 = TensBellSpacer2()
    tens_bell_support_plate = TensBellSupportPlate()
    tens_bell_spacer_2_2 = TensBellSpacer2()
    tens_bell_spacer_1 = TensBellSpacer1()
    turns_counter_locking_disc = TurnsCounterLockingDisc()
    results_counter_carry_ring = ResultsCounterCarryRing()

    def render(self):
        self.results_locking_disc.translate((0.0, 0.0, -23.1))
        self.tens_turns_counter_locking_disc.translate((0.0, 0.0, -10.8))
        self.tens_bell_body.translate((0.0, 0.0, -6.9))
        self.tens_results_locking_disc.translate((0.0, 0.0, -25.5))
        self.turns_counter_carry_ring.rotate(-103.0, (0.0, 0.0, 1.0))
        self.turns_counter_carry_ring.translate((0.0, 0.0, -18.3))
        self.tens_bell_spacer_2_1.rotate(77.0, (0.0, 0.0, 1.0))
        self.tens_bell_spacer_2_1.translate((0.0, 0.0, -31.5))
        self.tens_bell_support_plate.translate((0.0, 0.0, -33.0))
        self.tens_bell_spacer_2_2.rotate(-103.0, (0.0, 0.0, 1.0))
        self.tens_bell_spacer_2_2.translate((0.0, 0.0, -16.8))
        self.tens_bell_spacer_1.rotate(-13.0, (0.0, 0.0, 1.0))
        self.tens_bell_spacer_1.translate((0.0, 0.0, -21.6))
        self.turns_counter_locking_disc.translate((0.0, 0.0, -8.4))
        self.results_counter_carry_ring.rotate(77.0, (0.0, 0.0, 1.0))
        self.results_counter_carry_ring.translate((0.0, 0.0, -33.0))


class Part10220_410003_1_419181(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_6 = FittedCarryPinion()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    pentagonal_lockout = FittedCarryLockout()

    def render(self):
        self.transmission_gear_0_6.translate((13.851815805, 38.057551142, -16.5))
        self.p_1_3mm_spacer.translate((13.851815805, 38.057551142, -21.9))
        self.p_1_9mm_spacer.translate((13.851815805, 38.057551142, -14.7))
        self.p_4_8mm_tens_ratchet_sleeve.translate((13.851815805, 38.057551142, -7.5))
        self.pentagonal_lockout.translate((13.851815805, 38.057551142, -9.0))


class Part10230_410008_1_419182(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_2_5mm_lockout_sleeve = FittedInputSleeve()
    transmission_gear_0_5 = FittedCounterPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((13.851815805, 38.057551142, -43.35))
        self.transmission_gear_0_5.translate((13.851815805, 38.057551142, -44.85))
        self.p_1_6mm_spacer.translate((13.851815805, 38.057551142, -50.85))


class MainAxleStepDrumTop1(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    one_tooth_turns_step_drum_segment_1 = OneToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_2 = OneToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_3 = OneToothTurnsStepDrumSegment()
    nine_tooth_turns_step_drum_segment = NineToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_4 = OneToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_5 = OneToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_6 = OneToothTurnsStepDrumSegment()
    step_drum_frame_top = StepDrumFrameTop()

    def render(self):
        self.one_tooth_turns_step_drum_segment_1.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_1.translate((-0.016356142, 0.223394941, -51.2))
        self.one_tooth_turns_step_drum_segment_2.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_2.translate((-0.016356142, 0.223394941, -45.2))
        self.one_tooth_turns_step_drum_segment_3.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_3.translate((-0.016356142, 0.223394941, -46.7))
        self.nine_tooth_turns_step_drum_segment.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.nine_tooth_turns_step_drum_segment.translate((-0.016356142, 0.223394941, -49.7))
        self.one_tooth_turns_step_drum_segment_4.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_4.translate((-0.016356142, 0.223394941, -52.7))
        self.one_tooth_turns_step_drum_segment_5.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_5.translate((-0.016356142, 0.223394941, -54.2))
        self.one_tooth_turns_step_drum_segment_6.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_6.translate((-0.016356142, 0.223394941, -48.2))
        self.step_drum_frame_top.rotate(-89.895917198, (0.0, 0.0, 1.0))
        self.step_drum_frame_top.translate((-0.009541016, 0.073549841, -66.3))


class MainAxleStepDrumBottom1(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    eight_tooth_step_drum_segment_1 = EightToothStepDrumSegment()
    two_tooth_step_drum_segment_1 = TwoToothStepDrumSegment()
    step_drum_termination_segment = StepDrumTerminationSegment()
    four_tooth_step_drum_segment_1 = FourToothStepDrumSegment()
    three_tooth_step_drum_segment_1 = ThreeToothStepDrumSegment()
    six_tooth_step_drum_segment_1 = SixToothStepDrumSegment()
    two_tooth_step_drum_segment_2 = TwoToothStepDrumSegment()
    five_tooth_step_drum_segment_1 = FiveToothStepDrumSegment()
    four_tooth_step_drum_segment_2 = FourToothStepDrumSegment()
    four_tooth_step_drum_segment_3 = FourToothStepDrumSegment()
    one_tooth_step_drum_segment_1 = OneToothStepDrumSegment()
    two_tooth_step_drum_segment_3 = TwoToothStepDrumSegment()
    five_tooth_step_drum_segment_2 = FiveToothStepDrumSegment()
    five_tooth_step_drum_segment_3 = FiveToothStepDrumSegment()
    four_tooth_step_drum_segment_4 = FourToothStepDrumSegment()
    two_tooth_step_drum_segment_4 = TwoToothStepDrumSegment()
    three_tooth_step_drum_segment_2 = ThreeToothStepDrumSegment()
    nine_tooth_step_drum_segment_1 = NineToothStepDrumSegment()
    two_tooth_step_drum_segment_5 = TwoToothStepDrumSegment()
    three_tooth_step_drum_segment_3 = ThreeToothStepDrumSegment()
    one_tooth_step_drum_segment_2 = OneToothStepDrumSegment()
    ten_tooth_step_drum_segment = TenToothStepDrumSegment()
    five_tooth_step_drum_segment_4 = FiveToothStepDrumSegment()
    two_tooth_step_drum_segment_6 = TwoToothStepDrumSegment()
    seven_tooth_step_drum_segment_1 = SevenToothStepDrumSegment()
    one_tooth_step_drum_segment_3 = OneToothStepDrumSegment()
    one_tooth_step_drum_segment_4 = OneToothStepDrumSegment()
    step_drum_frame_bottom = StepDrumFrameBottom()
    nine_tooth_step_drum_segment_2 = NineToothStepDrumSegment()
    eight_tooth_step_drum_segment_2 = EightToothStepDrumSegment()
    three_tooth_step_drum_segment_4 = ThreeToothStepDrumSegment()
    five_tooth_step_drum_segment_5 = FiveToothStepDrumSegment()
    seven_tooth_step_drum_segment_2 = SevenToothStepDrumSegment()
    one_tooth_step_drum_segment_5 = OneToothStepDrumSegment()
    three_tooth_step_drum_segment_5 = ThreeToothStepDrumSegment()
    three_tooth_step_drum_segment_6 = ThreeToothStepDrumSegment()
    four_tooth_step_drum_segment_5 = FourToothStepDrumSegment()
    four_tooth_step_drum_segment_6 = FourToothStepDrumSegment()
    six_tooth_step_drum_segment_2 = SixToothStepDrumSegment()
    one_tooth_step_drum_segment_6 = OneToothStepDrumSegment()

    def render(self):
        self.eight_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.eight_tooth_step_drum_segment_1.translate((0.0, 0.0, -79.8))
        self.two_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_1.translate((0.0, 0.0, -78.3))
        self.step_drum_termination_segment.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.step_drum_termination_segment.translate((0.0, 0.0, -124.8))
        self.four_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_1.translate((0.0, 0.0, -102.3))
        self.three_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_1.translate((0.0, 0.0, -81.3))
        self.six_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.six_tooth_step_drum_segment_1.translate((0.0, 0.0, -91.8))
        self.two_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_2.translate((0.0, 0.0, -115.8))
        self.five_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_1.translate((0.0, 0.0, -99.3))
        self.four_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_2.translate((0.0, 0.0, -87.3))
        self.four_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_3.translate((0.0, 0.0, -105.3))
        self.one_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_1.translate((0.0, 0.0, -73.8))
        self.two_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_3.translate((0.0, 0.0, -75.3))
        self.five_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_2.translate((0.0, 0.0, -94.8))
        self.five_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_3.translate((0.0, 0.0, -93.3))
        self.four_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_4.translate((0.0, 0.0, -90.3))
        self.two_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_4.translate((0.0, 0.0, -114.3))
        self.three_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_2.translate((0.0, 0.0, -109.8))
        self.nine_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.nine_tooth_step_drum_segment_1.translate((0.0, 0.0, -118.8))
        self.two_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_5.translate((0.0, 0.0, -117.3))
        self.three_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_3.translate((0.0, 0.0, -108.3))
        self.one_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_2.translate((0.0, 0.0, -120.3))
        self.ten_tooth_step_drum_segment.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.ten_tooth_step_drum_segment.translate((0.0, 0.0, -67.8))
        self.five_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_4.translate((0.0, 0.0, -96.3))
        self.two_tooth_step_drum_segment_6.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_6.translate((0.0, 0.0, -76.8))
        self.seven_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.seven_tooth_step_drum_segment_1.translate((0.0, 0.0, -106.8))
        self.one_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_3.translate((0.0, 0.0, -72.3))
        self.one_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_4.translate((0.0, 0.0, -70.8))
        self.step_drum_frame_bottom.rotate(-89.895917198, (0.0, 0.0, 1.0))
        self.step_drum_frame_bottom.translate((0.0, 0.0, -66.3))
        self.nine_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.nine_tooth_step_drum_segment_2.translate((0.0, 0.0, -73.8))
        self.eight_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.eight_tooth_step_drum_segment_2.translate((0.0, 0.0, -112.8))
        self.three_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_4.translate((0.0, 0.0, -84.3))
        self.five_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_5.translate((0.0, 0.0, -97.8))
        self.seven_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.seven_tooth_step_drum_segment_2.translate((0.0, 0.0, -85.8))
        self.one_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_5.translate((0.0, 0.0, -69.3))
        self.three_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_5.translate((0.0, 0.0, -82.8))
        self.three_tooth_step_drum_segment_6.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_6.translate((0.0, 0.0, -111.3))
        self.four_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_5.translate((0.0, 0.0, -88.8))
        self.four_tooth_step_drum_segment_6.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_6.translate((0.0, 0.0, -103.8))
        self.six_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.six_tooth_step_drum_segment_2.translate((0.0, 0.0, -100.8))
        self.one_tooth_step_drum_segment_6.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_6.translate((0.0, 0.0, -121.8))


class Part10220_410003_1_419227(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    transmission_gear_0_6 = FittedCarryPinion()
    pentagonal_lockout = FittedCarryLockout()
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()

    def render(self):
        self.transmission_gear_0_6.translate((38.137315415, -13.851815805, -33.6))
        self.pentagonal_lockout.translate((38.137315415, -13.851815805, -26.1))
        self.p_1_9mm_spacer.translate((38.137315415, -13.851815805, -31.8))
        self.p_1_3mm_spacer.translate((38.137315415, -13.851815805, -39.0))
        self.p_4_8mm_tens_ratchet_sleeve.translate((38.137315415, -13.851815805, -24.6))


class Part10230_410008_1_419229(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_6mm_spacer = FittedSlidingSpacer()
    transmission_gear_0_5 = FittedInputPinion()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()

    def render(self):
        self.p_1_6mm_spacer.translate((38.137315415, -13.851815805, -70.92499975))
        self.transmission_gear_0_5.translate((38.137315415, -13.851815805, -64.92499975))
        self.p_2_5mm_lockout_sleeve.translate((38.137315415, -13.851815805, -63.42499975))


class Part10230_410008_1_419232(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_2_5mm_lockout_sleeve = FittedInputSleeve()
    transmission_gear_0_5 = FittedInputPinion()
    p_1_6mm_spacer = FittedSlidingSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((20.25, -35.074028853, -63.42499975))
        self.transmission_gear_0_5.translate((20.25, -35.074028853, -64.92499975))
        self.p_1_6mm_spacer.translate((20.25, -35.074028853, -70.92499975))


class Part10220_410003_1_419234(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    transmission_gear_0_6 = FittedCarryPinion()
    pentagonal_lockout = FittedCarryLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_1_9mm_spacer = Part1_9mmSpacer()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((20.25, -35.074028853, -20.4))
        self.transmission_gear_0_6.translate((20.25, -35.074028853, -29.4))
        self.pentagonal_lockout.translate((20.25, -35.074028853, -21.9))
        self.p_1_3mm_spacer.translate((20.25, -35.074028853, -34.8))
        self.p_1_9mm_spacer.translate((20.25, -35.074028853, -27.6))


class Part10230_410008_1_419237(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_6mm_spacer = FittedSlidingSpacer()
    transmission_gear_0_5 = FittedCounterPinion()
    p_2_5mm_lockout_sleeve = FittedInputSleeve()

    def render(self):
        self.p_1_6mm_spacer.translate((35.074028853, 20.25, -50.85))
        self.transmission_gear_0_5.translate((35.074028853, 20.25, -44.85))
        self.p_2_5mm_lockout_sleeve.translate((35.074028853, 20.25, -43.35))


class Part10220_410003_1_419238(FusionNode):
    color = '#d3d5cb'
    angular_deflection = 0.5
    p_1_9mm_spacer = Part1_9mmSpacer()
    pentagonal_lockout = FittedCarryLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()
    transmission_gear_0_6 = FittedCarryPinion()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()

    def render(self):
        self.p_1_9mm_spacer.translate((35.074028853, 20.25, -14.7))
        self.pentagonal_lockout.translate((35.074028853, 20.25, -9.0))
        self.p_1_3mm_spacer.translate((35.074028853, 20.25, -21.9))
        self.transmission_gear_0_6.translate((35.074028853, 20.25, -16.5))
        self.p_4_8mm_tens_ratchet_sleeve.translate((35.074028853, 20.25, -7.5))
