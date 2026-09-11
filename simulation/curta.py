"""An inspectable Curta: calculator inputs above meaningful mechanical layers."""

from solid_node.simulation import Driver
from solid_node.motion.ports import Port
from simulation.arithmetic import calculate
from simulation.assemblies import LayeredSource
from simulation.mechanism import Inputs, MainDrive, Carriage, CarryMechanism
from simulation.transmission import Transmission


def registers(sources, targets):
    return calculate


def operation(sources, targets):
    return lambda *values: values


class Curta(LayeredSource):
    """Source geometry, one documented spring correction, and prescribed motion."""

    operand = Driver(default=0, range=(0, 99999999), dtype=int)
    crank_turns = Driver(default=0, range=(0, 12), unit='rev')
    initial_result = Driver(default=0, range=(0, 99999999999), dtype=int)
    initial_turns = Driver(default=0, range=(0, 999999), dtype=int)
    subtract = Driver(default=0, range=(0, 1), dtype=int)
    carriage_position = Driver(default=0, range=(0, 5), dtype=int)
    clear = Driver(default=0, range=(0, 1))
    result = Port()
    turns_counter = Port()

    input_selectors = Inputs()
    main_drive = MainDrive()
    carriage = Carriage()
    carry_mechanism = CarryMechanism()
    transmission = Transmission()

    operand.drives(input_selectors.selectors.operand)
    crank_turns.drives(main_drive.turn, ratio=-360)
    subtract.drives(main_drive.subtract)
    (initial_result & initial_turns & operand & crank_turns & subtract &
     carriage_position & clear).drives((result, turns_counter), law=registers)
    result.drives(carriage.registers.result_register.value)
    turns_counter.drives(carriage.registers.turns_register.value)
    result.drives(transmission.result.value)
    turns_counter.drives(transmission.turns.value)
    (operand & crank_turns & subtract & carriage_position).drives((
        transmission.result.operand, transmission.result.crank_turns,
        transmission.result.subtract, transmission.result.carriage_position,
    ), law=operation)
    (operand & crank_turns & subtract & carriage_position).drives((
        transmission.turns.operand, transmission.turns.crank_turns,
        transmission.turns.subtract, transmission.turns.carriage_position,
    ), law=operation)
    (operand & crank_turns & subtract & carriage_position & clear).drives((
        carriage.registers.result_register.operand,
        carriage.registers.result_register.crank_turns,
        carriage.registers.result_register.subtract,
        carriage.registers.result_register.carriage_position,
        carriage.registers.result_register.clear,
    ), law=operation)
    (operand & crank_turns & subtract & carriage_position & clear).drives((
        carriage.registers.turns_register.operand,
        carriage.registers.turns_register.crank_turns,
        carriage.registers.turns_register.subtract,
        carriage.registers.turns_register.carriage_position,
        carriage.registers.turns_register.clear,
    ), law=operation)
