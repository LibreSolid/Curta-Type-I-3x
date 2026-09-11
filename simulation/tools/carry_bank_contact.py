"""Locate a shifted neighbouring pin's contact and gauge its protrusion."""

import json
from math import cos, sin, radians
from simulation.curta import Curta
from simulation.tools.interference import world_solids


def probe():
    root = Curta()
    root.set_state(initial_result=22222222222, initial_turns=222222, operand=0,
                   crank_turns=0, subtract=0, carriage_position=2, carriage_lift=0, clear=0)
    root.assemble()
    slider_path = ('Curta.carry_mechanism.result_carries.results_tens_lever_assembly_10'
                   '.tens_slider_for_results')
    pin_path = 'Curta.carriage.registers.turns_register.p_10203_3.number_roll_carry_pin_half'
    shapes = world_solids(root, selected={slider_path, pin_path})
    slider, pin = shapes[slider_path], shapes[pin_path]
    outward = (cos(radians(170)), sin(radians(170)), 0)
    for step in range(41):
        depth = step / 10
        moved = pin.translate(tuple(depth*value for value in outward))
        contact = slider.intersect(moved)
        bounds = contact.BoundingBox() if contact.Volume() > 0 else None
        print(json.dumps(dict(outward_mm=depth, overlap_mm3=contact.Volume(),
            center=contact.Center().toTuple() if bounds else None,
            bounds=[bounds.xmin,bounds.xmax,bounds.ymin,bounds.ymax,bounds.zmin,bounds.zmax]
                   if bounds else None)), flush=True)


if __name__ == '__main__':
    probe()
