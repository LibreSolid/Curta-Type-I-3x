"""Name the bell ingredients that touch the original lower carry shoe."""

import json
from simulation.carry_contact import CarryContactBench
from simulation.carry_fits import in_first_result_station
from simulation.standard.parts import TensSliderForResults
from simulation.tools.engagement_probe import ingredients


def probe():
    model = CarryContactBench()
    model.set_state(enabled=1, crank_turns=149/360)
    model.assemble()
    slider = in_first_result_station(TensSliderForResults().shape()).translate((0, 0, -4.2))
    for path, shape in ingredients(model.bell):
        overlap = slider.intersect(shape)
        if overlap.Volume() > 0:
            b = overlap.BoundingBox()
            print(json.dumps({'part': path, 'mm3': overlap.Volume(),
                              'bounds': [b.xmin,b.ymin,b.zmin,b.xmax,b.ymax,b.zmax]}), flush=True)


if __name__ == '__main__':
    probe()
