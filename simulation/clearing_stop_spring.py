"""The source stop pin compresses its documented .6 mm wire spring.

Manual page 40 specifies a .6 × 5 × 20 mm spring. Native sections give eight
turns at R 2.55, with 21 mm free centerline height. The sleeve and pin shoulder
set the installed length; this is a contact-driven shape, not a force model.
"""

from simulation.colors import STEEL
from molejo import Circle, Shape, Helix, P
from solid_node.node import AssemblyNode, MolejoNode
from solid_node.motion.ports import Port
from solid_node.motion.joints import Prismatic
from simulation.standard.assembly import UpperCarriageBody1
from simulation.standard.parts import ClearingPin

WIRE_RADIUS = .3
COIL_RADIUS = 2.55
SEAT_GAP = .05
# Native sleeve seat 27.0 and unpressed pin shoulder 44.4, minus wire/gaps.
HEIGHT = 44.4 - 27 - 2*(WIRE_RADIUS + SEAT_GAP)


class ClearingSpringWire(MolejoNode):
    height = Port(unit='mm')
    color = STEEL

    def render(self):
        return Shape(profile=Circle(WIRE_RADIUS),
                     path=[Helix(radius=COIL_RADIUS, turns=8, height=P.height)],
                     path_samples=512, profile_samples=24)


class MountedClearingSpring(AssemblyNode):
    height = Port(unit='mm')
    wire = ClearingSpringWire()
    height.drives(wire.height)

    def render(self):
        # Helix starts on its wire; the source mounting frame starts on its axis.
        self.wire.translate((COIL_RADIUS, 0, 0))


class ClearingPinCarrier(UpperCarriageBody1):
    press = Port(unit='mm')
    clearing_pin = ClearingPin(slide=Prismatic(axis=(0, 0, -1)))
    clearing_pin_spring = MountedClearingSpring(slide=Prismatic(axis=(0, 0, -1)))
    press.drives(clearing_pin.slide)
    press.drives(clearing_pin_spring.slide)
    press.drives(clearing_pin_spring.height, ratio=-1, offset=HEIGHT)

    def render(self):
        super().render()
        # Source spring points downward from Z 48; place its top wire below
        # the pin shoulder at 44.4. Compression keeps the lower seat fixed.
        self.clearing_pin_spring.translate((0, 0, 44.4 - WIRE_RADIUS - SEAT_GAP - 48))
