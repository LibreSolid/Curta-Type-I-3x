"""Measure the lever depression required by a dial pin, independently of timing."""

import argparse
import json
from math import radians, sin, cos
import numpy as np
import trimesh
import manifold3d as manifold
from OCP.BRepAdaptor import BRepAdaptor_Surface
from simulation.carry_contact import CarryContactBench
from simulation.tools.carry_phase import solid
from simulation.tools.interference import world_solids
from simulation.standard.carry import ResultsLever5
from solid_node.simulation import Driver


class FullPinLever(ResultsLever5):
    engaged = Driver(default=0, range=(0, 1))
    engaged.drives(ResultsLever5.engage)


def probe(clocking=0, index=0, survey=False, full=False, head_trim=0, pin_outward=0):
    model = CarryContactBench()
    model.set_state(crank_turns=0, enabled=0)
    model.assemble()
    model.build_stls()
    pin_node = (model.results_dials.p_10204_1.number_roll_carry_pin_full if full else
                model.results_dials.p_10203_1.number_roll_carry_pin_half)
    pin = solid(pin_node.mesh)
    if full:
        lever = FullPinLever()
        lever.set_state(engaged=0)
        lever.assemble()
        lever.build_stls()
        slider = solid(lever.tens_slider_for_results.mesh)
    else:
        slider = solid(model.results_lever.tens_slider_for_results.mesh)
    if head_trim:
        above_tip = manifold.Manifold.cube((200, 200, 100)).translate((-100, -100, 33 - head_trim))
        slider = slider - above_tip
    station = -80 if full else 0
    dial_axis = np.array((cos(radians(station)), sin(radians(station)), 0))
    pin = pin.translate(tuple(pin_outward*dial_axis))
    dial_at = 71.474057463*dial_axis + (0, 0, 33.9)
    path = ('Curta.results_dials.p_10204_1.number_roll_carry_pin_full' if full else
            'Curta.results_dials.p_10203_1.number_roll_carry_pin_half')
    shape = world_solids(model, selected={path})[path]
    face = max((face for face in shape.Faces() if face.geomType() == 'CYLINDER'),
               key=lambda face: face.Area())
    cylinder = BRepAdaptor_Surface(face.wrapped).Cylinder()
    axis, at = cylinder.Axis().Direction().Coord(), cylinder.Location().Coord()
    if survey:
        for trial in range(-90, 91, 10):
            clock = trimesh.transformations.rotation_matrix(radians(trial), axis, at)
            rotated = pin.transform(clock[:3])
            worst, first, last, at_nine = 0, None, None, 0
            for step in range(400, 501):
                digit = step/50
                matrix = trimesh.transformations.rotation_matrix(radians(36*(digit+index)),
                    dial_axis, dial_at)
                posed = rotated.transform(matrix[:3])
                def contact(drop):
                    return (posed ^ slider.translate((0, 0, -drop))).volume()
                if contact(0) <= 0:
                    continue
                first = digit if first is None else first
                last = digit
                low, high = 0, 6
                assert contact(high) <= 0
                for _ in range(16):
                    middle = (low + high)/2
                    if contact(middle) > 0:
                        low = middle
                    else:
                        high = middle
                worst = max(worst, high)
                if step == 450:
                    at_nine = high
            print(json.dumps(dict(clocking=trial, first=first, last=last,
                                  maximum_drop_mm=worst, at_nine_mm=at_nine)), flush=True)
        return
    clock = trimesh.transformations.rotation_matrix(radians(clocking), axis, at)
    pin = pin.transform(clock[:3])
    for step in range(501):
        digit = step/50
        matrix = trimesh.transformations.rotation_matrix(radians(36*(digit+index)),
                                                         dial_axis, dial_at)
        posed = pin.transform(matrix[:3])
        def contact(drop):
            return (posed ^ slider.translate((0, 0, -drop))).volume()
        initial = contact(0)
        if initial <= 0:
            continue
        if contact(4.2) > 0:
            drop = None
        else:
            low, high = 0, 4.2
            for _ in range(18):
                middle = (low + high)/2
                if contact(middle) > 0:
                    low = middle
                else:
                    high = middle
            drop = high
        print(json.dumps({'digit': digit, 'clocking': clocking, 'index': index,
                          'upper_overlap_mm3': initial, 'minimum_drop_mm': drop}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--clocking', type=float, default=0)
    parser.add_argument('--index', type=float, default=0)
    parser.add_argument('--survey', action='store_true')
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--head-trim', type=float, default=0)
    parser.add_argument('--pin-outward', type=float, default=0)
    probe(**vars(parser.parse_args()))
