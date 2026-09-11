"""Compare all source carry springs in their own bearing frames."""

import json
import numpy as np
from solid_node.node.adapters.step import StepAssembly
from simulation.source import STEP
from simulation.tools.transmission_import import translation


def probe():
    source = StepAssembly(STEP)
    for bank, count in [('Results', 10), ('Turns', 5)]:
        for index in range(1, count + 1):
            name = f'{bank}TensLeverAssembly{index}'
            origin = translation(name, 'tens_slide_bearing')
            spring_origin = translation(name, 'carry_lever_spring')

            def at(point):
                return next(item for item in source.occurrences
                            if np.linalg.norm(np.array(item.world_matrix)[:3, 3] - point) < 1e-7)

            bearing, spring = at(origin), at(spring_origin)
            relative = np.linalg.inv(bearing.world_matrix) @ spring.world_matrix
            print(json.dumps({'lever': name, 'bearing': origin,
                              'spring_in_bearing': np.round(relative, 6).tolist()}), flush=True)


if __name__ == '__main__':
    probe()
