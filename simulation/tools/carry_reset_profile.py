"""Measure how the rotating bell limits a lowered lever, without a reset law."""

import json
from math import radians
import trimesh
from simulation.carry_contact import CarryContactBench
from simulation.tools.carry_phase import solid


def probe():
    model = CarryContactBench()
    model.set_state(enabled=0, crank_turns=0)
    model.assemble()
    model.build_stls()
    bell = solid(model.bell.mesh)
    for bank, part in (
        ('result', model.results_lever.tens_slider_for_results),
        ('counter', model.turns_lever.tens_slider_for_turns_counter),
    ):
        slider = solid(part.mesh)
        for angle in range(361):
            matrix = trimesh.transformations.rotation_matrix(radians(-angle), (0, 0, 1))
            posed = bell.transform(matrix[:3])
            def contact(drop):
                return (posed ^ slider.translate((0, 0, -drop))).volume()
            if contact(4.2) <= 0:
                continue
            assert contact(0) <= 0, (bank, angle)
            low, high = 0, 4.2
            for _ in range(18):
                middle = (low + high)/2
                if contact(middle) > 0:
                    high = middle
                else:
                    low = middle
            print(json.dumps(dict(bank=bank, angle=angle, maximum_drop_mm=low,
                                  required_lift_mm=4.2-low)), flush=True)


if __name__ == '__main__':
    probe()
