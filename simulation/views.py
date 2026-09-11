"""Reproducible inspection poses; snapshot uses declared driver defaults.

Keep these beside the model modules: nested SCAD output currently fails to
rebase flexible snapshot STL paths. See the project's framework findings.
"""

from solid_node.simulation import Driver
from simulation.carry_contact import CarryContactBench
from simulation.bell_spring import BellLeafContactBench


class CarryPinDriving(CarryContactBench):
    enabled = Driver(default=1, range=(0, 1), dtype=int)
    crank_turns = Driver(default=.325, range=(0, 2), unit='rev')


class CarryReset(CarryContactBench):
    enabled = Driver(default=1, range=(0, 1), dtype=int)
    crank_turns = Driver(default=350/360, range=(0, 2), unit='rev')


class InstalledBellLeaf(BellLeafContactBench):
    def render(self):
        super().render()
        self.drum.omit()
        self.bell.omit()


class SubtractBellLeaf(InstalledBellLeaf):
    subtract = Driver(default=1, range=(0, 1))
