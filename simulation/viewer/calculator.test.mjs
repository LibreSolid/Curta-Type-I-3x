import { test } from 'node:test';
import assert from 'node:assert/strict';
import { Calculator, calculate } from './calculator.mjs';

const zero = { operand: 0, crank_turns: 0, initial_result: 0, initial_turns: 0,
  subtract: 0, carriage_position: 0, clear: 0 };

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
