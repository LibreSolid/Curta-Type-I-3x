"""Locate bell/carry contact by exact source ingredient; no volume epsilon."""

import argparse
import json
from simulation.carry_mesh import CarryMesh
from simulation.tools.engagement_probe import ingredients


def probe(crank=0, enabled=0):
    model = CarryMesh()
    model.set_state(crank_turns=crank/360, enabled=enabled)
    model.assemble()
    parts = ingredients(model)
    bell = [(path, shape) for path, shape in parts if '.bell.' in path]
    for bank, key in [('result', 'p_10220_410003_1_419227'),
                      ('counter', 'p_10220_410003_1_419081')]:
        group = [(path, shape) for path, shape in parts if f'.{bank}.{key}.' in path]
        for a, first in bell:
            for b, second in group:
                overlap = first.intersect(second)
                assert overlap.isValid(), (a, b)
                volume = sum(solid.Volume() for solid in overlap.Solids())
                if volume > 0:
                    box = overlap.BoundingBox()
                    print(json.dumps({'bell': a, 'carry': b, 'mm3': volume,
                                      'bounds': [box.xmin, box.ymin, box.zmin,
                                                 box.xmax, box.ymax, box.zmax]}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--crank', type=float, default=0)
    parser.add_argument('--enabled', type=int, default=0)
    probe(**vars(parser.parse_args()))
