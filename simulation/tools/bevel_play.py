"""Measure each installed bevel pair's flank contacts around its own shaft."""

import json
import numpy as np
from simulation.curta import Curta
from simulation.fit import FittedBevelTip
from simulation.standard.parts import ResultsDialType1, ResultsDialType2
from simulation.tools.interference import world_solids, rigid_leaves


def probe():
    model = Curta()
    model.set_state(**Curta.instructions['Rest'].targets)
    model.assemble()
    model.build_stls()
    world, origins = world_solids(model), {}
    parts = list(rigid_leaves(model))
    dials = [(path, part) for path, part in parts
             if isinstance(part, (ResultsDialType1, ResultsDialType2))]

    def visit(node, path, ancestors):
        operations = [*node.operations, *ancestors]
        if isinstance(node, FittedBevelTip):
            at = np.array([0., 0., 0., 1.])
            for operation in operations:
                at = operation.matrix() @ at
            origins[path] = at[:3]
        for child in node.children:
            visit(child, path + '.' + child.name, operations)

    visit(model, 'Curta', [])
    for path, part in parts:
        if not isinstance(part, FittedBevelTip):
            continue
        dial_path, dial = min(dials, key=lambda item:
            np.linalg.norm(item[1].mesh.centroid[:2] - part.mesh.centroid[:2]))
        x, y, z = origins[path]
        volumes = {}
        for angle in (-24, -18, -12, 12, 18, 24):
            overlap = world[path].rotate((x, y, z), (x, y, z + 1), angle).intersect(world[dial_path])
            assert overlap.isValid()
            volumes[angle] = sum(solid.Volume() for solid in overlap.Solids())
        print(json.dumps({'tip': path, 'dial': dial_path, 'mm3': volumes}), flush=True)


if __name__ == '__main__':
    probe()
