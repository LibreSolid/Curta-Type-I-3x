/** Session state belongs to this page; the solid-node model remains replayable. */
export const DRIVER_IDS = [
  'operand', 'crank_turns', 'initial_result', 'initial_turns',
  'subtract', 'carriage_position', 'carriage_lift', 'clear',
];

export function calculate(state) {
  const count = Math.floor(state.crank_turns);
  const scale = Array.from({ length: 6 }, (_, place) =>
    10 ** place * Math.max(0, 1 - Math.abs(state.carriage_position - place))).reduce((a, b) => a + b);
  const step = (1 - 2 * state.subtract) * scale * count;
  const wrap = (value, modulus) => ((value % modulus) + modulus) % modulus;
  return state.clear === 1 ? { result: 0, turns: 0 } : {
    result: wrap(state.initial_result + state.operand * step, 1e11),
    turns: wrap(state.initial_turns + step, 1e6),
  };
}

export class Calculator {
  constructor(viewer) { this.viewer = viewer; }
  state() { return Object.fromEntries(DRIVER_IDS.map(id => [id, this.viewer.driver(id)])); }
  preview() { return calculate(this.state()); }
  commit() {
    const state = this.state();
    if (!Number.isInteger(state.crank_turns)) throw new Error('Finish a complete crank turn before committing.');
    if (state.clear > 0 && state.clear < 1) throw new Error('Finish clearing before committing.');
    if (state.carriage_lift > 0) throw new Error('Reseat the carriage before committing a calculation.');
    if (!Number.isInteger(state.carriage_position)) throw new Error('Choose a carriage detent before committing.');
    const { result, turns } = this.preview();
    this.viewer.setDriver('initial_result', result);
    this.viewer.setDriver('initial_turns', turns);
    this.viewer.setDriver('crank_turns', 0);
    this.viewer.setDriver('clear', 0);
    return { result, turns };
  }
}
