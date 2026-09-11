"""Measure law expansion before building CAD or allocating the expanded wires.

A short symbolic time token stands in for each root driver. This is a lower
bound on raw expression size, not an exported document or a motion substitute.
"""

import json
from solid_node.node import AssemblyNode
from simulation.arithmetic import calculate
from simulation.transmission import channel_values
from simulation.detents import spreading


class SymbolProbe(AssemblyNode):
    def render(self):
        return []


def probe():
    symbol = SymbolProbe()
    symbol.assemble()
    x = symbol.time
    result, turns = calculate(x, x, x, x, x, x, x)
    for counter, places, value in ((False, 11, result), (True, 6, turns)):
        channels = channel_values(places, counter)(None, None)(value, x, x, x, x, x)
        template = str(spreading(counter)(None, None)(x))
        repeats = template.count('$t')
        for channel in range(places):
            angle, setting, carry = channels[3*channel:3*channel+3]
            length = len(str(carry))
            print(json.dumps(dict(bank='turns' if counter else 'result', channel=channel,
                                  turn_chars=len(str(angle)), carry_chars=length,
                                  spread_input_repeats=repeats,
                                  spread_chars_estimate=len(template)+repeats*(length-2))), flush=True)


if __name__ == '__main__':
    probe()
