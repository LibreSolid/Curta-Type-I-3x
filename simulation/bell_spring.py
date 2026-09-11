"""Inspection bench for the tens bell's forked retaining leaf spring."""

from simulation.curta import Curta
from solid_node.node import AssemblyNode
from solid_node.simulation import Driver
from solid_node.motion.joints import Prismatic
from simulation.retaining_spring import RetainingSpring, MOUNT_Z
from simulation.prints import PrintedDrum
from simulation.standard.printed import TensBell1
from simulation.bell_spring_motion import positioning


class BellSpringBench(Curta):
    pass


class BellLeafFitBench(AssemblyNode):
    spread = Driver(default=0, range=(0, 8), unit='mm')
    subtract = Driver(default=0, range=(0, 1))
    spring = RetainingSpring()
    drum = PrintedDrum(lift=Prismatic(axis=(0, 0, 1)))
    bell = TensBell1()
    spread.drives(spring.spread)
    subtract.drives(drum.lift, ratio=9)

    def render(self):
        self.spring.translate((0, 0, MOUNT_Z))


class BellLeafContactBench(AssemblyNode):
    subtract = Driver(default=0, range=(0, 1))
    spring = RetainingSpring()
    drum = PrintedDrum(lift=Prismatic(axis=(0, 0, 1)))
    bell = TensBell1()
    subtract.drives(spring.spread, law=positioning)
    subtract.drives(drum.lift, ratio=9)

    def render(self):
        self.spring.translate((0, 0, MOUNT_Z))
