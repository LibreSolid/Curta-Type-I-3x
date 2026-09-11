"""Locate cover contacts before choosing a bounded builder-style fit.

Measurements are in the operating machine's world frame, reconstructing the
unfitted covers and axle independently of the currently installed cover fits.
The probe reports positive contacts; none is accepted by a volume threshold.
"""

import json
import numpy as np
import trimesh
from simulation.curta import Curta
from simulation.tools.carry_phase import solid
from simulation.tools.moving_seats import world_frames
from simulation.tools.interference import rigid_leaves
from simulation.standard.parts import DigitsAxle


def extent(body):
    points = body.to_mesh().vert_properties[:, :3]
    if not len(points):
        return None
    radii = np.linalg.norm(points[:, :2], axis=1)
    return dict(bounds_mm=[points.min(axis=0).tolist(), points.max(axis=0).tolist()],
                radial_mm=[float(radii.min()), float(radii.max())])


def probe():
    root = Curta()
    root.set_state(**root.instructions['Rest'].targets)
    root.assemble()
    root.build_stls()
    carriage = root.carriage.registers
    nodes = dict(digits=carriage.covers.digits_cover,
                 housing=carriage.covers.upper_housing,
                 ring=carriage.clearing_ring.clearing_cover,
                 axle=carriage.carrier.upper_carriage_body_1.digits_axle_1)
    frames = world_frames(root)
    meshes = {name: node.mesh for name, node in nodes.items()}
    for name, path in (('digits', 'covers.digits_cover'), ('housing', 'covers.upper_housing')):
        meshes[name] = trimesh.load_mesh(nodes[name].stl_source)
        meshes[name].apply_transform(frames['Curta.carriage.registers.' + path])
    raw_axle = DigitsAxle()
    raw_axle.assemble()
    raw_axle.build_stls()
    meshes['axle'] = raw_axle.mesh
    frame = frames['Curta.carriage.registers.carrier.upper_carriage_body_1.digits_axle_1']
    meshes['axle'].apply_transform(frame)
    bodies = {name: solid(mesh) for name, mesh in meshes.items()}
    for name, body in bodies.items():
        print(json.dumps(dict(part=name, **extent(body))), flush=True)
    for first, second in (('digits', 'ring'), ('digits', 'axle'),
                          ('housing', 'axle'), ('digits', 'housing')):
        contact = bodies[first] ^ bodies[second]
        print(json.dumps(dict(pair=[first, second], volume_mm3=contact.volume(),
                              contact=extent(contact))), flush=True)
    for height in (-.1, -.05, 0, .05, .1, .15, .2):
        moved = bodies['ring'].translate((0, 0, height))
        print(json.dumps(dict(ring_lift_mm=height,
                              digit_cover_overlap_mm3=(moved ^ bodies['digits']).volume())), flush=True)

    # Keep the source pin's D-flat intact while checking whether placement alone
    # can seat its outer end. Local +Z is inward along the axle, not machine Z.
    for roll in (0, 90, 180, 270):
        for inward in (0, .1, .2, .5, 1, 2):
            local = trimesh.transformations.rotation_matrix(np.radians(roll), (0, 0, 1))
            local[2, 3] = inward
            moved = meshes['axle'].copy()
            moved.apply_transform(frame @ local @ np.linalg.inv(frame))
            pin = solid(moved)
            print(json.dumps(dict(axle_roll_deg=roll, axle_inward_mm=inward,
                                  digit_cover_overlap_mm3=(pin ^ bodies['digits']).volume(),
                                  housing_overlap_mm3=(pin ^ bodies['housing']).volume())), flush=True)

    for inward in (0, 1.6, 1.7, 1.8, 2):
        pin = bodies['axle'].translate(tuple(frame[:3, 2] * inward))
        contacts = {}
        for path, node in rigid_leaves(carriage):
            if node is nodes['axle']:
                continue
            if node is nodes['digits']:
                neighbour = bodies['digits']
            elif node is nodes['housing']:
                neighbour = bodies['housing']
            else:
                neighbour = solid(node.mesh)
            overlap = (pin ^ neighbour).volume()
            if overlap > 0:
                contacts[path] = overlap
        print(json.dumps(dict(axle_inward_mm=inward, carriage_overlaps_mm3=contacts)), flush=True)


if __name__ == '__main__':
    probe()
