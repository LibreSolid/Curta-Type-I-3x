"""Identify nominal overlap pairs whose relative placement changes in use.

This is a kinematic triage, not collision acceptance. Every reported moving
interface still needs a contact contract; static source fits need provenance.
"""

import json
import sys
from pathlib import Path
import numpy as np
import trimesh
from math import radians
from simulation.curta import Curta


def world_frames(root):
    frames = {}

    def visit(node, path, parent):
        local = np.eye(4)
        for operation in node.operations:
            if hasattr(operation, 'angle'):
                matrix = trimesh.transformations.rotation_matrix(radians(operation.angle), operation.axis)
            elif hasattr(operation, 'translation'):
                matrix = np.eye(4)
                matrix[:3, 3] = operation.translation
            else:
                raise TypeError(type(operation).__name__)
            local = matrix @ local
        world = parent @ local
        if node.rigid:
            frames[path] = world
        else:
            for child in node.children:
                visit(child, path + '.' + child.name, world)

    visit(root, 'Curta', np.eye(4))
    return frames


def probe(path):
    log = Path(path).read_text()
    source = json.loads(log[log.index('\n{')+1:] if '\n{' in log else log)
    pairs = {tuple(pair.split(' / ')): volume for pair, volume in source['overlap_mm3'].items()}
    root = Curta()
    rest = root.instructions['Rest'].targets
    root.set_state(**rest)
    root.assemble()
    frames = world_frames(root)
    initial = {pair: np.linalg.inv(frames[pair[0]]) @ frames[pair[1]] for pair in pairs}
    changes = {pair: (0, None) for pair in pairs}
    poses = [('input', dict(operand=98765432))]
    poses.extend((f'crank {step}/12', dict(initial_result=99999999999,
                                        initial_turns=999999, operand=1, crank_turns=step/12))
                 for step in range(25))
    poses.extend((f'subtract {step}/4', dict(subtract=step/4)) for step in range(5))
    poses.extend((f'shift {step}/2', dict(carriage_lift=1, carriage_position=step/2))
                 for step in range(11))
    poses.extend((f'clear {step}/20', dict(initial_result=98765432109,
                                        initial_turns=987654, clear=step/20))
                 for step in range(21))
    for label, pose in poses:
        root.set_state(**(rest | pose))
        frames = world_frames(root)
        for pair in pairs:
            relative = np.linalg.inv(frames[pair[0]]) @ frames[pair[1]]
            change = float(np.max(np.abs(relative-initial[pair])))
            if change > changes[pair][0]:
                changes[pair] = (change, label)
    for pair, (change, pose) in changes.items():
        # Imported placement precision; never an overlap-volume epsilon.
        if change > .00001:
            print(json.dumps(dict(pair=' / '.join(pair), overlap_mm3=pairs[pair],
                                  relative_matrix_change=change, witness=pose)), flush=True)


if __name__ == '__main__':
    probe(sys.argv[1])
