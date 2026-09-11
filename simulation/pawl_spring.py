"""Seven documented CCW windings, fitted between the plate and moving pawl."""

from simulation.colors import STEEL
from math import atan2, cos, sin, hypot, tau
from molejo import Circle, Shape, Spline, P
from solid_node.node import AssemblyNode, MolejoNode
from solid_node.motion.ports import Port
from solid_node.math import turn
from simulation.fit import PAWL_PIVOT, PAWL_SPRING_ANCHOR, PAWL_SPRING_HOLE

# A 9.5 mm winding mandrel is not the installed bore. The 12.5 mm source
# collar needs a 12.6 mm bore: radius 6.25 + .30 wire radius + .05 seat gap.
RADIUS = 6.6
HEIGHT = 4.55
TURNS = 7
cx, cy, _ = PAWL_PIVOT
phase = atan2(PAWL_SPRING_HOLE[1] - cy, PAWL_SPRING_HOLE[0] - cx)
SHOULDER = (PAWL_SPRING_HOLE[0] - .3*cos(phase) - .6*sin(phase),
            PAWL_SPRING_HOLE[1] - .3*sin(phase) + .6*cos(phase))


def relative(points):
    return [tuple(value - origin for value, origin in zip(point, PAWL_SPRING_ANCHOR))
            for point in points]


def path():
    anchor_phase = atan2(PAWL_SPRING_ANCHOR[1] - cy, PAWL_SPRING_ANCHOR[0] - cx)
    anchor_radius = hypot(PAWL_SPRING_ANCHOR[0] - cx, PAWL_SPRING_ANCHOR[1] - cy)
    lead = []
    # The upper terminal follows the outside of the collar before joining the
    # first winding. A straight chord would pass through the printed collar.
    for index in range(21):
        progress = index / 20
        angle = anchor_phase + (phase + tau - anchor_phase) * progress
        radius = anchor_radius - (anchor_radius - RADIUS) * max(0, (progress - .7)/.3)
        lead.append((cx + radius*cos(angle), cy + radius*sin(angle), -139.3 + .5*progress))
    coil = [(cx + RADIUS*cos(phase + tau*TURNS*i/(32*TURNS)),
             cy + RADIUS*sin(phase + tau*TURNS*i/(32*TURNS)),
             -138.8 - HEIGHT*i/(32*TURNS)) for i in range(32*TURNS + 1)]
    tangent = (-RADIUS*sin(phase), RADIUS*cos(phase), -HEIGHT/(tau*TURNS))
    return [
        Spline(relative([(*PAWL_SPRING_ANCHOR[:2], -136),
                         (*PAWL_SPRING_ANCHOR[:2], -138.8)]),
               start_tangent=(0, 0, -1), end_tangent=(0, 0, -1)),
        Spline(relative(lead), start_tangent=(0, 0, -1), end_tangent=tangent),
        Spline(relative(coil[1:]), start_tangent=tangent, end_tangent=tangent),
        Spline([(P.shoulder_x, P.shoulder_y, -143 - PAWL_SPRING_ANCHOR[2]),
                (P.terminal_x, P.terminal_y, -143.35 - PAWL_SPRING_ANCHOR[2]),
                (P.terminal_x, P.terminal_y, PAWL_SPRING_HOLE[2] - PAWL_SPRING_ANCHOR[2])],
               start_tangent=tangent, end_tangent=(0, 0, -1)),
    ]


class PawlSpring(MolejoNode):
    shoulder_x = Port(unit='mm')
    shoulder_y = Port(unit='mm')
    terminal_x = Port(unit='mm')
    terminal_y = Port(unit='mm')
    color = STEEL

    def render(self):
        return Shape(profile=Circle(.3), path=path(), path_samples=4, profile_samples=24)


def coordinate(point, index):
    def law(source, target):
        return lambda angle: turn(point, angle, about=PAWL_PIVOT[:2])[index] - PAWL_SPRING_ANCHOR[index]
    return law


class MountedPawlSpring(AssemblyNode):
    deflection = Port(unit='deg')
    wire = PawlSpring()
    deflection.drives(wire.shoulder_x, law=coordinate(SHOULDER, 0))
    deflection.drives(wire.shoulder_y, law=coordinate(SHOULDER, 1))
    deflection.drives(wire.terminal_x, law=coordinate(PAWL_SPRING_HOLE[:2], 0))
    deflection.drives(wire.terminal_y, law=coordinate(PAWL_SPRING_HOLE[:2], 1))
