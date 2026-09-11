"""Measure hook spreading against the two actual slider detent profiles."""

import json
import numpy as np
import cadquery as cq
from solid_node.node.adapters.step import StepAssembly
from simulation.source import STEP
from simulation.carry_spring import HALF_SPAN, TIP_CENTER, FIRST_TIP
from simulation.tools.carry_spring import SourceCarryBench, SourceTurnsBench
from simulation.tools.transmission_import import translation
from simulation.tools.interference import world_solids


def probe():
    source = StepAssembly(STEP)
    for bank, cls, slider_name in [('Results', SourceCarryBench, 'tens_slider_for_results'),
                                   ('Turns', SourceTurnsBench, 'tens_slider_for_turns_counter')]:
        model = cls()
        model.set_state(engaged=0)
        model.assemble()
        origin = translation(f'{bank}TensLeverAssembly1', 'carry_lever_spring')
        occurrence = next(item for item in source.occurrences
                          if item.product_name == model.carry_lever_spring.part
                          and np.linalg.norm(np.array(item.world_matrix)[:3, 3] - origin) < 1e-7)

        def hooks(spread):
            wires = [cq.Solid.makeCylinder(.35, 5.1,
                        cq.Vector(TIP_CENTER + sign*(HALF_SPAN + spread), .6, FIRST_TIP[2]),
                        cq.Vector(0, 1, 0)) for sign in (-1, 1)]
            gauge = cq.Compound.makeCompound(wires)
            return gauge.rotate((0, 0, 0), occurrence.axis, occurrence.angle_deg).translate(occurrence.translation)

        for index in range(101):
            engaged = index / 100
            model.set_state(engaged=engaged)
            slider = world_solids(model)['Curta.' + slider_name]

            def blocked(spread):
                overlap = slider.intersect(hooks(spread))
                assert overlap.isValid(), (bank, engaged, spread)
                return overlap.Volume() > 0

            low, high = 0, 3
            assert not blocked(high), (bank, engaged)
            if blocked(0):
                for _ in range(16):
                    mid = (low + high)/2
                    if blocked(mid):
                        low = mid
                    else:
                        high = mid
            else:
                high = 0
            print(json.dumps({'bank': bank, 'engaged': engaged, 'spread': high}), flush=True)


if __name__ == '__main__':
    probe()
