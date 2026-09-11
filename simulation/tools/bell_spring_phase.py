"""Check whether source spring/drum interference is mounting phase or deflection."""

import json
from math import radians
import trimesh
from simulation.bell_spring import BellLeafFitBench
from simulation.standard.parts import TensBellSpring
from simulation.tools.carry_phase import solid
from simulation.tools.interference import rigid_leaves


def probe():
    root = BellLeafFitBench()
    root.set_state(spread=0, subtract=0)
    root.assemble()
    root.build_stls()
    source = TensBellSpring()
    source.assemble()
    source.build_stls()
    spring = solid(source.mesh).translate((0, 0, -8.7))
    bodies = [solid(part.mesh) for _, part in rigid_leaves(root.drum)]
    for lift in (0, 9):
        for angle in range(0, 181, 5):
            rotation = trimesh.transformations.rotation_matrix(radians(angle), (0, 0, 1))
            volumes = [(spring ^ body.transform(rotation[:3]).translate((0, 0, lift))).volume()
                       for body in bodies]
            print(json.dumps(dict(lift=lift, drum_phase=angle, overlap_mm3=volumes)), flush=True)


if __name__ == '__main__':
    probe()
