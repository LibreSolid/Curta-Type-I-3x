"""Educational layers: visibility follows the mechanism, not STEP export order."""

from solid_node.node import AssemblyNode
import simulation.standard.layers as layers


class Frame(AssemblyNode):
    upper_frame = layers.UpperFrame()
    lower_bearing_plate = layers.LowerBearingPlate()
    fasteners = layers.FrameFasteners()


class Inputs(AssemblyNode):
    selectors = layers.InputSelectors()
    bearings = layers.InputBearings()


class MainDrive(AssemblyNode):
    crank = layers.CrankAssembly()
    stepped_drum = layers.DrumAssembly()
    zero_positioning = layers.ZeroPositioning()
    anti_reversal = layers.AntiReversal()
    reversing_lever = layers.ReversingAssembly()


class CarryMechanism(AssemblyNode):
    tens_bell = layers.TensBellAssembly()
    result_carries = layers.ResultCarry()
    turns_carries = layers.TurnsCarry()
    lever_pivots = layers.CarryPivots()


class RegisterCarriage(AssemblyNode):
    covers = layers.CarriageCovers()
    result_register = layers.ResultRegister()
    turns_register = layers.TurnsRegister()
    dial_detents = layers.RegisterDetents()
    clearing_ring = layers.ClearingAssembly()
    carrier = layers.CarriageStructure()
    decimal_markers = layers.DecimalMarkers()


class Carriage(AssemblyNode):
    positioning = layers.CarriagePositioning()
    registers = RegisterCarriage()


class LayeredSource(AssemblyNode):
    """All 547 source occurrences regrouped, without correcting their geometry."""

    enclosure = layers.Enclosure()
    frame = Frame()
    input_selectors = Inputs()
    main_drive = MainDrive()
    transmission = layers.Transmission()
    carry_mechanism = CarryMechanism()
    carriage = Carriage()
