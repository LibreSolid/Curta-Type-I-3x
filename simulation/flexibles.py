"""Flexible parts fitted from the build manual and source mounting geometry."""

from simulation.colors import STEEL
from math import atan2, cos, sin, tau

from molejo import Circle, Shape, Spline, Helix, P
from solid_node.node import MolejoNode, AssemblyNode
from solid_node.motion.ports import Port
from solid_node.math import turn

ZERO_PIVOT = (40.5, 33.6)
FIXED_PIN = (33.552746609, 28.154097304, -133.45)
LEVER_PIN = (40.5, 24.9, -157.3)
WIRE = 1.1
WINDING_MANDREL = 11.5
COLLAR_RADIUS = 6.75
SEAT_GAP = 0.05
COIL_RADIUS = COLLAR_RADIUS + WIRE / 2 + SEAT_GAP
COIL_HEIGHT = 6.0
TURNS = 5


def zero_spring_path(tail=None):
    """Five CCW windings, fitted terminal bends, coordinates from the fixed pin.

    The winding mandrel is not the installed bore: the latter clears the source
    lever's 13.5 mm collar. A cubic centerline through 32 points per turn keeps
    both terminal bends continuous. It is a prescribed installed shape, not a
    springback or preload prediction. See docs/measurements.md.
    """
    cx, cy = ZERO_PIVOT
    phase = atan2(FIXED_PIN[1] - cy, FIXED_PIN[0] - cx)
    coil = []
    for index in range(32 * TURNS + 1):
        progress = index / (32 * TURNS)
        angle = phase + tau * TURNS * progress
        coil.append((cx + COIL_RADIUS * cos(angle),
                     cy + COIL_RADIUS * sin(angle),
                     -143.5 - COIL_HEIGHT * progress))
    tangent = (-COIL_RADIUS * sin(phase), COIL_RADIUS * cos(phase),
               -COIL_HEIGHT / (tau * TURNS))

    def relative(points):
        return [tuple(value - origin for value, origin in zip(point, FIXED_PIN))
                for point in points]

    return [
        Spline(relative([(*FIXED_PIN[:2], -138.9),
                         (*FIXED_PIN[:2], -140.5), coil[0]]),
               start_tangent=(0, 0, -1), end_tangent=tangent),
        Spline(relative(coil[1:]), start_tangent=tangent, end_tangent=tangent),
        Spline(tail if tail is not None else relative([
                   (cx - 3, cy - 8.7, -151.5), (*LEVER_PIN[:2], -153.0), LEVER_PIN]),
               start_tangent=tangent, end_tangent=(0, 0, -1)),
    ]


class ZeroSpring(MolejoNode):
    """Authorized replacement for invalid STEP PRODUCT #419219; 1.1 mm wire."""

    color = STEEL

    def render(self):
        return Shape(profile=Circle(WIRE / 2),
                     path=zero_spring_path(),
                     # Sampling is per spline span, not per complete spring:
                     # 32 control points/turn × 4 samples = 128 rings/turn.
                     path_samples=4, profile_samples=24)


class MovingZeroSpring(MolejoNode):
    """The coil stays on its collar while its terminal follows the lever hole."""
    shoulder_x = Port(unit='mm')
    shoulder_y = Port(unit='mm')
    terminal_x = Port(unit='mm')
    terminal_y = Port(unit='mm')
    color = STEEL

    def render(self):
        tail = [(P.shoulder_x, P.shoulder_y, -151.5 - FIXED_PIN[2]),
                (P.terminal_x, P.terminal_y, -153 - FIXED_PIN[2]),
                (P.terminal_x, P.terminal_y, LEVER_PIN[2] - FIXED_PIN[2])]
        return Shape(profile=Circle(WIRE / 2), path=zero_spring_path(tail),
                     path_samples=4, profile_samples=24)


def lever_coordinate(point, coordinate):
    def law(source, target):
        return lambda angle: turn(point, angle, about=ZERO_PIVOT)[coordinate] - FIXED_PIN[coordinate]
    return law


class MountedZeroSpring(AssemblyNode):
    deflection = Port(unit='deg')
    wire = MovingZeroSpring()
    deflection.drives(wire.shoulder_x, law=lever_coordinate((37.5, 24.9), 0))
    deflection.drives(wire.shoulder_y, law=lever_coordinate((37.5, 24.9), 1))
    deflection.drives(wire.terminal_x, law=lever_coordinate(LEVER_PIN[:2], 0))
    deflection.drives(wire.terminal_y, law=lever_coordinate(LEVER_PIN[:2], 1))


class CarriageSpring(MolejoNode):
    """Source-sized 1.8 mm wire, four coils on a 13.2 mm centerline radius.

    Constant pitch is an educational approximation to the source's flattened
    ends. The measured seats prescribe height; this does not solve spring force
    or wire strain. The upper wire endpoint stays fixed throughout the lift.
    """
    height = Port(unit='mm')
    color = STEEL

    def render(self):
        return Shape(profile=Circle(.9),
                     path=[Helix(radius=13.2, turns=4, height=P.height)],
                     path_samples=400, profile_samples=24)


class MountedCarriageSpring(AssemblyNode):
    """Placement belongs to the mounting assembly; shape ports describe the wire."""
    height = Port(unit='mm')
    wire = CarriageSpring()
    height.drives(wire.height)
