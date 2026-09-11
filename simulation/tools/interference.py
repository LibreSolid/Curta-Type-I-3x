"""Inventory source overlaps without a volume epsilon or triangle welding.

Run: python -m simulation.tools.interference
Uses the native Manifold result's status and volume. Converting a boolean result
back through Trimesh's automatic vertex welding can destroy small valid regions
at nearly coincident source faces; that conversion is deliberately unnecessary.
This is a faceted diagnostic, not an exact-kernel certification.
"""

import json
import argparse
from itertools import combinations
import manifold3d as manifold
import numpy as np

from simulation.curta import Curta


def rigid_leaves(node, path='Curta'):
    if node.rigid:
        yield path, node
    else:
        for child in node.children:
            yield from rigid_leaves(child, path + '.' + child.name)


def world_solids(root):
    """Apply the public rotation/translation operations in their actual order."""
    found = {}

    def visit(node, path, ancestors):
        operations = [*node.operations, *ancestors]
        if node.rigid and node.exact:
            shape = node.shape()
            for operation in operations:
                if hasattr(operation, 'angle'):
                    shape = shape.rotate((0, 0, 0), operation.axis, operation.angle)
                elif hasattr(operation, 'translation'):
                    shape = shape.translate(operation.translation)
                else:
                    raise TypeError(f'Unsupported placement {type(operation).__name__}')
            found[path] = shape
        else:
            for child in node.children:
                visit(child, path + '.' + child.name, operations)

    visit(root, 'Curta', [])
    return found


def inventory(root, exact=False):
    meshes = {path: node.mesh for path, node in rigid_leaves(root)}
    bounds = {path: mesh.bounds for path, mesh in meshes.items()}
    solids, overlaps, refusals = {}, {}, {}
    native = world_solids(root) if exact else {}
    contact_sums = {}

    def solid(path):
        if path not in solids:
            mesh = meshes[path]
            value = manifold.Manifold(manifold.Mesh(
                np.asarray(mesh.vertices, dtype=np.float32),
                np.asarray(mesh.faces, dtype=np.uint32)))
            if value.status() != manifold.Error.NoError:
                raise ValueError(f'{path}: {value.status()}')
            solids[path] = value
        return solids[path]

    for first, second in combinations(meshes, 2):
        a, b = bounds[first], bounds[second]
        if not np.all(np.minimum(a[1], b[1]) > np.maximum(a[0], b[0])):
            continue
        key = first + ' / ' + second
        try:
            if first in native and second in native:
                overlap = native[first].intersect(native[second])
                if not overlap.isValid():
                    raise ValueError('Invalid OCCT intersection')
                volume = overlap.Volume()
            else:
                overlap = solid(first) ^ solid(second)
                if overlap.status() != manifold.Error.NoError:
                    raise ValueError(str(overlap.status()))
                volume = overlap.volume()
            if volume > 0:
                overlaps[key] = volume
            elif volume < 0:
                # Preserve these signed sums as diagnostics. No positive volume
                # is suppressed, however small; invalid results are refused above.
                contact_sums[key] = volume
        except ValueError as error:
            refusals[key] = str(error)
    return {'rigid_occurrences': len(meshes),
            'kernel': 'OCCT with source-STL interfaces' if exact else 'Manifold, faceted',
            'overlap_mm3': overlaps, 'refusals': refusals,
            'nonpositive_contact_sums_mm3': contact_sums}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact', action='store_true')
    args = parser.parse_args()
    root = Curta()
    root.set_state(time=0, operand=0, crank_turns=0, initial_result=0,
                   initial_turns=0, subtract=0, carriage_position=0, clear=0)
    root.assemble()
    root.build_stls()
    print(json.dumps(inventory(root, exact=args.exact), indent=2))
