"""An inspectable Curta: calculator inputs above meaningful mechanical layers."""

from solid_node.simulation import Driver
from solid_node.motion.ports import Port
from simulation.arithmetic import calculate
from simulation.assemblies import LayeredSource
from simulation.mechanism import Inputs, MainDrive, Carriage


def registers(sources, targets):
    return calculate


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

    operand.drives(input_selectors.selectors.operand)
    crank_turns.drives(main_drive.turn, ratio=360)
    (initial_result & initial_turns & operand & crank_turns & subtract &
     carriage_position & clear).drives((result, turns_counter), law=registers)
