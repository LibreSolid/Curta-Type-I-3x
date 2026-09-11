"""Instructions must land exactly and route carriage shifts through the lift."""

import json
from pathlib import Path
from solid_node.simulation import ScenarioTest, Instruction
from simulation.demo import Demo


class DemoTest(ScenarioTest):
    node = Demo
    dt = .1
    meshes = True

    def test_worked_examples_match_the_browser_and_replay(self):
        examples = json.loads((Path(__file__).parent / 'viewer/examples.json').read_text())
        original = self.node.instructions
        rest = original['Rest'].targets
        try:
            for example in examples:
                self.node.instructions = dict(original, Setup=Instruction(
                    dict(rest, **example['start']), duration=.1))
                for replay in range(2):
                    sim = self.simulation()
                    sim.trigger('Setup')
                    sim.run(.1)
                    for move in example['moves']:
                        instruction = original[move['instruction']]
                        self.assertEqual(instruction.targets, {move['driver']: move['target']})
                        self.assertEqual(instruction.duration, move['duration'])
                        if move['driver'] == 'carriage_position':
                            self.assertEqual(sim.state['carriage_lift'], 1)
                        sim.trigger(move['instruction'])
                        sim.run(move['duration'])
                        self.assertEqual(sim.state[move['driver']], move['target'])
                    self.assertEqual(self.node.result.value, example['expected']['result'], example['title'])
                    self.assertEqual(self.node.turns_counter.value, example['expected']['turns'], example['title'])
        finally:
            self.node.instructions = original

    def test_named_moves_land_and_shift_disengaged(self):
        sim = self.simulation()
        moves = [('Rest', 1), ('Set one', 1), ('Turn crank', 6),
                 ('Lift carriage', 1), ('Shift ×10', 1), ('Seat carriage', 1),
                 ('Clear both', 3)]
        sampled = []

        def clearance():
            # The adjacent bevel interface is checked here; the full source
            # overlap inventory is a separate, still-open root contract.
            dial = self.node.carriage.registers.result_register.p_10203_1.results_dial_type_1
            tip = self.node.transmission.result.ones.p_10208_1.transmission_gear_tip
            self.assertNotIntersecting(dial, tip)
            sampled.append(sim.time)

        sim.every(.2, clearance)
        for name, duration in moves:
            sim.trigger(name)
            sim.run(duration)
            for driver, value in self.node.instructions[name].targets.items():
                self.assertEqual(sim.state[driver], value, (name, driver))
        self.assertEqual(self.node.result.value, 0)
        self.assertEqual(self.node.turns_counter.value, 0)
        self.assertEqual(len(sampled), 70)
