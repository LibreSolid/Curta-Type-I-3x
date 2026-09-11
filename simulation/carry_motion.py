"""Dial-pin approach, over-centre latch, and the next passing reset cam.

The pin and cam profiles are measured clearances. The short snap between
detents is prescribed motion, not a spring-force or impact simulation.
"""

from solid_node.math import abs, clamp01, piecewise
from simulation.arithmetic import modulo
from simulation.carry_profiles import PIN_DROP, RESET_LIFT

STROKE = 4.2


def maximum(first, second):
    return (first + second + abs(first - second)) / 2


def engagement(position, enabled, previous, angle, channel,
               counter=False, carriage_lift=0):
    """A fixed carry shaft is tripped by the dial immediately before it."""
    approach = maximum(0, piecewise(modulo(position, 10), PIN_DROP) - carriage_lift) / STROKE
    trip = clamp01((position - 9.3) / .1)

    offset = (50 if counter else 0) + 20 * (channel - 1)
    next_cycle = 343 + offset >= 360
    phase = angle - offset + (360 if next_cycle else 0)
    lift = piecewise(phase, RESET_LIFT)
    # The measured spring-spread crest is near 61% of the downward stroke.
    # The cam crosses it after 1.65 mm of lift; then the upper detent snaps in.
    snap = clamp01((lift - 1.65) / .2)
    reset = (lift + (STROKE - lift) * snap) / STROKE
    latched = (previous * (1 - reset) + enabled * trip if next_cycle
               else enabled * trip * (1 - reset))
    return maximum(approach, latched)
