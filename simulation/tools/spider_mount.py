"""Read the spider ring's installed collar seat before prescribing preload."""

import json
from simulation.curta import Curta
from simulation.tools.carry_phase import solid
from simulation.standard.parts import SpiderSpring


def probe():
    root = Curta()
    root.set_state(**root.instructions['Rest'].targets)
    root.assemble()
    root.build_stls()
    carriage = root.carriage.registers
    source = SpiderSpring()
    source.assemble()
    source.build_stls()
    spring = solid(source.mesh).translate((0, 0, 45.2))
    hardware = {
        'collar': carriage.carrier.crank_collar,
        'cover': carriage.clearing_ring.clearing_cover,
        'carrier': carriage.carrier.upper_carriage_body_1.counter_body,
        'pin_1': carriage.carrier.upper_carriage_body_1.counter_body_pin_1,
        'pin_2': carriage.carrier.upper_carriage_body_1.counter_body_pin_2,
    }
    bodies = {name: solid(node.mesh) for name, node in hardware.items()}
    for step in range(-16, 17):
        height = step/4
        moved = spring.translate((0, 0, height))
        volumes = {name: (moved ^ body).volume() for name, body in bodies.items()}
        print(json.dumps(dict(rise=height, overlap_mm3=volumes)), flush=True)


if __name__ == '__main__':
    probe()
