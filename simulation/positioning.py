"""The carriage lifts against a spring whose upper seat stays on the shaft."""

from solid_node.simulation import Driver
from solid_node.motion.joints import Prismatic
from solid_node.motion.ports import Port
from simulation.standard.layers import CarriagePositioning as SourcePositioning
from simulation.standard.parts import ThrustRing
from simulation.flexibles import MountedCarriageSpring
from math import cos, sin, radians


class CarriagePositioning(SourcePositioning):
    lift = Port(unit='mm')
    thrust_ring = ThrustRing(slide=Prismatic(axis=(0, 0, 1)))
    carriage_spring = MountedCarriageSpring(slide=Prismatic(axis=(0, 0, 1)))
    lift.drives(thrust_ring.slide)
    lift.drives(carriage_spring.slide)
    lift.drives(carriage_spring.height, ratio=-1, offset=24)

    def render(self):
        super().render()
        # Molejo's helix begins on its wire, not at the spring's central axis.
        phase = radians(35.717779468)
        self.carriage_spring.translate((13.2 * cos(phase), 13.2 * sin(phase), 0))


class PositioningBench(CarriagePositioning):
    travel = Driver(default=0, range=(0, 6), unit='mm')
    travel.drives(CarriagePositioning.lift)
