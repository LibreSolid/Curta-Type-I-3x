"""Center the installed bevel's backlash without loosening its axial fit."""

from math import radians
import json
import numpy as np
import trimesh
from simulation.curta import Curta
from simulation.tools.carry_phase import solid


def probe():
    model = Curta()
    model.set_state(**Curta.instructions['Rest'].targets)
    model.assemble()
    model.build_stls()
    tip = model.transmission.result.ones.p_10208_1.transmission_gear_tip.mesh
    dial = model.carriage.registers.result_register.p_10203_1.results_dial_type_1.mesh

    def moved(mesh, angle, axis, at):
        copy = mesh.copy()
        copy.apply_transform(trimesh.transformations.rotation_matrix(radians(angle), axis, at))
        return solid(copy)

    gears = {(angle, perturb): moved(tip, angle + perturb, (0, 0, 1), (40.5, 0, 0))
             for angle in range(0, 73, 6) for perturb in (-12, 0, 12)}
    for phase in np.arange(-5, 1.01, .5):
        clear, blocked = [], []
        for angle in range(0, 73, 6):
            wheel = moved(dial, phase - angle/2, (-1, 0, 0), (71.474057463, 0, 33.9))
            clear.append((gears[angle, 0] ^ wheel).volume())
            for perturb in (-12, 12):
                blocked.append((gears[angle, perturb] ^ wheel).volume())
        print(json.dumps({'dial_phase': float(phase), 'max_overlap': max(clear),
                          'min_blocked_volume': min(blocked)}), flush=True)


if __name__ == '__main__':
    probe()
