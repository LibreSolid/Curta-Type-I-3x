"""Measure the carry spring's detent contacts through a complete slider stroke."""

import json
import argparse
import numpy as np
from simulation.standard.assembly import ResultsTensLeverAssembly1, TurnsTensLeverAssembly1
from simulation.standard.parts import TensSliderForResults, TensSliderForTurnsCounter
from solid_node.motion.joints import Prismatic
from solid_node.simulation import Driver
from simulation.tools.interference import world_solids
from solid_node.node.adapters.step import StepAssembly
from simulation.source import STEP
from simulation.tools.transmission_import import translation
from simulation.standard.parts import CarryLeverSpring


class SourceCarryBench(ResultsTensLeverAssembly1):
    engaged = Driver(default=0, range=(0, 1))
    tens_slider_for_results = TensSliderForResults(travel=Prismatic(axis=(0, 0, -1)))
    engaged.drives(tens_slider_for_results.travel, ratio=4.2, offset=-4.2)


class SourceTurnsBench(TurnsTensLeverAssembly1):
    engaged = Driver(default=0, range=(0, 1))
    tens_slider_for_turns_counter = TensSliderForTurnsCounter(travel=Prismatic(axis=(0, 0, -1)))
    engaged.drives(tens_slider_for_turns_counter.travel, ratio=4.2, offset=-1.8)


def probe(fitted=False):
    from simulation.carry import CarryBench
    model = CarryBench() if fitted else SourceCarryBench()
    model.set_state(engaged=0)
    model.assemble()
    origin = translation('ResultsTensLeverAssembly1', 'carry_lever_spring')
    occurrence = next(item for item in StepAssembly(STEP).occurrences
                      if item.product_name == CarryLeverSpring.part
                      and np.linalg.norm(np.array(item.world_matrix)[:3, 3] - origin) < 1e-7)
    inverse = np.linalg.inv(occurrence.world_matrix)
    for index in range(21):
        engaged = index / 20
        model.set_state(engaged=engaged)
        solids = world_solids(model, include_flexible=fitted)
        spring = solids['Curta.carry_lever_spring' + ('.wire' if fitted else '')]
        slider = solids['Curta.tens_slider_for_results']
        bearing = solids['Curta.tens_slide_bearing']
        row = {'engaged': engaged, 'wire_valid': spring.isValid(),
               'wire_solids': len(spring.Solids()), 'wire_volume': spring.Volume()}
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fitted', action='store_true')
    probe(parser.parse_args().fitted)
