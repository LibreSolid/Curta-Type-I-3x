"""Measure carry tooth passage independently of the candidate motion law."""

from math import radians
import json
import numpy as np
import manifold3d as manifold
import trimesh
from simulation.carry_mesh import CarryMesh


def rotation(angle, at=(0, 0, 0)):
    return trimesh.transformations.rotation_matrix(radians(angle), (0, 0, 1), at)


def solid(mesh):
    shape = manifold.Manifold(manifold.Mesh(np.asarray(mesh.vertices, dtype=np.float32),
                                           np.asarray(mesh.faces, dtype=np.uint32)))
    assert shape.status() == manifold.Error.NoError
    return shape


def probe():
    model = CarryMesh()
    model.set_state(crank_turns=0, enabled=1)
    model.assemble()
    model.build_stls()
    bell = model.bell.mesh
    for bank, home, center, at, path in [
        ('result', 140, 152, (38.057551142, -13.851815805, 0), 'p_10220_410003_1_419227'),
        ('counter', 196, 204, (-13.851815805, 38.057551142, 0), 'p_10220_410003_1_419081'),
    ]:
        model.set_state(crank_turns=home/360)
        group = getattr(getattr(model, bank), path)
        pinion = group.mesh
        tooth = group.transmission_gear_0_6.mesh
        samples = np.arange(center - 13, center + 13.01, 1)
        rings = []
        for angle in samples:
            mesh = bell.copy()
            mesh.apply_transform(rotation(-angle))
            rings.append(solid(mesh))
        results = []
        for pitch in np.arange(8, 16.01, 1):
            for end in np.arange(center + 2, center + 10.01, .5):
                volumes = []
                for angle, ring in zip(samples, rings):
                    progress = np.clip((angle - end + pitch) / pitch, 0, 1)
                    mesh = pinion.copy()
                    mesh.apply_transform(rotation(72 * progress, at))
                    overlap = ring ^ solid(mesh)
                    assert overlap.status() == manifold.Error.NoError
                    volumes.append(overlap.volume())
                blocked = []
                progress = np.clip((center - end + pitch) / pitch, 0, 1)
                for perturb in (-12, 12):
                    mesh = tooth.copy()
                    mesh.apply_transform(rotation(72 * progress + perturb, at))
                    blocked.append((rings[13] ^ solid(mesh)).volume())
                results.append(dict(bank=bank, pitch=float(pitch), end=float(end),
                                    maximum=max(volumes), min_blocked=min(blocked),
                                    total=sum(max(v, 0) for v in volumes)))
        for result in sorted(results, key=lambda item: (max(item['maximum'], 0), -item['min_blocked']))[:12]:
            print(json.dumps(result), flush=True)


if __name__ == '__main__':
    probe()
