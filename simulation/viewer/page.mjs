import { Calculator } from './calculator.mjs';

const $ = id => document.getElementById(id);
const status = text => { $('status').textContent = text; };
const names = ['ones', 'tens', 'hundreds', 'thousands', 'ten thousands',
  'hundred thousands', 'millions', 'ten millions'];

async function main() {
  if (!globalThis.SolidNodeWidget || SolidNodeWidget.apiVersion < 7)
    throw new Error('Export this project with the current solid-node viewer before opening this page.');
  const viewer = await SolidNodeWidget.mount('#model', '../../_build_export/manifest.json', {
    driverControls: 'none', up: [0, 0, 1], fov: 30,
  });
  const calculator = new Calculator(viewer);
  let cancelAnimation = null;
  const hidden = new Map();
  const visibility = new Map();

  function show(path, visible) {
    viewer.setVisible(path, visible);
    const key = JSON.stringify(path);
    if (visible) hidden.delete(key); else hidden.set(key, path);
    if (visibility.has(key)) visibility.get(key).checked = visible;
  }

  function tree(node, parent) {
    const container = document.createElement(node.children.length ? 'details' : 'div');
    const row = document.createElement(node.children.length ? 'summary' : 'div');
    row.className = 'node';
    const check = document.createElement('input');
    check.type = 'checkbox'; check.checked = true;
    check.setAttribute('aria-label', `Show ${node.name.replaceAll('_', ' ')}`);
    check.onclick = event => event.stopPropagation();
    check.onchange = () => show(node.path, check.checked);
    visibility.set(JSON.stringify(node.path), check);
    const focus = document.createElement('button');
    focus.textContent = node.name.replaceAll('_', ' ');
    focus.title = 'Focus this assembly';
    focus.onclick = event => { event.preventDefault(); viewer.setRoot(node.path); };
    row.append(check, focus); container.append(row); parent.append(container);
    node.children.forEach(child => tree(child, container));
  }
  viewer.assembly().children.forEach(node => tree(node, $('layers')));

  function set(id, value) {
    viewer.setDriver(id, value);
    status('Preview is reproducible from the starting registers. Complete and keep a turn to continue calculating.');
  }

  const digits = [];
  for (let place = 7; place >= 0; place--) {
    const label = document.createElement('label'); label.className = 'digit';
    const value = document.createElement('output');
    const slider = document.createElement('input');
    Object.assign(slider, { type: 'range', min: '0', max: '9', step: '1', value: '0' });
    slider.setAttribute('aria-label', `Input ${names[place]}`);
    slider.oninput = () => {
      const operand = viewer.driver('operand');
      const previous = Math.floor(operand / 10 ** place) % 10;
      set('operand', operand + (Number(slider.value) - previous) * 10 ** place);
    };
    const caption = document.createElement('small'); caption.textContent = `10${'⁰¹²³⁴⁵⁶⁷'[place]}`;
    label.append(value, slider, caption); $('digits').append(label);
    digits.push({ place, value, slider });
  }

  function refresh() {
    const state = calculator.state();
    const result = calculator.preview();
    $('result').textContent = String(result.result).padStart(11, '0');
    $('turns').textContent = String(result.turns).padStart(6, '0');
    $('operand').value = state.operand;
    $('initial-result').value = state.initial_result;
    $('initial-turns').value = state.initial_turns;
    $('subtract').checked = Boolean(state.subtract);
    $('shift').value = state.carriage_position;
    $('shift-value').textContent = `${state.carriage_position + 1} · ×${10 ** state.carriage_position}`;
    $('crank').value = state.crank_turns;
    $('crank-value').textContent = `${state.crank_turns.toFixed(3)} turns`;
    $('commit').disabled = !Number.isInteger(state.crank_turns) || state.crank_turns === 0;
    $('clear').disabled = !Number.isInteger(state.crank_turns);
    $('turn').disabled = state.clear > 0;
    $('clear').textContent = state.clear > 0 && state.clear < 1 ? 'Finish clearing' : 'Clear both registers';
    for (const item of digits) {
      item.slider.value = Math.floor(state.operand / 10 ** item.place) % 10;
      item.value.textContent = item.slider.value;
    }
  }

  for (const [id, driver] of [['operand', 'operand'], ['initial-result', 'initial_result'],
    ['initial-turns', 'initial_turns']]) {
    $(id).onchange = () => {
      if ($(id).reportValidity()) set(driver, Number($(id).value));
    };
  }
  $('subtract').onchange = () => set('subtract', Number($('subtract').checked));
  $('shift').oninput = () => set('carriage_position', Number($('shift').value));
  $('crank').oninput = () => set('crank_turns', Number($('crank').value));
  $('repeat').onchange = () => {
    if ($('repeat').reportValidity()) $('crank').max = $('repeat').value;
  };

  function animate(driver, target, seconds, finish) {
    const start = viewer.driver(driver), started = performance.now();
    let stopped = false;
    $('controls').disabled = true; $('pause').hidden = false;
    cancelAnimation = () => {
      stopped = true; cancelAnimation = null;
      $('controls').disabled = false; $('pause').hidden = true;
      status(driver === 'clear' ? 'Paused. Press Finish clearing to continue.' :
        'Paused. Inspect the mechanism or press Turn crank to finish.');
    };
    function frame(now) {
      if (stopped) return;
      const progress = Math.min(1, (now - started) / (seconds * 1000));
      viewer.setDriver(driver, progress === 1 ? target : start + (target - start) * progress);
      if (progress < 1) requestAnimationFrame(frame);
      else {
        cancelAnimation = null; $('controls').disabled = false; $('pause').hidden = true;
        finish(); refresh();
      }
    }
    requestAnimationFrame(frame);
  }

  $('turn').onclick = () => {
    if (!$('repeat').reportValidity()) return;
    const current = viewer.driver('crank_turns');
    const target = Math.max(Number($('repeat').value), Math.floor(current) + 1);
    if (target > 12) { status('Keep the completed turns before beginning another operation.'); return; }
    $('crank').max = target;
    status('Turning the crank. Pause at any point to inspect the mechanism.');
    animate('crank_turns', target, (target - current) * Number($('duration').value), () => {
      calculator.commit(); status('Operation kept. Set the next input, shift the carriage, or turn again.');
    });
  };
  $('pause').onclick = () => cancelAnimation?.();
  $('commit').onclick = () => { calculator.commit(); status('Completed turns kept in this page.'); };
  $('clear').onclick = () => {
    status('Clearing both registers.');
    animate('clear', 1, 3, () => { calculator.commit(); status('Both registers cleared. Input selectors are unchanged.'); });
  };
  $('inside').onclick = () => {
    viewer.setRoot(null);
    [['enclosure'], ['frame'], ['carriage', 'registers', 'covers'],
      ['carriage', 'registers', 'carrier']].forEach(path => show(path, false));
  };
  $('outside').onclick = () => {
    for (const path of [...hidden.values()]) show(path, true);
    viewer.setRoot(null);
  };
  $('whole').onclick = () => viewer.setRoot(null);
  viewer.onDriverChange(refresh);
  refresh(); $('controls').disabled = false;
  status('Ready. Set an input and turn the crank; completed operations remain in this page.');
  // Public console handle for lessons and automated checks; no renderer internals.
  window.curta = { viewer, calculator };
}

main().catch(error => { status(`Could not open the calculator: ${error.message}`); console.error(error); });
