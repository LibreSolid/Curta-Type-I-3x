"""An inspectable Curta: calculator inputs above meaningful mechanical layers."""

from solid_node.simulation import Driver, Instruction
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
    carriage_position = Driver(default=0, range=(0, 5))
    carriage_lift = Driver(default=0, range=(0, 1))
    clear = Driver(default=0, range=(0, 1))
    result = Port()
    turns_counter = Port()

    instructions = {
        'Rest': Instruction(dict(operand=0, crank_turns=0, initial_result=0,
                                 initial_turns=0, subtract=0, carriage_position=0,
                                 carriage_lift=0, clear=0), duration=1),
        'Set one': Instruction({'operand': 1}, duration=1),
        'Turn crank': Instruction({'crank_turns': 1}, duration=6),
        'Lift carriage': Instruction({'carriage_lift': 1}, duration=1),
        'Shift ×10': Instruction({'carriage_position': 1}, duration=1),
        'Seat carriage': Instruction({'carriage_lift': 0}, duration=1),
        'Clear both': Instruction({'clear': 1}, duration=3),
    }

    input_selectors = Inputs()
    main_drive = MainDrive()
    carriage = Carriage()
    carry_mechanism = CarryMechanism()
    transmission = Transmission()

    operand.drives(input_selectors.selectors.operand)
    crank_turns.drives(main_drive.turn, ratio=-360)
    subtract.drives(main_drive.subtract)
    crank_turns.drives(carry_mechanism.tens_bell.turn, ratio=-360)
    carriage_position.drives(carriage.position)
    carriage_lift.drives(carriage.lift)
    clear.drives(carriage.clear)
    transmission.result.tens.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_1.engage)
    transmission.result.hundreds.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_2.engage)
    transmission.result.digit_4.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_3.engage)
    transmission.result.digit_5.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_4.engage)
    transmission.result.digit_6.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_5.engage)
    transmission.result.digit_7.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_6.engage)
    transmission.result.digit_8.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_7.engage)
    transmission.result.digit_9.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_8.engage)
    transmission.result.digit_10.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_9.engage)
    transmission.result.digit_11.carry.drives(carry_mechanism.result_carries.results_tens_lever_assembly_10.engage)
    transmission.turns.tens.carry.drives(carry_mechanism.turns_carries.turns_tens_lever_assembly_1.engage)
    transmission.turns.hundreds.carry.drives(carry_mechanism.turns_carries.turns_tens_lever_assembly_2.engage)
    transmission.turns.digit_4.carry.drives(carry_mechanism.turns_carries.turns_tens_lever_assembly_3.engage)
    transmission.turns.digit_5.carry.drives(carry_mechanism.turns_carries.turns_tens_lever_assembly_4.engage)
    transmission.turns.digit_6.carry.drives(carry_mechanism.turns_carries.turns_tens_lever_assembly_5.engage)
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
