import { test } from 'node:test';
import assert from 'node:assert/strict';
import { Calculator, calculate } from './calculator.mjs';
import { readFileSync } from 'node:fs';

const zero = { operand: 0, crank_turns: 0, initial_result: 0, initial_turns: 0,
  subtract: 0, carriage_position: 0, carriage_lift: 0, clear: 0 };

test('author calibration and committed operations retain both registers', () => {
  const state = { ...zero };
  const model = { driver: id => state[id], setDriver: (id, value) => { state[id] = value; } };
  const calculator = new Calculator(model);
  for (const [operand, result, turns] of [[0, 0, 1], [1, 1, 2], [9, 10, 3], [90, 100, 4]]) {
    model.setDriver('operand', operand);
    model.setDriver('crank_turns', 1);
    assert.deepEqual(calculator.preview(), { result, turns });
    calculator.commit();
    assert.equal(state.crank_turns, 0);
    assert.deepEqual(calculator.preview(), { result, turns });
  }
});

test('multiplication, decimal shift, subtraction, clearing and overflow', () => {
  assert.deepEqual(calculate({ ...zero, operand: 123, crank_turns: 4 }), { result: 492, turns: 4 });
  assert.deepEqual(calculate({ ...zero, initial_result: 492, initial_turns: 4,
    operand: 123, crank_turns: 2, carriage_position: 1 }), { result: 2952, turns: 24 });
  assert.deepEqual(calculate({ ...zero, initial_result: 1, initial_turns: 1,
    operand: 1, crank_turns: 1, subtract: 1 }), { result: 0, turns: 0 });
  assert.deepEqual(calculate({ ...zero, initial_result: 99999999999, initial_turns: 999999,
    operand: 1, crank_turns: 1 }), { result: 0, turns: 0 });
  assert.deepEqual(calculate({ ...zero, initial_result: 123, initial_turns: 9, clear: 1 }), { result: 0, turns: 0 });
});

test('partial turns can be inspected but cannot silently commit', () => {
  const state = { ...zero, operand: 9, crank_turns: .5 };
  const calculator = new Calculator({ driver: id => state[id], setDriver() {} });
  assert.throws(() => calculator.commit(), /complete crank/);
});

test('a calculation cannot be committed with the carriage lifted or between detents', () => {
  const state = { ...zero, operand: 9, crank_turns: 1, carriage_lift: 1 };
  const calculator = new Calculator({ driver: id => state[id], setDriver() {} });
  assert.throws(() => calculator.commit(), /reseat/i);
  state.carriage_lift = 0;
  state.carriage_position = 1.5;
  assert.throws(() => calculator.commit(), /detent/i);
});

test('worked examples calculate their stated answers and lift before shifting', () => {
  const examples = JSON.parse(readFileSync(new URL('./examples.json', import.meta.url)));
  assert.equal(examples.length, 6);
  for (const example of examples) {
    const state = { ...zero, ...example.start };
    for (const move of example.moves) {
      if (move.driver === 'carriage_position') assert.equal(state.carriage_lift, 1);
      if (move.driver === 'crank_turns') assert.equal(state.carriage_lift, 0);
      state[move.driver] = move.target;
    }
    assert.deepEqual(calculate(state), example.expected, example.title);
  }
});
