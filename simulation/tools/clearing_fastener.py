"""Measure the source screw axis and the clearing cover's retaining hole."""

import json
import numpy as np
import cadquery as cq
import matplotlib.pyplot as plt
from OCP.BRepAdaptor import BRepAdaptor_Surface
from simulation.clearing_fasteners import ClearingFastenerBench
from simulation.tools.interference import world_solids
from simulation.tools.carry_phase import solid


def probe():
    root = ClearingFastenerBench()
    root.assemble()
    root.build_stls()
    shapes = world_solids(root)
    for name in ('m4x10_419010_1', 'clearing_cover'):
        shape = shapes['Curta.' + name]
        for face in shape.Faces():
            if face.geomType() == 'CYLINDER':
                cylinder = BRepAdaptor_Surface(face.wrapped).Cylinder()
                radius = cylinder.Radius()
                if radius > 5:
                    continue
                at, direction = cylinder.Axis().Location(), cylinder.Axis().Direction()
                print(json.dumps(dict(part=name, radius=radius, area=face.Area(),
                    at=[at.X(), at.Y(), at.Z()],
                    axis=[direction.X(), direction.Y(), direction.Z()],
                    center=face.Center().toTuple())), flush=True)
    screw = solid(root.m4x10_419010_1.mesh)
    for strip in root.tooth_stack.children:
        overlap = screw ^ solid(strip.mesh)
        bounds = overlap.bounding_box()
        print(json.dumps(dict(strip=strip.name, overlap=overlap.volume(), bounds=bounds)), flush=True)

    origin = np.array((47.68594709841183, 13.282697936004507, 49.498770926845005))
    axis = np.array((.680666453407537, .1915546374782895, .7071067812333344))
    normal = np.cross(axis, (0, 0, 1))
    normal /= np.linalg.norm(normal)
    plane = cq.Plane(tuple(origin), tuple(axis), tuple(normal))
    figure, ax = plt.subplots(figsize=(10, 7))
    for name, color in (('m4x10_419010_1', 'tab:blue'), ('clearing_cover', 'tab:gray')):
        shape = shapes['Curta.' + name]
        section = cq.Workplane(plane).add(shape).section().val()
        first = True
        for edge in section.Edges():
            points, _ = edge.sample(60)
            local = [plane.toLocalCoords(point) for point in points]
            ax.plot([p.x for p in local], [p.y for p in local], color=color,
                    label=name if first else None)
            first = False
    for strip, color in zip(root.tooth_stack.children, ('tab:orange', 'tab:green', 'tab:red')):
        section = strip.mesh.section(plane_origin=origin, plane_normal=normal)
        first = True
        for line in section.discrete:
            local = [plane.toLocalCoords(cq.Vector(*point)) for point in line]
            ax.plot([p.x for p in local], [p.y for p in local], color=color,
                    label=strip.name if first else None)
            first = False
    ax.set(xlim=(-9, 9), ylim=(-10, 8), xlabel='Along screw axis (mm)',
           ylabel='Across screw axis (mm)')
    ax.set_aspect('equal')
    ax.legend()
    ax.grid()
    figure.tight_layout()
    figure.savefig('_build_evidence/clearing-fastener-section.png', dpi=150)


if __name__ == '__main__':
    probe()
