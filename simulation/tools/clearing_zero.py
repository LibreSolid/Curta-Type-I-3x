"""Locate any clearing-row contact at the physical zero index."""

import json
from math import radians
import numpy as np
import trimesh
import manifold3d as manifold
from simulation.clearing_contact import ClearingContactBench
from simulation.tools.carry_phase import solid


def probe():
    model = ClearingContactBench()
    model.set_state(digit=0, clear=0)
    model.assemble()
    model.build_stls()
    strips = [(part.name, solid(part.mesh)) for part in model.clearing.tooth_stack.children]
    for kind, part in [('outer', model.results.p_10203_1.results_dial_type_1),
                        ('inner', model.results.p_10205_1.results_dial_type_2)]:
        dial = solid(part.mesh)
        rows = []
        for angle in np.arange(0, 80.01, .25):
            matrix = trimesh.transformations.rotation_matrix(radians(-angle), (0, 0, 1))
            for name, strip in strips:
                overlap = dial ^ strip.transform(matrix[:3])
                assert overlap.status() == manifold.Error.NoError
                if overlap.volume() > 0:
                    vertices = overlap.to_mesh().vert_properties[:, :3]
                    rows.append({'kind': kind, 'strip': name, 'angle': float(angle),
                                 'volume': overlap.volume(),
                                 'bounds': [vertices.min(axis=0).tolist(), vertices.max(axis=0).tolist()]})
        print(json.dumps({'kind': kind, 'contacts': rows}), flush=True)


if __name__ == '__main__':
    probe()
