"""Carry sliders at their source bearing stations; the spring fit is separate."""

from solid_node.motion.joints import Prismatic
from solid_node.motion.ports import Port
from simulation.standard.parts import TensSliderForResults, TensSliderForTurnsCounter
import simulation.standard.assembly as source
import simulation.standard.layers as layers


class ResultsLever1(source.ResultsTensLeverAssembly1):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=-4.2)


class ResultsLever2(source.ResultsTensLeverAssembly2):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=0.0)


class ResultsLever3(source.ResultsTensLeverAssembly3):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=0.0)


class ResultsLever4(source.ResultsTensLeverAssembly4):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=0.0)


class ResultsLever5(source.ResultsTensLeverAssembly5):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=0.0)


class ResultsLever6(source.ResultsTensLeverAssembly6):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=-4.2)


class ResultsLever7(source.ResultsTensLeverAssembly7):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=0.0)


class ResultsLever8(source.ResultsTensLeverAssembly8):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=-4.2)


class ResultsLever9(source.ResultsTensLeverAssembly9):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=-4.2)


class ResultsLever10(source.ResultsTensLeverAssembly10):
    engage = Port()
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_results.travel, ratio=4.2, offset=-4.2)


class ResultsCarry(layers.ResultCarry):
    results_tens_lever_assembly_1 = ResultsLever1()
    results_tens_lever_assembly_2 = ResultsLever2()
    results_tens_lever_assembly_3 = ResultsLever3()
    results_tens_lever_assembly_4 = ResultsLever4()
    results_tens_lever_assembly_5 = ResultsLever5()
    results_tens_lever_assembly_6 = ResultsLever6()
    results_tens_lever_assembly_7 = ResultsLever7()
    results_tens_lever_assembly_8 = ResultsLever8()
    results_tens_lever_assembly_9 = ResultsLever9()
    results_tens_lever_assembly_10 = ResultsLever10()


class TurnsLever1(source.TurnsTensLeverAssembly1):
    engage = Port()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_turns_counter.travel, ratio=4.2, offset=-1.8)


class TurnsLever2(source.TurnsTensLeverAssembly2):
    engage = Port()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_turns_counter.travel, ratio=4.2, offset=-1.8)


class TurnsLever3(source.TurnsTensLeverAssembly3):
    engage = Port()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_turns_counter.travel, ratio=4.2, offset=-1.8)


class TurnsLever4(source.TurnsTensLeverAssembly4):
    engage = Port()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_turns_counter.travel, ratio=4.2, offset=-1.8)


class TurnsLever5(source.TurnsTensLeverAssembly5):
    engage = Port()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter(travel=Prismatic(axis=(0, 0, -1)))
    engage.drives(tens_slider_for_turns_counter.travel, ratio=4.2, offset=-1.8)


class TurnsCarry(layers.TurnsCarry):
    turns_tens_lever_assembly_1 = TurnsLever1()
    turns_tens_lever_assembly_2 = TurnsLever2()
    turns_tens_lever_assembly_3 = TurnsLever3()
    turns_tens_lever_assembly_4 = TurnsLever4()
    turns_tens_lever_assembly_5 = TurnsLever5()
