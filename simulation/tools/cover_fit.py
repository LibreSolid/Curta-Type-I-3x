"""Compare source cover datums with the recentered operating register axes."""

import json
from math import radians
import trimesh
from simulation.curta import Curta
from simulation.standard.parts import ResultsDialType1, ResultsDialType2
from simulation.tools.interference import rigid_leaves
from simulation.tools.carry_phase import solid
from simulation.fit import CARRIAGE_CLOCKING

COVER_CENTRE = (.386511579, -.028412332, 0)


def probe():
    root = Curta()
    rest = root.instructions['Rest'].targets
    root.set_state(**rest)
    root.assemble()
    root.build_stls()
    carriage = root.carriage.registers
    covers = dict(digits=carriage.covers.digits_cover, housing=carriage.covers.upper_housing)
    dials = [(path, part) for path, part in rigid_leaves(root)
             if isinstance(part, (ResultsDialType1, ResultsDialType2))]
    assert len(dials) == 17
    candidates = {}
    for name, node in covers.items():
        # Reconstruct the untouched source placements, independent of the fit
        # currently installed in the operating model.
        source_mesh = trimesh.load_mesh(node.stl_source)
        angle, axis, height = ((-180, (.168920173, .985629735, 0), 31.6)
                               if name == 'digits' else
                               (160.549916905, (0, 0, 1), -4.4))
        source_mesh.apply_transform(trimesh.transformations.rotation_matrix(radians(angle), axis))
        source_mesh.apply_translation((*COVER_CENTRE[:2], height))
        source = solid(source_mesh)
        centered = source.translate(tuple(-coordinate for coordinate in COVER_CENTRE))
        clocked = centered.rotate((0, 0, -CARRIAGE_CLOCKING))
        candidates[name] = dict(source=source, centered=centered,
                               clocked=clocked, seated_up=clocked.translate((0, 0, .05)),
                               seated_down=clocked.translate((0, 0, -.05)))
    for digit in range(10):
        root.set_state(initial_result=digit*11111111111, initial_turns=digit*111111)
        wheels = [(path, solid(dial.mesh)) for path, dial in dials]
        for cover, placements in candidates.items():
            for placement, body in placements.items():
                volumes = {path: (body ^ dial).volume() for path, dial in wheels}
                print(json.dumps(dict(cover=cover, placement=placement, digit=digit,
                                      overlap_mm3=volumes)), flush=True)


if __name__ == '__main__':
    probe()
