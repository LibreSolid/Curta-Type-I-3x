"""A U-wire held at its closed end, with the two free hooks spreading apart."""

from math import pi, sin, cos, radians
from molejo import Shape, Circle, Line, Arc, Spline, P
from solid_node.node import AssemblyNode, MolejoNode
from solid_node.motion.joints import Prismatic
from solid_node.motion.ports import Port

# Source-frame measurements; small fits clear the bearing's 6 mm waist and
# lower support. The slider's center is .075 mm off the bearing's center.
HALF_SPAN = 3.4
TIP_CENTER = .119583
FIRST_TIP = (TIP_CENTER - HALF_SPAN, 5.7, -.004257159)
BRIDGE_Y = 1.320845073 - FIRST_TIP[1]
BRIDGE_Z = 18.586565808 - FIRST_TIP[2]
ELBOW_Y = 1.216656167 - FIRST_TIP[1]
ELBOW_Z = 17.995681156 - FIRST_TIP[2]
SLOPE = (0, sin(radians(10)), cos(radians(10)))
FOLD_AXIS = (0, cos(radians(10)), -sin(radians(10)))


class CarrySpring(MolejoNode):
    left_mid = Port(unit='mm')
    left_root = Port(unit='mm')
    left_bridge = Port(unit='mm')
    right_bridge = Port(unit='mm')
    right_mid = Port(unit='mm')
    right_tip = Port(unit='mm')
    color = '#aeb7c2'

    def render(self):
        return Shape(profile=Circle(.3), path=[
            Line((0, -5.1, 0)),
            Arc(center=(0, -5.1, .6), axis=(-1, 0, 0), angle=pi/2),
            Spline([(P.left_mid, -5.7, 9.3 - FIRST_TIP[2]),
                    (P.left_root, ELBOW_Y, ELBOW_Z)],
                   start_tangent=(0, 0, 1), end_tangent=SLOPE),
            Arc(center=(P.left_bridge, ELBOW_Y, ELBOW_Z), axis=FOLD_AXIS, angle=pi/2),
            Line((P.right_bridge, BRIDGE_Y, BRIDGE_Z)),
            Arc(center=(P.right_bridge, ELBOW_Y, ELBOW_Z), axis=FOLD_AXIS, angle=pi/2),
            Spline([(P.right_mid, -5.7, 9.3 - FIRST_TIP[2]),
                    (P.right_tip, -5.7, .6)],
                   start_tangent=tuple(-value for value in SLOPE), end_tangent=(0, 0, -1)),
            Arc(center=(P.right_tip, -5.1, .6), axis=(1, 0, 0), angle=pi/2),
            Line((P.right_tip, 0, 0)),
        ], path_samples=24, profile_samples=24)


def coordinates(source, targets):
    def spread(amount):
        mid = 5/16  # A smooth bending-shape control, not a computed spring force.
        origin = FIRST_TIP[0]
        return (-HALF_SPAN + TIP_CENTER*mid - origin + (1-mid)*amount,
                -HALF_SPAN - origin + amount,
                -HALF_SPAN + .6 - origin + amount,
                HALF_SPAN - .6 - origin + amount,
                HALF_SPAN + TIP_CENTER*mid - origin + (1+mid)*amount,
                2*HALF_SPAN + 2*amount)
    return spread


class MountedCarrySpring(AssemblyNode):
    # The shape starts at the left open end. Its local frame follows that end;
    # inverse offsets in the shape law keep the closed U fixed on its support.
    spread = Prismatic(axis=(-1, 0, 0))
    wire = CarrySpring()
    spread.drives((wire.left_mid, wire.left_root, wire.left_bridge, wire.right_bridge,
                   wire.right_mid, wire.right_tip), law=coordinates)

    def render(self):
        self.wire.translate(FIRST_TIP)
