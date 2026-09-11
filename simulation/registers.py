"""Dial joints and source-specific clocking; one port per register value."""

from solid_node.node import AssemblyNode
from solid_node.motion.joints import Revolute
from solid_node.motion.ports import Port
from solid_node.simulation import Driver
from simulation.cycle import dial_positions
from simulation.fit import CARRIAGE_CENTER, CARRIAGE_CLOCKING, INPUT_CLOCKING
from simulation.standard.assembly import *
import simulation.standard.layers as source


def dial_values(phases, counter=False):
    return lambda sources, targets: lambda *values: tuple(
        phase - INPUT_CLOCKING / 2 - 36 * position for phase, position in
        zip(phases, dial_positions(*values, len(phases), counter)))


def neutral_operation(source, targets):
    return lambda value: (0, 0, 0)


class ResultRegister(source.ResultRegister):
    value = Port()
    operand = Port()
    crank_turns = Port(unit='rev')
    subtract = Port()
    carriage_position = Port()
    clear = Port()

    p_10203_1 = Part10203_1(turn=Revolute(
        axis=(-0.9999539409, -0.0095977127, 2e-10), at=(72.008486542, 0.647810225, 33.9)))
    p_10203_2 = Part10203_2(turn=Revolute(
        axis=(-0.9429319505, 0.3329854904, 1e-10), at=(67.932893459, -23.838001321, 33.9)))
    p_10205_1 = Part10205_1(turn=Revolute(
        axis=(-0.7721784508, 0.6354057288, 0.0), at=(55.72844801, -45.453202839, 33.9)))
    p_10205_2 = Part10205_2(turn=Revolute(
        axis=(-0.5082888339, 0.8611866588, 0.0), at=(36.867186359, -61.590682021, 33.9)))
    p_10204_1 = Part10204_1(turn=Revolute(
        axis=(-0.183092082, 0.9830957682, 0.0), at=(13.624055025, -70.304020713, 33.9)))
    p_10204_2 = Part10204_2(turn=Revolute(
        axis=(0.164188277, 0.9864290191, 0.0), at=(-11.197481322, -70.542261674, 33.9)))
    p_10204_3 = Part10204_3(turn=Revolute(
        axis=(0.491665107, 0.870784372, 0.0), at=(-34.603579072, -62.276669529, 33.9)))
    p_10204_4 = Part10204_4(turn=Revolute(
        axis=(0.759839869, 0.650110278, 0.0), at=(-53.771117399, -46.504196676, 33.9)))
    p_10204_5 = Part10204_5(turn=Revolute(
        axis=(0.9363667283, 0.3510232901, 0.0), at=(-66.388208297, -25.127236119, 33.9)))
    p_10204_6 = Part10204_6(turn=Revolute(
        axis=(0.9999539409, 0.009597713, 0.0), at=(-70.933044396, -0.724164791, 33.9)))
    results_dial_type_2_1 = ResultsDialType2(turn=Revolute(
        axis=(0.9429319507, -0.3329854896, 1e-10), at=(-66.857451389, 23.761646754, 33.9)))

    (value & operand & crank_turns & subtract & carriage_position & clear).drives((
        p_10203_1.turn,
        p_10203_2.turn,
        p_10205_1.turn,
        p_10205_2.turn,
        p_10204_1.turn,
        p_10204_2.turn,
        p_10204_3.turn,
        p_10204_4.turn,
        p_10204_5.turn,
        p_10204_6.turn,
        results_dial_type_2_1.turn,
    ), law=dial_values((3.0, -86.99999999, -126.4500831, -146.45008308, -166.45008308, -186.45008307, -206.45008308, -226.45008311, -246.45008311, -266.4500831, 3.00000002)))

    def render(self):
        super().render()
        self.translate(tuple(-value for value in CARRIAGE_CENTER))
        self.rotate(-CARRIAGE_CLOCKING, (0, 0, 1))


class TurnsRegister(source.TurnsRegister):
    value = Port()
    operand = Port()
    crank_turns = Port(unit='rev')
    subtract = Port()
    carriage_position = Port()
    clear = Port()

    p_10203_3 = Part10203_3(turn=Revolute(
        axis=(0.650110279, -0.7598398681, 3e-10), at=(-45.928298358, 54.270661151, 33.9)))
    p_10203_4 = Part10203_4(turn=Revolute(
        axis=(0.3510232907, -0.936366728, 0.0), at=(-24.5513378, 66.887752049, 33.9)))
    p_10205_3 = Part10205_3(turn=Revolute(
        axis=(0.009597713, -0.9999539409, 0.0), at=(-0.148266473, 71.432588148, 33.9)))
    p_10205_4 = Part10205_4(turn=Revolute(
        axis=(-0.3329854899, -0.9429319506, 0.0), at=(24.337545072, 67.35699514, 33.9)))
    p_10204_7 = Part10204_7(turn=Revolute(
        axis=(-0.6354057288, -0.7721784508, 0.0), at=(45.952746591, 55.152549691, 33.9)))
    results_dial_type_2_2 = ResultsDialType2(turn=Revolute(
        axis=(-0.8611866588, -0.508288834, -0.0), at=(62.090225773, 36.291288041, 33.9)))

    (value & operand & crank_turns & subtract & carriage_position & clear).drives((
        p_10203_3.turn,
        p_10203_4.turn,
        p_10205_3.turn,
        p_10205_4.turn,
        p_10204_7.turn,
        results_dial_type_2_2.turn,
    ), law=dial_values((3.00000002, 3.00000001, 3.5499169, -16.45008308, -36.4500831, 3.00000002), counter=True))

    def render(self):
        super().render()
        self.translate(tuple(-value for value in CARRIAGE_CENTER))
        self.rotate(-CARRIAGE_CLOCKING, (0, 0, 1))


class RegisterBench(AssemblyNode):
    result = Driver(default=0, range=(0, 99999999999), dtype=int)
    operand = Driver(default=1, range=(0, 99999999), dtype=int)
    crank_turns = Driver(default=0, range=(0, 1), unit='rev')
    registers = ResultRegister()
    result.drives(registers.value)
    operand.drives(registers.operand)
    crank_turns.drives(registers.crank_turns)
    result.drives((registers.subtract, registers.carriage_position, registers.clear), law=neutral_operation)
