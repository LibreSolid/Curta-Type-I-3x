"""Measure the carry spring's detent contacts through a complete slider stroke."""

import json
import numpy as np
from simulation.carry import CarryBench
from simulation.tools.interference import world_solids
from solid_node.node.adapters.step import StepAssembly
from simulation.source import STEP


def probe():
    model = CarryBench()
    model.set_state(engaged=0)
    model.assemble()
    occurrence = next(item for item in StepAssembly(STEP).occurrences
                      if item.product_name == model.carry_lever_spring.part)
    inverse = np.linalg.inv(occurrence.world_matrix)
    for index in range(21):
        engaged = index / 20
        model.set_state(engaged=engaged)
        solids = world_solids(model)
        spring = solids['Curta.carry_lever_spring']
        slider = solids['Curta.tens_slider_for_results']
        bearing = solids['Curta.tens_slide_bearing']
        row = {'engaged': engaged}
        for name, part in [('slider', slider), ('bearing', bearing)]:
            overlap = spring.intersect(part)
            assert overlap.isValid(), (name, engaged)
            row[name + '_overlap_mm3'] = overlap.Volume()
            if index in (0, 5, 10, 20):
                row[name + '_regions'] = [
                    {'volume': region.Volume(),
                     'spring_local_center': (inverse @ np.array((*region.Center().toTuple(), 1)))[:3].tolist()}
                    for region in overlap.Solids()]
        print(json.dumps(row), flush=True)


if __name__ == '__main__':
    probe()
