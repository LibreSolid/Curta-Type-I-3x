"""Sample the admissible pinion phase during one drum-tooth passage.

This faceted search discovers a candidate law; the native contact contract,
not this search, decides whether the candidate can be used by the simulation.
"""

import json
import argparse
import manifold3d as manifold
import numpy as np
import trimesh
from simulation.standard.parts import OneToothStepDrumSegment, TransmissionGear0_5


def solid(node):
    vertices, triangles = node.shape().tessellate(0.01, 0.05)
    mesh = trimesh.Trimesh([vertex.toTuple() for vertex in vertices], triangles)
    value = manifold.Manifold(manifold.Mesh(
        np.asarray(mesh.vertices, dtype=np.float32),
        np.asarray(mesh.faces, dtype=np.uint32)))
    assert value.status() == manifold.Error.NoError
    return value


def probe(relief=0):
    tooth = solid(OneToothStepDrumSegment()).rotate((0, 0, 170.104082802))
    tooth = tooth.translate((0, 0, -70.8))
    gear_node = TransmissionGear0_5()
    if relief:
        from simulation.tools.input_fit import relieved
        class Sample:
            def shape(self):
                return relieved(gear_node.shape(), relief)
        gear = solid(Sample())
    else:
        gear = solid(gear_node)
    phases = np.arange(-18, 90.01, 0.5)
    gears = [gear.rotate((0, 0, phase)).translate((40.5, 0, -70.92499975))
             for phase in phases]
    for angle in range(100, 141):
        a = tooth.rotate((0, 0, -angle))
        volumes = []
        for b in gears:
            result = a ^ b
            assert result.status() == manifold.Error.NoError
            volumes.append(max(0, result.volume()))
        free = [phase for phase, volume in zip(phases, volumes) if volume == 0]
        print(json.dumps({'crank': angle, 'free': free,
                          'minimum_mm3': min(volumes),
                          'minimum_phase': float(phases[np.argmin(volumes)])}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--relief', type=float, default=0)
    probe(parser.parse_args().relief)
