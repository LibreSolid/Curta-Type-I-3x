"""Measure actual shared expressions without building the calculator's CAD.

A short symbolic time token stands in for each root driver. The counts describe
standalone law emissions, not export size or peak memory. On expression-graph
frameworks str() emits a self-contained binding closure; counting token repeats
and multiplying text lengths no longer measures the emitted expression.
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
        spread = spreading(counter)(None, None)
        for channel in range(places):
            angle, setting, carry = channels[3*channel:3*channel+3]
            print(json.dumps(dict(bank='turns' if counter else 'result', channel=channel,
                                  turn_chars=len(str(angle)), carry_chars=len(str(carry)),
                                  spread_chars=len(str(spread(carry))))), flush=True)


if __name__ == '__main__':
    probe()
