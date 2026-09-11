"""Reproducible inspection poses; snapshot uses declared driver defaults.

Keep these beside the model modules: nested SCAD output currently fails to
rebase flexible snapshot STL paths. See the project's framework findings.
"""

from solid_node.simulation import Driver
from solid_node.node import AssemblyNode
from simulation.carry_contact import CarryContactBench
from simulation.bell_spring import BellLeafContactBench
from simulation.mechanism import RegisterCarriage
from simulation.clearing_stop_spring import ClearingPinCarrier


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


def stationary(sources, targets):
    zeros = (0,) * len(targets)
    return lambda crank: zeros


class RegisterDetentView(RegisterCarriage):
    crank_turns = Driver(default=0, range=(0, 1), unit='rev')
    crank_turns.drives(RegisterCarriage.result_register.crank_turns)
    crank_turns.drives(RegisterCarriage.turns_register.crank_turns)
    crank_turns.drives(RegisterCarriage.result_register.operand, ratio=0, offset=1)
    crank_turns.drives(RegisterCarriage.turns_register.operand, ratio=0, offset=1)
    crank_turns.drives((RegisterCarriage.result_register.value,
                       RegisterCarriage.result_register.subtract,
                       RegisterCarriage.result_register.carriage_position,
                       RegisterCarriage.result_register.clear,
                       RegisterCarriage.turns_register.value,
                       RegisterCarriage.turns_register.subtract,
                       RegisterCarriage.turns_register.carriage_position,
                       RegisterCarriage.turns_register.clear,
                       RegisterCarriage.clearing_ring.turn), law=stationary)

    def render(self):
        super().render()
        self.covers.omit()
        self.carrier.omit()
        self.clearing_ring.omit()


class RegisterDetentMoving(RegisterDetentView):
    crank_turns = Driver(default=(113.5 + 11.25/2)/360, range=(0, 1), unit='rev')


class StopPinCutaway(ClearingPinCarrier):
    def render(self):
        super().render()
        self.counter_body.omit()
        self.clearing_stop_pin_sleeve.omit()
        self.counter_body_pin_1.omit()
        self.counter_body_pin_2.omit()
        self.counter_body_stop_pin.omit()
        for index in range(1, 18):
            getattr(self, f'digits_axle_{index}').omit()


class ClearingStopSeated(AssemblyNode):
    press = Driver(default=3.089172, range=(0, 8), unit='mm')
    carrier = StopPinCutaway()
    press.drives(carrier.press)


class ClearingStopDepressed(ClearingStopSeated):
    press = Driver(default=7.900085, range=(0, 8), unit='mm')
