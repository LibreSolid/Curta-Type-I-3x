"""Motion belongs to the mechanism that the navigation tree exposes."""

from solid_node.motion.joints import Revolute
from solid_node.motion.ports import Port
from simulation.assemblies import Inputs as SourceInputs, MainDrive as SourceDrive
from simulation.assemblies import RegisterCarriage as SourceRegisters, Carriage as SourceCarriage
from simulation.flexibles import FIXED_PIN, ZeroSpring
from simulation.selectors import Selectors
from simulation.print_parts import DigitsCover, UpperHousing, CrankCollar
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


class MainDrive(SourceDrive):
    turn = Port(unit='deg')
    crank = layers.CrankAssembly(turn=Revolute(axis=(0, 0, 1)))
    stepped_drum = layers.DrumAssembly(turn=Revolute(axis=(0, 0, 1)))
    zero_positioning = ZeroPositioning()

    turn.drives(crank.turn)
    crank.turn.drives(stepped_drum.turn)


class CarriageCovers(layers.CarriageCovers):
    digits_cover = DigitsCover()
    upper_housing = UpperHousing()


class CarriageStructure(layers.CarriageStructure):
    crank_collar = CrankCollar()


class RegisterCarriage(SourceRegisters):
    covers = CarriageCovers()
    carrier = CarriageStructure()


class Carriage(SourceCarriage):
    registers = RegisterCarriage()
