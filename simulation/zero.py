"""The retained zero cam, its following lever, and the sliding drive pin."""

from solid_node.node import AssemblyNode
from solid_node.motion.joints import Revolute, Prismatic
from solid_node.motion.ports import Port
from solid_node.simulation import Driver
from solid_node.math import piecewise
from simulation.arithmetic import modulo
from simulation.flexibles import MountedZeroSpring, FIXED_PIN, ZERO_PIVOT
from simulation.standard.parts import (
    M5Nut, M5x15HexBolt, M5x30HexBolt, ZeroPositioningDisc,
    ZeroPositioningDiscPin, ZeroPositioningDiscRoller, ZeroPositioningLever,
    ZeroPositioningM5BoltSleeve, DiscRollerBoltSleeve,
    ZeroPositioningDiscSecuringSpring,
)
from simulation.standard.layers import LowerBearingPlate

# Native cam against a 10.4 mm roller gauge (10.35 mm roller + .05 mm gap).
# tools/zero_profile.py measures the two edges; the circular flank is a dwell.
CAM = (
    (0, 0), (1, .00569), (2, 1.28577), (3, 2.41396), (4, 3.40455),
    (5, 4.26905), (6, 5.01671), (7, 5.65535), (8, 6.19156),
    (9, 6.63088), (10, 6.97807), (11, 7.23733), (12, 7.41205),
    (13, 7.50515), (14, 7.52303), (339, 7.52303), (340, 7.49182),
    (341, 7.38423), (342, 7.20089), (343, 6.94192), (344, 6.60697),
    (345, 6.19467), (346, 5.70265), (347, 5.12723), (348, 4.48934),
    (349, 3.87267), (350, 3.28357), (351, 2.72172), (352, 2.18671),
    (353, 1.67825), (354, 1.19594), (355, .73938), (356, .30822),
    (357, 0), (360, 0),
)


def follower_angle(source, target):
    return lambda turn: piecewise(modulo(-turn, 360), CAM)


class ZeroCam(ZeroPositioningDisc):
    """Resolve the .05 mm roller seat; the source B-rep is unchanged."""
    linear_deflection = .01
    angular_deflection = .1


class ZeroRoller(ZeroPositioningDiscRoller):
    linear_deflection = .01
    angular_deflection = .1


class ZeroFollower(AssemblyNode):
    zero_positioning_disc_roller = ZeroRoller()
    zero_positioning_lever = ZeroPositioningLever()
    disc_roller_bolt_sleeve = DiscRollerBoltSleeve()
    m5_nut_2 = M5Nut()
    m5x15_hex_bolt_1 = M5x15HexBolt()

    def render(self):
        self.zero_positioning_disc_roller.translate((40.5, 0, -153.1))
        self.zero_positioning_lever.rotate(-90, (0, 0, 1)).translate((40.5, 33.6, -156.3))
        self.disc_roller_bolt_sleeve.rotate(-90, (0, 0, 1)).translate((40.5, 0, -153.3))
        self.m5_nut_2.rotate(-90, (0, 0, 1)).translate((40.5, 0, -160.5))
        self.m5x15_hex_bolt_1.rotate(-90, (0, 0, 1)).translate((40.5, 0, -161.4))


class ZeroPositioning(AssemblyNode):
    turn = Port(unit='deg')
    subtract = Port()
    zero_positioning_disc = ZeroCam(turn=Revolute(axis=(0, 0, 1)))
    zero_positioning_disc_pin = ZeroPositioningDiscPin(
        turn=Revolute(axis=(0, 0, 1)), lift=Prismatic(axis=(0, 0, 1)))
    follower = ZeroFollower(turn=Revolute(axis=(0, 0, 1), at=(*ZERO_PIVOT, 0)))
    documented_spring = MountedZeroSpring()
    m5_nut_1 = M5Nut()
    zero_positioning_m5_bolt_sleeve = ZeroPositioningM5BoltSleeve()
    m5x30_hex_bolt = M5x30HexBolt()
    zero_positioning_disc_securing_spring = ZeroPositioningDiscSecuringSpring()

    turn.drives(zero_positioning_disc.turn)
    turn.drives(zero_positioning_disc_pin.turn)
    subtract.drives(zero_positioning_disc_pin.lift, ratio=9)
    turn.drives(follower.turn, law=follower_angle)
    follower.turn.drives(documented_spring.deflection)

    def render(self):
        self.zero_positioning_disc.rotate(-180, (.70774875, -.706464229, 0))
        self.zero_positioning_disc.translate((0, 0, -138.45))
        self.zero_positioning_disc_pin.rotate(-179.92640235, (.707106635, .000642261, .707106635))
        self.zero_positioning_disc_pin.translate((-14.99997525, -.027248799, -165.75))
        self.m5_nut_1.rotate(180, (1, 0, 0)).translate((40.5, 33.6, -128.25))
        self.zero_positioning_m5_bolt_sleeve.rotate(-90, (0, 0, 1))
        self.zero_positioning_m5_bolt_sleeve.translate((40.5, 33.6, -161.85))
        self.m5x30_hex_bolt.rotate(180, (0, 1, 0)).translate((40.5, 33.6, -128.25))
        self.zero_positioning_disc_securing_spring.rotate(180, (.999999588, .000908294, 0))
        self.zero_positioning_disc_securing_spring.translate((.029065386, -15.9999736, -142.2))
        self.documented_spring.translate(FIXED_PIN)


class ZeroCamBench(AssemblyNode):
    crank_turns = Driver(default=0, range=(0, 1), unit='rev')
    subtract = Driver(default=0, range=(0, 1), dtype=int)
    mechanism = ZeroPositioning()
    bearing_plate = LowerBearingPlate()
    crank_turns.drives(mechanism.turn, ratio=-360)
    subtract.drives(mechanism.subtract)
