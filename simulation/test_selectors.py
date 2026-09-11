"""Every input digit changes its own channel, with the other axes stationary."""

import numpy as np
from solid_node.test import TestCase
from simulation.selectors import SelectorBank


class SelectorBankTest(TestCase):
    node = SelectorBank

    def test_decimal_input_travels(self):
        machine = self.node
        machine.set_state(input_number=0)
        bank = machine
        knobs = [next(child for child in selector.children
                      if child.name.startswith('selector_knob'))
                 for selector in bank.children]
        before = [knob.children[-1].mesh.vertices.copy() for knob in knobs]
        machine.set_state(input_number=12345678)
        for selector, knob, vertices in zip(bank.children, knobs, before):
            # Source placement identifies decimal order independently of STEP names.
            shaft = selector.selector_shaft_bottom
            x, y, _ = shaft.mesh.vertices.mean(axis=0)
            place = round(-np.degrees(np.arctan2(y, x)) / 20)
            digit = 12345678 // 10 ** place % 10
            self.assertEqual(selector.setting.value, digit)
            actual = knob.children[-1].mesh.vertices
            self.assertLess(np.max(np.abs(actual - vertices - [0, 0, -6 * digit])), 0.00001)
