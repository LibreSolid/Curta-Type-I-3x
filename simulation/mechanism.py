"""Motion belongs to the mechanism that the navigation tree exposes."""

from solid_node.motion.joints import Revolute, Prismatic
from solid_node.motion.ports import Port
from solid_node.math import clamp01, abs
from simulation.assemblies import Inputs as SourceInputs, MainDrive as SourceDrive, Frame as SourceFrame
from simulation.assemblies import RegisterCarriage as SourceRegisters, Carriage as SourceCarriage
from simulation.assemblies import CarryMechanism as SourceCarry
from simulation.zero import ZeroPositioning
from simulation.selectors import Selectors
from simulation.print_parts import DigitsCover, UpperHousing, CrankCollar
from simulation.registers import ResultRegister, TurnsRegister
from simulation.fit import CARRIAGE_CENTER, CARRIAGE_CLOCKING
from simulation.prints import PrintedDrum
from simulation.standard.printed import TensBell1
from simulation.clearing import ClearingGrooveCover, ClearingTeethStack
from simulation.standard.carry import ResultsCarry, TurnsCarry
from simulation.positioning import CarriagePositioning
from simulation.pawl import AntiReversal, PawlBearingPlate
import simulation.standard.layers as layers


class Inputs(SourceInputs):
    selectors = Selectors()


class Frame(SourceFrame):
    lower_bearing_plate = PawlBearingPlate()


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
    anti_reversal = AntiReversal()

    turn.drives(crank.turn)
    crank.turn.drives(stepped_drum.turn)
    # One and a half 6 mm selector pitches puts the complementary rows in mesh.
    subtract.drives(crank.lift, ratio=9)
    crank.lift.drives(stepped_drum.lift)
    turn.drives(zero_positioning.turn)
    subtract.drives(zero_positioning.subtract)
    turn.drives(anti_reversal.turn)


class TensBellAssembly(layers.TensBellAssembly):
    turn = Port(unit='deg')
    tens_bell_1 = TensBell1(turn=Revolute(axis=(0, 0, 1)))
    turn.drives(tens_bell_1.turn)


class CarryMechanism(SourceCarry):
    tens_bell = TensBellAssembly()
    result_carries = ResultsCarry()
    turns_carries = TurnsCarry()


class CarriageCovers(layers.CarriageCovers):
    digits_cover = DigitsCover()
    upper_housing = UpperHousing()

    def render(self):
        super().render()
        self.clearing_cover.omit()


class ClearingAssembly(layers.ClearingAssembly):
    """The toothed clearing plate and its handle turn together, not the housing."""
    clearing_cover = ClearingGrooveCover()
    tooth_stack = ClearingTeethStack()
    decimal_markers = layers.UpperDecimalMarkers()

    def render(self):
        super().render()
        self.clearing_cover.rotate(180, (0.797150916, -0.603780106, 0))
        self.clearing_cover.translate((0, 0, 57.1))
        self.tooth_stack.rotate(180, (0.797150916, -0.603780106, 0))
        self.tooth_stack.translate((0, 0, 57.1))


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
    clearing_ring = ClearingAssembly(turn=Revolute(axis=(0, 0, 1)))

    def render(self):
        self.decimal_markers.omit()
        self.dial_detents.translate(tuple(-value for value in CARRIAGE_CENTER))
        self.dial_detents.rotate(-CARRIAGE_CLOCKING, (0, 0, 1))


def lifted(source, target):
    def height(manual, clear):
        automatic = clamp01(clear / .1) * (1 - clamp01((clear - .9) / .1))
        return 6 * (manual + automatic + abs(manual - automatic)) / 2
    return height


def clearing_turn(source, target):
    return lambda clear: -360 * clamp01((clear - .1) / .8)


class Carriage(SourceCarriage):
    position = Port()
    lift = Port()
    clear = Port()
    positioning = CarriagePositioning()
    registers = RegisterCarriage(turn=Revolute(axis=(0, 0, 1)),
                                 lift=Prismatic(axis=(0, 0, 1)))
    position.drives(registers.turn, ratio=20)
    (lift & clear).drives(registers.lift, law=lifted)
    registers.lift.drives(positioning.lift)
    clear.drives(registers.clearing_ring.turn, law=clearing_turn)
