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
from simulation.standard.parts import M4x10_419159
from simulation.retaining_spring import RetainingSpring, SEAT_GAP as SPRING_SEAT_GAP
from simulation.bell_spring_motion import positioning as spring_positioning
from simulation.register_detents import RegisterDetents
from simulation.dial_detent_motion import following
import simulation.standard.layers as layers


class Inputs(SourceInputs):
    selectors = Selectors()


class UpperFrame(layers.UpperFrame):
    def render(self):
        super().render()
        self.m4x10_419159_1.omit()
        self.m4x10_419159_2.omit()


class Frame(SourceFrame):
    upper_frame = UpperFrame()
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
    subtract = Port()
    tens_bell_1 = TensBell1()
    tens_bell_spring = RetainingSpring()
    m4x10_419159_1 = M4x10_419159()
    m4x10_419159_2 = M4x10_419159()
    subtract.drives(tens_bell_spring.spread, law=spring_positioning)

    def render(self):
        super().render()
        self.tens_bell_spring.translate((0, 0, -SPRING_SEAT_GAP))
        # Manual page 9: these two screws secure the spring to the bell.
        self.m4x10_419159_1.rotate(180, (1, 0, 0)).translate((-10.5, 0, -2.7))
        self.m4x10_419159_2.rotate(180, (1, 0, 0)).translate((10.5, 0, -2.7))


class CarryMechanism(SourceCarry):
    tens_bell = TensBellAssembly(turn=Revolute(axis=(0, 0, 1)))
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
    dial_detents = RegisterDetents()
    clearing_ring = ClearingAssembly(turn=Revolute(axis=(0, 0, 1)))

    # Origins are the source-specific dial joints at their calibrated zero.
    result_register.p_10203_1.turn.drives(dial_detents.p_6mm_ball_419241_12.lift, law=following(-146))
    result_register.p_10203_2.turn.drives(dial_detents.p_6mm_ball_419241_1.lift, law=following(-235.99999999))
    result_register.p_10205_1.turn.drives(dial_detents.p_6mm_ball_419241_13.lift, law=following(-275.4500831))
    result_register.p_10205_2.turn.drives(dial_detents.p_6mm_ball_419241_16.lift, law=following(-295.45008308))
    result_register.p_10204_1.turn.drives(dial_detents.p_6mm_ball_419241_11.lift, law=following(-315.45008308))
    result_register.p_10204_2.turn.drives(dial_detents.p_6mm_ball_419241_3.lift, law=following(-335.45008307))
    result_register.p_10204_3.turn.drives(dial_detents.p_6mm_ball_419241_7.lift, law=following(-355.45008308))
    result_register.p_10204_4.turn.drives(dial_detents.p_6mm_ball_419241_4.lift, law=following(-375.45008311))
    result_register.p_10204_5.turn.drives(dial_detents.p_6mm_ball_419241_17.lift, law=following(-395.45008311))
    result_register.p_10204_6.turn.drives(dial_detents.p_6mm_ball_419241_8.lift, law=following(-415.4500831))
    result_register.results_dial_type_2_1.turn.drives(dial_detents.p_6mm_ball_419241_5.lift, law=following(-145.99999998))
    turns_register.p_10203_3.turn.drives(dial_detents.p_6mm_ball_419241_2.lift, law=following(-145.99999998))
    turns_register.p_10203_4.turn.drives(dial_detents.p_6mm_ball_419241_14.lift, law=following(-145.99999999))
    turns_register.p_10205_3.turn.drives(dial_detents.p_6mm_ball_419241_9.lift, law=following(-145.4500831))
    turns_register.p_10205_4.turn.drives(dial_detents.p_6mm_ball_419241_10.lift, law=following(-165.45008308))
    turns_register.p_10204_7.turn.drives(dial_detents.p_6mm_ball_419241_6.lift, law=following(-185.4500831))
    turns_register.results_dial_type_2_2.turn.drives(dial_detents.p_6mm_ball_419241_15.lift, law=following(-145.99999998))

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
