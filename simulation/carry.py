"""The carry slider drops to engage and rises when the bell resets it."""

from solid_node.simulation import Driver
from simulation.standard.carry import ResultsLever1, TurnsLever1


class CarryBench(ResultsLever1):
    engaged = Driver(default=0, range=(0, 1))
    engaged.drives(ResultsLever1.engage)


class TurnsCarryBench(TurnsLever1):
    engaged = Driver(default=0, range=(0, 1))
    engaged.drives(TurnsLever1.engage)
