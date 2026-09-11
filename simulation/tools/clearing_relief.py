"""Compare the formed source and exported relief without coincident booleans."""

import json
import numpy as np
import trimesh
from simulation.clearing import ClearingBench


def faces(mesh):
    return {tuple(sorted(map(tuple, face)))
            for face in np.asarray(mesh.triangles, dtype=np.float32)}


def probe():
    root = ClearingBench()
    root.assemble()
    root.build_stls()
    for part in root.teeth.children:
        original = part.form(trimesh.load_mesh(part.stl_source))
        before, after = faces(original), faces(part.mesh)
        changed = np.array(list(before ^ after)).reshape(-1, 3)
        print(json.dumps(dict(part=part.name, removed_mm3=original.volume-part.mesh.volume,
            original_triangles=len(before), fitted_triangles=len(after),
            changed_triangles=len(before ^ after),
            changed_bounds=[changed.min(axis=0).tolist(), changed.max(axis=0).tolist()])), flush=True)


if __name__ == '__main__':
    probe()
