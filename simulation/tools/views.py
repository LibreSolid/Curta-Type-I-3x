"""Reproducible inspection poses; snapshot uses declared driver defaults."""

from solid_node.simulation import Driver
from simulation.carry_contact import CarryContactBench


class CarryPinDriving(CarryContactBench):
    enabled = Driver(default=1, range=(0, 1), dtype=int)
    crank_turns = Driver(default=.325, range=(0, 2), unit='rev')


class CarryReset(CarryContactBench):
    enabled = Driver(default=1, range=(0, 1), dtype=int)
    crank_turns = Driver(default=350/360, range=(0, 2), unit='rev')
