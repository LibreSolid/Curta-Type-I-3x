"""Read the flat clearing-strip prints and the cover's cylindrical seats."""

from pathlib import Path
import json
import numpy as np
import trimesh
from OCP.BRepAdaptor import BRepAdaptor_Surface
from simulation.print_parts import PRINTS
from simulation.standard.parts import ClearingCover


def probe():
    shape = ClearingCover().shape()
    for face in shape.Faces():
        if face.geomType() == 'CYLINDER':
            cylinder = BRepAdaptor_Surface(face.wrapped).Cylinder()
            point = cylinder.Axis().Location()
            print(json.dumps({'radius': cylinder.Radius(),
                'axis_point': [point.X(), point.Y(), point.Z()],
                'z': [face.BoundingBox().zmin, face.BoundingBox().zmax]}))
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 1, figsize=(14, 5), constrained_layout=True)
    for ax, name in zip(axes, ('clearing cap teeth x2.stl',
                              'clearing cap tooth segment spacer.stl')):
        mesh = trimesh.load_mesh(PRINTS / '37 - Clearing Cover' / name)
        print(json.dumps({'file': name, 'bounds': mesh.bounds.tolist(),
                          'watertight': mesh.is_watertight, 'volume': mesh.volume,
                          'bodies': len(mesh.split())}))
        # Show the source's flat print plane; no repair or change to its mesh.
        for triangle in mesh.triangles:
            if np.ptp(triangle[:, 2]) == 0 and triangle[0, 2] == 0:
                loop = np.vstack((triangle, triangle[0]))
                ax.plot(loop[:, 1], -loop[:, 0], color='#29546e', linewidth=.2)
        ax.set_title(name)
        ax.set_xlabel('Source Y (mm)')
        ax.set_ylabel('−source X (mm)')
        ax.set_aspect('equal')
        ax.grid(alpha=.2)
    fig.savefig(Path('_build_evidence/clearing-flat-profiles.png'), dpi=140)


if __name__ == '__main__':
    probe()
