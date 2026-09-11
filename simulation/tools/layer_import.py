"""Emit an apply_patch adding educational layers from the source scaffold.

One-time mechanical reorganization: copy declarations and their unchanged
placement statements, not geometry. Refuse missing or multiply-owned members.
The raw scaffold remains the independent placement reference.
"""

import ast
from collections import defaultdict
from pathlib import Path
from math import atan2, degrees

SOURCE = Path(__file__).resolve().parents[1] / 'standard/assembly.py'
TARGET = SOURCE.parent / 'layers.py'
TREE = ast.parse(SOURCE.read_text())
CLASSES = {node.name: node for node in TREE.body if isinstance(node, ast.ClassDef)}
GROUPS = defaultdict(list)
TAKEN = set()


def members(owner):
    return {node.targets[0].id: node for node in CLASSES[owner].body
            if isinstance(node, ast.Assign)}


def take(group, owner, names):
    for name in names:
        assert name in members(owner), (owner, name)
        assert (owner, name) not in TAKEN, (owner, name)
        TAKEN.add((owner, name))
        GROUPS[group].append((owner, name))


def matching(group, owner, prefix):
    take(group, owner, [name for name in members(owner) if name.startswith(prefix)])


def rest(group, owner):
    take(group, owner, [name for name in members(owner) if (owner, name) not in TAKEN])


def emit():
    root, lower, upper, carriage = 'CurtaAssembly', 'LowerFrame1', 'UpperFrame1', 'Carriage1'
    # Whole source groups split below, so none of their children is duplicated.
    for name in ('lower_frame_1', 'upper_frame_1', 'carriage_1'):
        TAKEN.add((root, name))
    matching('InputSelectors', root, 'digit_selector_axle_')
    matching('InputBearings', root, 'selector_shaft_bearing_')
    matching('InputBearings', root, 'setting_axle_holding_plate_')
    take('InputBearings', root, [f'm4x10_419010_{i}' for i in range(2, 6)])
    matching('Transmission', root, 'p_102')
    matching('ResultCarry', root, 'results_tens_lever_assembly_')
    matching('TurnsCarry', root, 'turns_tens_lever_assembly_')
    matching('CarryPivots', root, 'm4x16_hex_')
    matching('DecimalMarkers', root, 'decimal_marker_')
    take('CrankAssembly', root, ['crank_handle_1', 'crank_handle_pin'])
    take('DrumAssembly', lower, ['main_axle_step_drum_1'])
    take('AntiReversal', lower, ['anti_reversal_spring', 'anti_reversal_m5_bolt_sleeve',
                               'reverse_rotation_prevention_pawl', 'm5x15_hex_bolt_2'])
    take('LowerBearingPlate', lower, ['bearing_plate', 'bearing_plate_screw', 'reverse_nose_plate'])
    rest('ZeroPositioning', lower)
    take('TensBellAssembly', upper, ['tens_bell_1', 'tens_bell_spring',
                                   'tens_bell_c_clip', 'retaining_ring_for_tens_bell'])
    rest('UpperFrame', upper)
    take('CarriagePositioning', root, ['thrust_ring', 'carriage_spring_sleeve',
                                     'carriage_spring', 'spring_sleeve_c_clip',
                                     'p_6mm_ball_419094'])
    take('ReversingAssembly', root, ['reversing_lever_1'])
    take('Enclosure', root, ['cover_ring', 'upper_outer_sleeve', 'lower_housing_1',
                             'base_plate', 'm4x10_419010_6',
                             'm5x30_countersunk_1', 'm5x30_countersunk_2'])
    matching('Enclosure', root, 'm3x10_')
    take('ClearingAssembly', root, ['m4x10_419010_1'])
    rest('FrameFasteners', root)
    # The source dial groups retain their carry pins and exact individual frames.
    for name, declaration in members(carriage).items():
        kind = declaration.value.func.id
        if name.startswith('p_102') or name.startswith('results_dial'):
            owner = kind if name.startswith('p_102') else carriage
            dial = next((key for key, node in members(owner).items()
                         if node.value.func.id.startswith('ResultsDial')), name)
            if owner == carriage:
                dial = name
            render = next(node for node in CLASSES[owner].body
                          if isinstance(node, ast.FunctionDef) and node.name == 'render')
            move = next(node.value for node in render.body
                        if ast.unparse(node).startswith(f'self.{dial}.translate('))
            x, y, _ = ast.literal_eval(move.args[0])
            # The two 30-degree gaps separate the 11-result and 6-turns banks.
            group = 'TurnsRegister' if 20 < degrees(atan2(y, x)) < 150 else 'ResultRegister'
        elif name.startswith('p_6mm_ball') or name == 'spider_spring':
            group = 'RegisterDetents'
        elif name in ('digits_cover', 'upper_housing', 'clearing_cover'):
            group = 'CarriageCovers'
        elif name.startswith('clearing_'):
            group = 'ClearingAssembly'
        else:
            group = 'CarriageStructure'
        take(group, carriage, [name])
    assert len(GROUPS['ResultRegister']) == 11
    assert len(GROUPS['TurnsRegister']) == 6

    lines = ['"""Source placements reorganized into independently visible teaching layers.',
             '', 'Generated by tools/layer_import.py; geometry stays in standard.parts.',
             'The raw standard.assembly remains the independent STEP placement map.',
             '"""', 'from solid_node.node import AssemblyNode',
             'from .assembly import *', 'from .parts import *', '']
    for group, selected in GROUPS.items():
        lines.append(f'class {group}(AssemblyNode):')
        seen = set()
        placement = []
        for owner, name in selected:
            assert name not in seen, (group, name)
            seen.add(name)
            lines.append('    ' + ast.unparse(members(owner)[name]))
            render = next((n for n in CLASSES[owner].body
                           if isinstance(n, ast.FunctionDef) and n.name == 'render'), None)
            if render:
                for statement in render.body:
                    if ast.unparse(statement).startswith(f'self.{name}.'):
                        placement.append('        ' + ast.unparse(statement))
        if placement:
            lines.extend(['', '    def render(self):', *placement])
        lines.extend(['', ''])
    # Explicit ownership is exhaustive for each decomposed source assembly.
    for owner in (root, lower, upper, carriage):
        assert all((owner, name) in TAKEN for name in members(owner))
    print('*** Begin Patch')
    print(f'*** Add File: {TARGET}')
    print('\n'.join('+' + line for line in '\n'.join(lines).rstrip().splitlines()))
    print('*** End Patch')


if __name__ == '__main__':
    emit()
