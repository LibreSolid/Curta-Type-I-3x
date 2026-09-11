"""Reproduce the STEP product measurements used by this simulation.

Run from the project: python -m simulation.tools.probe
Prints JSON; no geometry is repaired and no upstream files are written.
"""

import inspect
import json

import numpy as np
import trimesh
from solid_node.node.adapters.step import StepAssembly

from simulation.standard import parts
from simulation.source import SOURCE, STEP, prepare


def measure(shape):
    bounds = shape.BoundingBox()
    return {
        "valid": shape.isValid(),
        "solids": len(shape.Solids()),
        "volume_mm3": shape.Volume(),
        "center_mm": shape.Center().toTuple(),
        "bounds_mm": [[bounds.xmin, bounds.ymin, bounds.zmin],
                      [bounds.xmax, bounds.ymax, bounds.zmax]],
    }


def probe():
    report = {"renamed_products": prepare(), "products": {}}
    for name, cls in inspect.getmembers(parts, inspect.isclass):
        if cls.__module__ != parts.__name__ or cls is parts.SourcePart:
            continue
        shape = cls().shape()
        reading = measure(shape)
        if not reading["valid"]:
            reading["automatic_fix_diagnostic_only"] = measure(shape.fix())
        report["products"][cls.part] = reading
    return report


def cover_interface():
    """Diagnose the housing interface on STEP and the author's print meshes."""
    source = StepAssembly(STEP)
    solids, meshes = [], []
    for cls in (parts.DigitsCover, parts.UpperHousing):
        occurrence = next(item for item in source.occurrences
                          if item.product_name == cls.part)
        # These two products are directly placed in a carriage at identity.
        # Refuse a changed hierarchy instead of silently dropping an ancestor.
        assert np.allclose(occurrence.world_matrix, occurrence.matrix)
        solid = cls().shape().rotate((0, 0, 0), occurrence.axis,
                                     occurrence.angle_deg)
        solids.append(solid.translate(occurrence.translation))
        path = (SOURCE.parents[1] / "STLs" /
                "42 - Digit Cover & Upper Housing" / f"{cls.part}.stl")
        mesh = trimesh.load_mesh(path)
        mesh.apply_transform(occurrence.world_matrix)
        meshes.append(mesh)
    intersection = solids[0].intersect(solids[1])
    faceted = trimesh.boolean.intersection(meshes, engine="manifold")
    return {
        "step_inputs_valid": [item.isValid() for item in solids],
        "step_result_valid": intersection.isValid(),
        "step_result_signed_volume_mm3": intersection.Volume(),
        "step_result_solids": len(intersection.Solids()),
        "stl_inputs_watertight": [item.is_watertight for item in meshes],
        "stl_result_watertight": faceted.is_watertight,
        "stl_result_signed_volume_mm3": faceted.volume,
        "interpretation": "Invalid boolean results are not certified overlap volumes.",
    }


if __name__ == "__main__":
    report = probe()
    report["cover_interface"] = cover_interface()
    print(json.dumps(report, indent=2))
