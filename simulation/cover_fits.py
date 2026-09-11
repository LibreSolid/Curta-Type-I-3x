"""Measured carriage-cover fits; no upstream print or STEP file is edited.

The covers keep their corrected datum, dial windows and threaded joint. The
clearing ring, axle bearings and carrier keep their already-tested placements.
See docs/measurements.md for the rejected axle translations and local contacts.
"""

import cadquery as cq
import manifold3d as manifold
import numpy as np
import trimesh
from solid_node.parameters import Length
from simulation.print_parts import DigitsCover, UpperHousing
from simulation.standard.parts import DigitsAxle
from simulation.clearing_stop_spring import ClearingPinCarrier

SEAT_GAP = .05
# Measured in the recentered carriage, from the seventeen source axle axes.
AXLE_ANGLES = (*range(0, -181, -20), 160, *range(130, 29, -20))


def mesh_solid(mesh):
    # Keep source coordinates in double precision until the final STL write.
    body = manifold.Manifold(manifold.Mesh64(
        np.asarray(mesh.vertices, dtype=np.float64), np.asarray(mesh.faces, dtype=np.uint64)))
    if body.status() != manifold.Error.NoError:
        raise ValueError(f'Invalid source cover: {body.status()}')
    return body


def fitted_mesh(body):
    if body.status() != manifold.Error.NoError:
        raise ValueError(f'Invalid cover fit: {body.status()}')
    mesh = body.to_mesh64()
    return trimesh.Trimesh(vertices=mesh.vert_properties[:, :3], faces=mesh.tri_verts, process=False)


class FittedDigitsCover(DigitsCover):
    """Face .10 mm off the inner top land, leaving .05 mm below the ring."""
    rim_relief = Length(.1, min=0)

    def adjust(self, mesh):
        # Local -Z is upward. The ring's R61.5 underside is world Z43.6;
        # this land starts at 43.65. Neither clearing groove nor window moves.
        tool = manifold.Manifold.cylinder(self.rim_relief + SEAT_GAP, 61.5 + SEAT_GAP,
                                          circular_segments=360).translate((0, 0, -12-SEAT_GAP))
        return fitted_mesh(mesh_solid(mesh) - tool)


class FittedUpperHousing(UpperHousing):
    """Seventeen shallow axle-end pockets in the inner lower seating flange."""
    seat_gap = Length(SEAT_GAP, min=0)

    def adjust(self, mesh):
        body = mesh_solid(mesh)
        # Axles are R2.945 at world Z33.9, outer ends on R73.574057463.
        # Housing local Z = world Z + 4.35 and its installed clocking is 160°.
        # The 2 mm tools span R71.65..73.65, not the outer threaded wall.
        pocket = manifold.Manifold.cylinder(2, 2.945+self.seat_gap, circular_segments=128)
        # Half a facet avoids a cutter edge coincident with an original radial
        # seam, which otherwise leaves zero-thickness fins on STL conversion.
        pocket = pocket.rotate((0, 0, 180/128)).rotate((0, 90, 0)).translate((71.65, 0, 38.25))
        for angle in AXLE_ANGLES:
            body = body - pocket.rotate((0, 0, angle-160))
        return fitted_mesh(body)


class FittedDigitsAxle(DigitsAxle):
    """Extend the outer retaining flat .15 mm; keep the entire 54 mm bearing."""
    flat_extension = Length(.15, min=0)

    def adjust(self, shape):
        tool = cq.Solid.makeBox(3.1, 6, 1.8+self.flat_extension, cq.Vector(-4, -3, 0))
        return shape.cut(tool)


class FittedAxleCarrier(ClearingPinCarrier):
    digits_axle_1 = FittedDigitsAxle()
    digits_axle_2 = FittedDigitsAxle()
    digits_axle_3 = FittedDigitsAxle()
    digits_axle_4 = FittedDigitsAxle()
    digits_axle_5 = FittedDigitsAxle()
    digits_axle_6 = FittedDigitsAxle()
    digits_axle_7 = FittedDigitsAxle()
    digits_axle_8 = FittedDigitsAxle()
    digits_axle_9 = FittedDigitsAxle()
    digits_axle_10 = FittedDigitsAxle()
    digits_axle_11 = FittedDigitsAxle()
    digits_axle_12 = FittedDigitsAxle()
    digits_axle_13 = FittedDigitsAxle()
    digits_axle_14 = FittedDigitsAxle()
    digits_axle_15 = FittedDigitsAxle()
    digits_axle_16 = FittedDigitsAxle()
    digits_axle_17 = FittedDigitsAxle()
