"""Source mounting plate and hooks, joined by measured ribbed flexible arms.

Only the long, constant-section arms are represented analytically. The STEP
keeps the holes, rounded roots and tapered hooks. Arm bending is prescribed;
this is not a stress, spring-force or inextensibility calculation.
"""

from math import radians, sin, cos, pi
import cadquery as cq
from molejo import Shape, Polygon, Line, Spline, P
from solid_node.node import AssemblyNode, MolejoNode
from solid_node.motion.ports import Port
from solid_node.motion.joints import Prismatic
from simulation.standard.parts import TensBellSpring

ROOT_X = 16.357624187715082
ROOT_Z = -2
ARM_ANGLE = 4.977196461857978
ARM_LENGTH = 35.13247377645187
JOIN = .05  # overlap inside one continuous printed part, not a seated assembly gap
SEAT_GAP = .05
MOUNT_Z = -8.7 - SEAT_GAP
CUFF = 1  # source-straight ends keep the flexible/native patch joins regular
SINE, COSINE = sin(radians(ARM_ANGLE)), cos(radians(ARM_ANGLE))


def downstream(side, distance):
    """Half-space normal to one measured arm, restricted to that arm's side."""
    normal = (-side*SINE, 0, -COSINE)
    origin = (side*ROOT_X + distance*normal[0], 0, ROOT_Z + distance*normal[2])
    plane = cq.Plane(origin, (side*COSINE, 0, -SINE), normal)
    tail = cq.Workplane(plane).box(60, 60, 200, centered=(True, True, False)).val()
    half = cq.Solid.makeBox(50, 100, 200, cq.Vector(0 if side > 0 else -50, -50, -100))
    return tail.intersect(half)


class SpringMount(TensBellSpring):
    def adjust(self, shape):
        return shape.cut(downstream(1, 0)).cut(downstream(-1, 0))


class RightHook(TensBellSpring):
    def adjust(self, shape):
        return shape.intersect(downstream(1, ARM_LENGTH))


class LeftHook(TensBellSpring):
    def adjust(self, shape):
        return shape.intersect(downstream(-1, ARM_LENGTH))


def ribbed_profile():
    # Native normal sections: 6.9 × 1.8 mm strip, with an inward R .9 rib.
    # 24 chords put the rib contour within .002 mm of its source semicircle.
    return [(-.9, -3.45), (.9, -3.45), (.9, 3.45), (-.9, 3.45)] + [
        (-.9 + .9*cos(pi/2 + pi*index/24), .9*sin(pi/2 + pi*index/24))
        for index in range(25)]


class SpringArm(MolejoNode):
    x1 = Port(unit='mm')
    z1 = Port(unit='mm')
    x2 = Port(unit='mm')
    z2 = Port(unit='mm')
    x3 = Port(unit='mm')
    z3 = Port(unit='mm')
    x4 = Port(unit='mm')
    z4 = Port(unit='mm')
    end_z = Port(unit='mm')
    color = '#d3d5cb'

    def render(self):
        points = [(P.x1, 0, P.z1), (P.x2, 0, P.z2),
                  (P.x3, 0, P.z3), (P.x4, 0, P.z4)]
        profile = ribbed_profile()
        return Shape(profile=Polygon(points=profile),
                     path=[Line(to=(0, 0, CUFF)),
                           Spline(points, start_tangent=(0, 0, 1), end_tangent=(0, 0, 1)),
                           Line(to=(P.x4, 0, P.end_z))],
                     path_samples=24, profile_samples=len(profile))


def arm_coordinates(source, targets):
    def points(spread):
        result = []
        for progress in (.25, .5, .75, 1):
            # Keep the upper arm inside the bell's lower lip; most bending is
            # below that measured guide. End slopes remain parallel to source.
            bend = progress**5 * (6 - 5*progress)
            result.extend((COSINE*bend*spread,
                           CUFF + (ARM_LENGTH + 2*JOIN - 2*CUFF)*progress
                           - SINE*bend*spread))
        return (*result, result[-1] + CUFF)
    return points


class FlexibleArm(AssemblyNode):
    spread = Port(unit='mm')
    body = SpringArm()
    spread.drives((body.x1, body.z1, body.x2, body.z2,
                   body.x3, body.z3, body.x4, body.z4, body.end_z), law=arm_coordinates)


class RetainingSpring(AssemblyNode):
    """One upstream spring occurrence; its five patches share a physical body."""
    spread = Port(unit='mm')
    mount = SpringMount()
    right_arm = FlexibleArm()
    left_arm = FlexibleArm()
    right_hook = RightHook(travel=Prismatic(axis=(1, 0, 0)))
    left_hook = LeftHook(travel=Prismatic(axis=(-1, 0, 0)))
    spread.drives(right_arm.spread)
    spread.drives(left_arm.spread)
    spread.drives(right_hook.travel)
    spread.drives(left_hook.travel)

    def render(self):
        self.right_arm.rotate(180, (1, 0, 0)).rotate(ARM_ANGLE, (0, 1, 0))
        self.right_arm.translate((ROOT_X + JOIN*SINE, 0, ROOT_Z + JOIN*COSINE))
        self.left_arm.rotate(180, (1, 0, 0)).rotate(ARM_ANGLE, (0, 1, 0)).rotate(180, (0, 0, 1))
        self.left_arm.translate((-ROOT_X - JOIN*SINE, 0, ROOT_Z + JOIN*COSINE))
