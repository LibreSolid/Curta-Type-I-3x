"""The spring-loaded pawl rides the disc's anti-reversal ratchet."""

from solid_node.node import AssemblyNode
from solid_node.simulation import Driver
from solid_node.motion.joints import Revolute
from solid_node.motion.ports import Port
from solid_node.math import piecewise, clamp01, floor
from simulation.arithmetic import modulo
from simulation.standard.parts import ZeroPositioningDisc, ReverseRotationPreventionPawl
from simulation.standard.layers import AntiReversal as SourceAntiReversal
from simulation.standard.layers import LowerBearingPlate
from simulation.fit import FittedPawl, FittedBearingPlate, PAWL_PIVOT, PAWL_SPRING_ANCHOR
from simulation.pawl_spring import MountedPawlSpring

PIVOT = PAWL_PIVOT
TOOTH_PITCH = 357 / 116
RELEASE = .31
CLOSING_RELEASE = RELEASE + 97 * TOOTH_PITCH + 3
# Measured .05 mm planar gauge, conservatively interpolated along the ramp.
# The spring's quick release is prescribed, not a dynamic impact calculation.
RAMP = ((0, 1.006), (.69, 1.627), (1.19, 2.082), (1.69, 2.541),
        (2.19, 3.004), (2.69, 3.472), (TOOTH_PITCH, 3.837))


def pawl_angle(source, target):
    def angle(turn):
        crank = modulo(-turn, 360)
        closing = (TOOTH_PITCH - 3) * clamp01(floor(crank / CLOSING_RELEASE))
        return piecewise(modulo(crank + closing - RELEASE, TOOTH_PITCH), RAMP)
    return angle


class AntiReversal(SourceAntiReversal):
    turn = Port(unit='deg')
    reverse_rotation_prevention_pawl = FittedPawl(
        turn=Revolute(axis=(0, 0, 1), at=PIVOT))
    documented_spring = MountedPawlSpring()
    turn.drives(reverse_rotation_prevention_pawl.turn, law=pawl_angle)
    reverse_rotation_prevention_pawl.turn.drives(documented_spring.deflection)

    def render(self):
        super().render()
        self.anti_reversal_spring.omit()
        self.documented_spring.translate(PAWL_SPRING_ANCHOR)


class PawlBearingPlate(LowerBearingPlate):
    bearing_plate = FittedBearingPlate()


class PawlBench(AssemblyNode):
    crank_turns = Driver(default=0, range=(0, 1), unit='rev')
    disc = ZeroPositioningDisc(turn=Revolute(axis=(0, 0, 1)))
    pawl = AntiReversal()
    bearing_plate = PawlBearingPlate()
    crank_turns.drives(disc.turn, ratio=-360)
    disc.turn.drives(pawl.turn)

    def render(self):
        self.disc.rotate(-180, (.70774875, -.706464229, 0))
        self.disc.translate((0, 0, -138.45))
