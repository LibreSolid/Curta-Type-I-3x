"""The manual's two clearing-tooth strips and spacer, absent from the STEP."""

import numpy as np
import trimesh
import manifold3d as manifold
import cadquery as cq
from solid_node.node import AssemblyNode, StlNode
from solid_node.parameters import Length
from simulation.print_parts import PRINTS
from simulation.standard.parts import ClearingCover

GROOVE_FLOOR = 8.325  # .675 mm deeper; .05 mm above the measured zero-gap shoulder.
SEAT_GAP = .05


class ClearingGrooveCover(ClearingCover):
    # The source's coarse cylinder tessellation cuts into the .05 mm slot gap.
    # Fine tessellation preserves that gap; adjust() separately deepens the floor.
    linear_deflection = .01
    angular_deflection = .1
    groove_floor = Length(GROOVE_FLOOR)

    def adjust(self, shape):
        # Seat the rack pitch line 6.125 mm above the dial axis. Only this annular
        # floor is deepened; the walls, cover datum and fastener pattern remain.
        outer = cq.Solid.makeCylinder(52.5, 9 - self.groove_floor, cq.Vector(0, 0, self.groove_floor))
        inner = cq.Solid.makeCylinder(49.05, 9 - self.groove_floor, cq.Vector(0, 0, self.groove_floor))
        return shape.cut(outer.cut(inner))


def bend_strip(mesh, inside, thickness, back, floor, center=0, reverse=False):
    """Bend the flat print about its mid-thickness without smoothing its teeth.

    Each strip keeps its own neutral-axis length. One plate is turned over so
    its nine teeth occupy the other half of the stack, as in manual page 38.
    Only planar refinement precedes the cylindrical placement; no mesh repair.
    """
    solid = manifold.Manifold(manifold.Mesh(
        np.asarray(mesh.vertices, dtype=np.float32), np.asarray(mesh.faces, dtype=np.uint32)))
    if solid.status() != manifold.Error.NoError:
        raise ValueError(f'Invalid source clearing strip: {solid.status()}')
    refined = solid.refine_to_length(1).to_mesh()
    mesh = trimesh.Trimesh(vertices=refined.vert_properties[:, :3],
                           faces=refined.tri_verts, process=False)
    x, y, z = mesh.vertices.T.copy()
    radius = inside + (thickness - z if reverse else z)
    angle = (y - center) / (inside + thickness/2)
    if reverse:
        angle = -angle
    angle -= np.pi/2  # Register the middle to the cover's -Y screw/rivet pair.
    mesh.vertices = np.column_stack((radius*np.cos(angle), radius*np.sin(angle),
                                    floor + SEAT_GAP + back - x))
    return mesh


class RetainingScrewFit:
    """A back relief for the source retaining screw; no clearing tooth is cut."""
    retaining_bore = Length(2.15)

    def adjust(self, mesh):
        formed = self.form(mesh)
        body = manifold.Manifold(manifold.Mesh(
            np.asarray(formed.vertices, dtype=np.float32),
            np.asarray(formed.faces, dtype=np.uint32)))
        result = self.relieve(body).to_mesh()
        return trimesh.Trimesh(vertices=result.vert_properties[:, :3],
                               faces=result.tri_verts, process=False)

    def relieve(self, body):
        # Source screw in the cover frame: R 2.1 shank, 45° down/outward.
        # The extra .05 mm is a radial seating allowance, not a test epsilon.
        bore = manifold.Manifold.cylinder(8.4, self.retaining_bore, circular_segments=96)
        bore = bore.rotate((135, 0, 0)).translate((.13205562, -45.57669045, 11.52567171))
        fitted = body - bore
        if fitted.status() != manifold.Error.NoError:
            raise ValueError(f'Invalid clearing screw relief: {fitted.status()}')
        return fitted


class ClearingTeeth(RetainingScrewFit, StlNode):
    stl_source = str(PRINTS / '37 - Clearing Cover/clearing cap teeth x2.stl')
    color = '#cad1d8'
    groove_floor = Length(GROOVE_FLOOR)

    def form(self, mesh):
        return bend_strip(mesh, inside=49.1, thickness=.9, back=7.2, floor=self.groove_floor)


class OuterClearingTeeth(ClearingTeeth):
    def form(self, mesh):
        return bend_strip(mesh, inside=51.55, thickness=.9, back=7.2, floor=self.groove_floor, reverse=True)


class ClearingSpacer(RetainingScrewFit, StlNode):
    stl_source = str(PRINTS / '37 - Clearing Cover/clearing cap tooth segment spacer.stl')
    color = '#8996a4'
    groove_floor = Length(GROOVE_FLOOR)

    def form(self, mesh):
        return bend_strip(mesh, inside=50.025, thickness=1.5, back=6.9, floor=self.groove_floor, center=35.25)


class ClearingTeethStack(AssemblyNode):
    inner_teeth = ClearingTeeth()
    spacer = ClearingSpacer()
    outer_teeth = OuterClearingTeeth()


class ClearingBench(AssemblyNode):
    cover = ClearingGrooveCover()
    teeth = ClearingTeethStack()
