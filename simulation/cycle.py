"""Prescribed decimal-wheel motion within one clockwise crank revolution."""

from math import degrees
from solid_node.math import abs, clamp01, floor, max
from simulation.arithmetic import digit, decimal_shift, modulo

TOOTH_PITCH = 11.25
RESULT_INPUT_END = 124.75
TURNS_INPUT_END = 176.0
# Full-bell flank probes center the first carried shaft at crank 152°/204°.
# Channel one is 20° after the bank datum; half a tooth passage follows center.
RESULT_CARRY_END = 137.625
TURNS_CARRY_END = 189.625


def cleared_position(position, clear, place, counter=False):
    """The two nine-tooth racks reset each dial only when they reach it.

    Pitch is the source strip's 3.75 mm spacing at its neutral radius. The
    measured first engagement fixes the phase; lifting and lowering do not
    turn the rack. The missing-tooth gap leaves a zero dial undisturbed.
    """
    # Shaft banks call this with a literal zero: clearing lifts the dials off
    # their bevel tips, so the shafts have no clearing expression to publish.
    if isinstance(clear, (int, float)) and clear == 0:
        return position
    outer = place < 2
    station = (130 if counter else 0) - 20 * place
    datum = 0 if outer else -40
    start = (9.75 if outer else 10.5) + (datum - station) % 360
    pitch = degrees(3.75 / (52 if outer else 49.55))
    remaining = modulo(-position, 10)
    denominator = max(1, remaining)
    angle = 360 * clamp01((clear - .1) / .8)
    return position + remaining * clamp01((angle - start) / (pitch * denominator))


def tooth_passage(angle, count, end):
    """A tooth train advances at 72 / 11.25; a zero row remains stationary."""
    denominator = max(1, count)
    return count * clamp01((angle - end + TOOTH_PITCH * count) /
                           (TOOTH_PITCH * denominator))


def added_digits(operand, subtract, shift, places, counter=False):
    shifted = (1 if counter else operand) * decimal_shift(shift)
    result = []
    for place in range(places):
        entered = digit(shifted, place)
        active = clamp01(place - shift + 1)
        first = 1 - clamp01(abs(place - shift))
        complement = active * (9 - entered) + first
        result.append((1 - subtract) * entered + subtract * complement)
    return tuple(result)


def carries(value, increments):
    return tuple(floor((modulo(value, 10 ** place) +
                        sum(increments[index] * 10 ** index for index in range(place))) /
                       10 ** place) for place in range(len(increments)))


def dial_positions(value, operand, crank_turns, subtract, shift, clear, places, counter=False):
    """Unwrapped digit positions; a ten-digit advance is a full wheel turn.

    `value` is the register after already completed crank turns, not hidden
    accumulated state. Subtraction adds decimal complements, as the Curta does.
    Phase constants prescribe kinematics; they are not a force/contact solver.
    """
    angle = 360 * modulo(crank_turns, 1)
    increments = added_digits(operand, subtract, shift, places, counter)
    transfer = carries(value, increments)
    input_end = TURNS_INPUT_END if counter else RESULT_INPUT_END
    carry_end = TURNS_CARRY_END if counter else RESULT_CARRY_END
    result = []
    for place in range(places):
        channel = place - shift
        direct = tooth_passage(angle, increments[place], input_end + 20 * channel)
        carry = tooth_passage(angle, transfer[place], carry_end + 20 * channel)
        position = digit(value, place) + direct + carry
        result.append(cleared_position(position, clear, place, counter))
    return tuple(result)
