"""Locate dial-pin, flange and reset-cam contacts through a complete carry."""

import json
import numpy as np
from simulation.carry_contact import CarryContactBench
from simulation.tools.carry_phase import solid
from simulation.tools.interference import rigid_leaves


def probe():
    model = CarryContactBench()
    model.set_state(crank_turns=0, enabled=0)
    model.assemble()
    model.build_stls()
    interfaces = (
        ('result', model.results_lever.tens_slider_for_results,
         model.results_dials.p_10203_1.number_roll_carry_pin_half, model.result),
        ('counter', model.turns_lever.tens_slider_for_turns_counter,
         model.turns_dials.p_10203_3.number_roll_carry_pin_half, model.counter),
    )
    for enabled in (0, 1):
        contacts = {}
        for angle in range(361):
            model.set_state(crank_turns=angle/360, enabled=enabled)
            for bank, slider, pin, shaft in interfaces:
                body = solid(slider.mesh)
                mates = [('pin', pin), ('reset', model.bell)]
                mates += [(path, part) for path, part in rigid_leaves(shaft, 'shaft')]
                for kind, mate in mates:
                    overlap = body ^ solid(mate.mesh)
                    volume = overlap.volume()
                    if volume > 0:
                        key = (bank, kind)
                        record = contacts.setdefault(key, {'bank': bank, 'kind': kind,
                            'enabled': enabled, 'first': angle, 'maximum_mm3': 0})
                        record['last'] = angle
                        if volume > record['maximum_mm3']:
                            record.update(maximum_mm3=volume, worst=angle,
                                          bounds=list(overlap.bounding_box()))
        print(json.dumps({'enabled': enabled, 'contacts': list(contacts.values())}), flush=True)


if __name__ == '__main__':
    probe()
