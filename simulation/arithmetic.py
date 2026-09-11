"""Reproducible decimal register state for a prescribed crank operation."""

from solid_node.math import floor


def modulo(value, modulus):
    return value - modulus * floor(value / modulus)


def digit(value, place):
    return modulo(floor(value / 10 ** place), 10)


def decimal_shift(position):
    # Same linear interpolation between the six detents, without six copied
    # branches in every downstream digit expression. Working detents are exact.
    lower = floor(position)
    return 10 ** lower * (1 + 9 * (position - lower))


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
