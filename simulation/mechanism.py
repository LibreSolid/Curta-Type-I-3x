"""Motion belongs to the mechanism that the navigation tree exposes."""

from solid_node.motion.joints import Revolute, Prismatic
from solid_node.motion.ports import Port
from simulation.assemblies import Inputs as SourceInputs, MainDrive as SourceDrive
from simulation.assemblies import RegisterCarriage as SourceRegisters, Carriage as SourceCarriage
from simulation.assemblies import CarryMechanism as SourceCarry
from simulation.flexibles import FIXED_PIN, ZeroSpring
from simulation.selectors import Selectors
from simulation.print_parts import DigitsCover, UpperHousing, CrankCollar
from simulation.registers import ResultRegister, TurnsRegister
from simulation.fit import CARRIAGE_CENTER, CARRIAGE_CLOCKING
from simulation.prints import PrintedDrum
from simulation.standard.printed import TensBell1
import simulation.standard.layers as layers


class Inputs(SourceInputs):
    selectors = Selectors()


class ZeroPositioning(layers.ZeroPositioning):
    """The documented fitted spring replaces source product #419219 only."""

    documented_spring = ZeroSpring()

    def render(self):
        super().render()
        self.zero_positioning_spring.omit()
        self.documented_spring.translate(FIXED_PIN)


class SteppedDrum(layers.DrumAssembly):
    main_axle_step_drum_1 = PrintedDrum()


class MainDrive(SourceDrive):
    turn = Port(unit='deg')
    subtract = Port()
    crank = layers.CrankAssembly(turn=Revolute(axis=(0, 0, 1)),
                                 lift=Prismatic(axis=(0, 0, 1)))
    stepped_drum = SteppedDrum(turn=Revolute(axis=(0, 0, 1)),
                               lift=Prismatic(axis=(0, 0, 1)))
    zero_positioning = ZeroPositioning()

    turn.drives(crank.turn)
    crank.turn.drives(stepped_drum.turn)
    # One and a half 6 mm selector pitches puts the complementary rows in mesh.
    subtract.drives(crank.lift, ratio=9)
    crank.lift.drives(stepped_drum.lift)


class TensBellAssembly(layers.TensBellAssembly):
    tens_bell_1 = TensBell1()


class CarryMechanism(SourceCarry):
    tens_bell = TensBellAssembly()


class CarriageCovers(layers.CarriageCovers):
    digits_cover = DigitsCover()
    upper_housing = UpperHousing()


class CarriageStructure(layers.CarriageStructure):
    crank_collar = CrankCollar()

    def render(self):
        super().render()
        self.upper_carriage_body_1.translate(tuple(-value for value in CARRIAGE_CENTER))
        self.upper_carriage_body_1.rotate(-CARRIAGE_CLOCKING, (0, 0, 1))


class RegisterCarriage(SourceRegisters):
    covers = CarriageCovers()
    carrier = CarriageStructure()
    result_register = ResultRegister()
    turns_register = TurnsRegister()

    def render(self):
        self.dial_detents.translate(tuple(-value for value in CARRIAGE_CENTER))
        self.dial_detents.rotate(-CARRIAGE_CLOCKING, (0, 0, 1))


class Carriage(SourceCarriage):
    registers = RegisterCarriage()
