"""Sweep an offset half pin past the neighbouring inactive carry head."""

import json
import argparse
from math import radians, cos, sin
import numpy as np
import trimesh
from OCP.BRepAdaptor import BRepAdaptor_Surface
from simulation.carry_contact import CarryContactBench
from simulation.tools.carry_phase import solid
from simulation.tools.interference import world_solids


def probe(pin_outward=0, clocking=0):
    model = CarryContactBench()
    model.set_state(enabled=0, crank_turns=0)
    model.assemble()
    model.build_stls()
    pin = solid(model.results_dials.p_10203_1.number_roll_carry_pin_half.mesh).translate((pin_outward, 0, 0))
    path = 'Curta.results_dials.p_10203_1.number_roll_carry_pin_half'
    shape = world_solids(model, selected={path})[path]
    face = max((face for face in shape.Faces() if face.geomType() == 'CYLINDER'),
               key=lambda face: face.Area())
    cylinder = BRepAdaptor_Surface(face.wrapped).Cylinder()
    pin = pin.transform(trimesh.transformations.rotation_matrix(radians(clocking),
        cylinder.Axis().Direction().Coord(), cylinder.Location().Coord())[:3])
    rotate = lambda angle: trimesh.transformations.rotation_matrix(radians(angle), (0, 0, 1))
    for bank, node, angle in (
        ('result', model.results_lever.tens_slider_for_results, 0),
        ('counter', model.turns_lever.tens_slider_for_turns_counter, -130),
    ):
        slider = solid(node.mesh).transform(rotate(angle)[:3])
        for offset in (-10, 10):
            shifted = pin.transform(rotate(offset)[:3])
            axis = np.array((cos(radians(offset)), sin(radians(offset)), 0))
            at = 71.474057463 * axis + (0, 0, 33.9)
            for step in range(501):
                digit = step / 50
                pose = trimesh.transformations.rotation_matrix(radians(36*digit), axis, at)
                contact = slider ^ shifted.transform(pose[:3])
                if contact.volume() <= 0:
                    continue
                vertices = np.asarray(contact.to_mesh().vert_properties)[:, :3]
                print(json.dumps(dict(bank=bank, offset=offset, digit=digit,
                    volume=contact.volume(), low=vertices.min(axis=0).tolist(),
                    high=vertices.max(axis=0).tolist())), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pin-outward', type=float, default=0)
    parser.add_argument('--clocking', type=float, default=0)
    probe(**vars(parser.parse_args()))
