"""The first register's measured five-to-ten-tooth bevel drive."""

from solid_node.node import AssemblyNode
from solid_node.motion.joints import Revolute
from solid_node.simulation import Driver
from solid_node.parameters import Length
from simulation.standard.assembly import Part10208_1, Part10203_1


class PinionShaft(Part10208_1):
    """Seat the bonded tip 0.8 mm below its nominal STEP position.

    The source bevel pair intersects at every phase. The measured 0.8 mm axial
    adjustment clears a complete tooth period; the engagement contract checks
    that the teeth still transmit motion. Source geometry is unchanged.
    """
    seating_drop = Length(0.8, min=0)

    def render(self):
        super().render()
        self.transmission_gear_tip.translate((0, 0, -self.seating_drop))


class BevelPair(AssemblyNode):
    pinion_angle = Driver(default=0, range=(0, 72), unit='deg')
    shaft = PinionShaft(turn=Revolute(axis=(0, 0, 1), at=(40.5, 0, 0)))
    dial = Part10203_1(turn=Revolute(
        axis=(-0.9999539408943618, -0.009597712739783826, 0),
        at=(72.008486542, 0.647810225, 33.9)))

    pinion_angle.drives(shaft.turn)
    shaft.turn.drives(dial.turn, ratio=-0.5, offset=3)
