"""Keyed transmission shafts: selector travel and the two-to-one dial drive."""

from solid_node.node import AssemblyNode
from solid_node.motion.ports import Port
from solid_node.simulation import Driver
from solid_node.math import abs, clamp01, floor
from simulation.arithmetic import digit, modulo, decimal_shift
from simulation.cycle import dial_positions, added_digits, carries
from simulation.carry_motion import engagement
from simulation.fit import INPUT_CLOCKING
import simulation.standard.channels as channels


class TransmissionBench(channels.ResultOnes):
    digit = Driver(default=0, range=(0, 9), dtype=int)
    advance = Driver(default=0, range=(0, 10))
    digit.drives(channels.ResultOnes.setting)
    advance.drives(channels.ResultOnes.turn, ratio=72, offset=INPUT_CLOCKING)
    advance.drives(channels.ResultOnes.carry, ratio=0)


def shifted(values, channel, shift):
    """Select the dial over a fixed shaft at one of the six carriage detents."""
    return sum(value * (1 - clamp01(abs(place - channel - shift)))
               for place, value in enumerate(values))


def channel_values(places, counter=False):
    def factory(sources, targets):
        def pose(value, operand, crank_turns, subtract, shift, carriage_lift=0):
            wheels = dial_positions(value, operand, crank_turns, subtract, shift, 0, places, counter)
            increments = added_digits(operand, subtract, shift, places, counter)
            transfer = carries(value, increments)
            previous_value = modulo(value - (1 - 2 * subtract) *
                                    (1 if counter else operand) * decimal_shift(shift), 10 ** places)
            previous_transfer = carries(previous_value, increments)
            completed = clamp01(floor(crank_turns))
            angle = 360 * modulo(crank_turns, 1)
            result = []
            for channel in range(places):
                clocking = (130 if counter else 0) - 20 * channel
                turn = clocking + INPUT_CLOCKING + 72 * shifted(wheels, channel, shift)
                # The normal counter setting is 4.5 mm above the source pose:
                # its first channel meets one tooth; all higher channels are blank.
                setting = -.75 if counter else digit(operand, channel) if channel < 8 else 0
                enabled = shifted(transfer, channel, shift)
                previous = completed * shifted(previous_transfer, channel, shift)
                engaged = engagement(shifted(wheels, channel - 1, shift), enabled,
                                     previous, angle, channel, counter,
                                     carriage_lift) if channel else 0
                result.extend((turn, setting, engaged))
            return tuple(result)
        return pose
    return factory


class RegisterDrive(AssemblyNode):
    value = Port()
    operand = Port()
    crank_turns = Port(unit='rev')
    subtract = Port()
    carriage_position = Port()
    carriage_lift = Port(unit='mm')


class ResultDrive(RegisterDrive):
    ones = channels.ResultOnes()
    tens = channels.ResultTens()
    hundreds = channels.ResultHundreds()
    digit_4 = channels.ResultDigit4()
    digit_5 = channels.ResultDigit5()
    digit_6 = channels.ResultDigit6()
    digit_7 = channels.ResultDigit7()
    digit_8 = channels.ResultDigit8()
    digit_9 = channels.ResultDigit9()
    digit_10 = channels.ResultDigit10()
    digit_11 = channels.ResultDigit11()

    (RegisterDrive.value & RegisterDrive.operand & RegisterDrive.crank_turns &
     RegisterDrive.subtract & RegisterDrive.carriage_position & RegisterDrive.carriage_lift).drives((
        ones.turn, ones.setting, ones.carry,
        tens.turn, tens.setting, tens.carry,
        hundreds.turn, hundreds.setting, hundreds.carry,
        digit_4.turn, digit_4.setting, digit_4.carry,
        digit_5.turn, digit_5.setting, digit_5.carry,
        digit_6.turn, digit_6.setting, digit_6.carry,
        digit_7.turn, digit_7.setting, digit_7.carry,
        digit_8.turn, digit_8.setting, digit_8.carry,
        digit_9.turn, digit_9.setting, digit_9.carry,
        digit_10.turn, digit_10.setting, digit_10.carry,
        digit_11.turn, digit_11.setting, digit_11.carry,
    ), law=channel_values(11))


class TurnsDrive(RegisterDrive):
    ones = channels.TurnsOnes()
    tens = channels.TurnsTens()
    hundreds = channels.TurnsHundreds()
    digit_4 = channels.TurnsDigit4()
    digit_5 = channels.TurnsDigit5()
    digit_6 = channels.TurnsDigit6()

    (RegisterDrive.value & RegisterDrive.operand & RegisterDrive.crank_turns &
     RegisterDrive.subtract & RegisterDrive.carriage_position & RegisterDrive.carriage_lift).drives((
        ones.turn, ones.setting, ones.carry,
        tens.turn, tens.setting, tens.carry,
        hundreds.turn, hundreds.setting, hundreds.carry,
        digit_4.turn, digit_4.setting, digit_4.carry,
        digit_5.turn, digit_5.setting, digit_5.carry,
        digit_6.turn, digit_6.setting, digit_6.carry,
    ), law=channel_values(6, counter=True))


class Transmission(AssemblyNode):
    result = ResultDrive()
    turns = TurnsDrive()
