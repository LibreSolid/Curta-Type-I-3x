"""Reproducible decimal register state for a prescribed crank operation."""

from solid_node.math import abs, clamp01, floor


def modulo(value, modulus):
    return value - modulus * floor(value / modulus)


def digit(value, place):
    return modulo(floor(value / 10 ** place), 10)


def decimal_shift(position):
    # One of the six detents; this also serializes as a viewer expression.
    return sum(10 ** place * (1 - clamp01(abs(position - place)))
               for place in range(6))


def calculate(initial_result, initial_turns, operand, turns, subtract=0, shift=0, clear=0):
    """Return settled registers; partial-turn dial motion is modeled separately.

    Inputs describe an operation from explicit starting registers. No hidden
    Python accumulator: revisiting a slider position gives the identical answer.
    Both decimal registers wrap exactly, including borrow below zero.
    """
    revolutions = floor(turns)
    direction = 1 - 2 * subtract
    scale = decimal_shift(shift)
    cleared = 1 - floor(clear)
    return (modulo(initial_result + direction * operand * scale * revolutions,
                   10 ** 11) * cleared,
            modulo(initial_turns + direction * scale * revolutions,
                   10 ** 6) * cleared)
