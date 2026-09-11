"""Print the source spring terminals and mating bore axes in world coordinates."""

import json
import numpy as np
from solid_node.node.adapters.step import StepAssembly
from simulation.source import STEP
from simulation.standard.parts import AntiReversalSpring, ReverseRotationPreventionPawl, BearingPlate


def probe():
    source = StepAssembly(STEP)
    for cls in (AntiReversalSpring, ReverseRotationPreventionPawl, BearingPlate):
        part = cls()
        occurrence = next(item for item in source.occurrences if item.product_name == part.part)
        for face in part.shape().Faces():
            kind = 'PLANE' if cls is AntiReversalSpring else 'CYLINDER'
            if face.geomType() != kind:
                continue
            center = (occurrence.world_matrix @ np.array((*face.Center().toTuple(), 1)))[:3]
            if cls is BearingPlate and np.linalg.norm(center[:2] - (-54.48, 16.42)) > 10:
                continue
            print(json.dumps({'part': cls.__name__, 'area': face.Area(),
                              'center': center.tolist()}))


if __name__ == '__main__':
    probe()
