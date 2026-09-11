"""A tapered spider finger as a moving side profile swept through its width.

The native ring and rounded tip stay intact. A transverse sweep preserves the
arm's changing thickness; its upper cone is bounded by a thin inner polygonal
approximation. Bending is prescribed, not a force or strain solution.
"""

from math import hypot
import cadquery as cq
from molejo import Shape, Polygon, Line, P
from solid_node.node import AssemblyNode, MolejoNode
from solid_node.parameters import Angle
from solid_node.motion.ports import Port
from solid_node.motion.joints import Prismatic
from simulation.standard.parts import SpiderSpring

WIDTH = 4.5
ROOT = 25
TIP = 42
JOIN = .05
BOTTOM = -.2
STATIONS = (ROOT-JOIN, ROOT+.95, 29, 32, 35, 38, TIP-.95, TIP+JOIN)
PHASES = tuple(-20*index for index in range(11)) + (130, 110, 90, 70, 50, 30)
SEAT_GAP = .05
# Ball top 46.35; mounted finger bottom 45.05; another .05 above the ball.
PRELOAD = 1.35


def top_at(x):
    # Native upper cone: Z 2.22 at R 24, radial slope 1.22/21.
    # Use the width edge; the entire extruded profile stays inside the cone.
    return 2.22 - (hypot(x, WIDTH/2) - 24) * (1.22/21)


def beyond(x, phase=0):
    return cq.Solid.makeBox(30, 5, 8, cq.Vector(x, -2.5, -1)).rotate(
        (0, 0, 0), (0, 0, 1), phase)


class OneFingerMount(SpiderSpring):
    color = '#d3d5cb'

    def adjust(self, shape):
        return shape.cut(beyond(ROOT))


class SpiderMount(SpiderSpring):
    """Unchanged source ring; its nominal collar overlap is inventoried."""
    color = '#d3d5cb'

    def adjust(self, shape):
        return shape.cut(*(beyond(ROOT, phase) for phase in PHASES))


class FingerTip(SpiderSpring):
    phase = Angle(0)
    color = '#d3d5cb'

    def adjust(self, shape):
        return shape.intersect(beyond(TIP, self.phase))


class TaperedArm(MolejoNode):
    bottom_1 = Port(unit='mm')
    bottom_2 = Port(unit='mm')
    bottom_3 = Port(unit='mm')
    bottom_4 = Port(unit='mm')
    bottom_5 = Port(unit='mm')
    bottom_6 = Port(unit='mm')
    top_1 = Port(unit='mm')
    top_2 = Port(unit='mm')
    top_3 = Port(unit='mm')
    top_4 = Port(unit='mm')
    top_5 = Port(unit='mm')
    top_6 = Port(unit='mm')
    color = '#d3d5cb'

    def render(self):
        bottom = (BOTTOM, BOTTOM, P.bottom_1, P.bottom_2, P.bottom_3,
                  P.bottom_4, P.bottom_5, P.bottom_6)
        top = (top_at(STATIONS[0]), top_at(STATIONS[1]), P.top_1, P.top_2,
               P.top_3, P.top_4, P.top_5, P.top_6)
        lower = [(x-STATIONS[0], z) for x, z in zip(STATIONS, bottom)]
        upper = [(x-STATIONS[0], z) for x, z in zip(STATIONS, top)]
        return Shape(profile=Polygon(points=lower + upper[::-1]),
                     path=[Line(to=(0, 0, WIDTH))], path_samples=2, profile_samples=16)


def profile_coordinates(source, targets):
    def profile(rise):
        lower, upper = [], []
        for x in STATIONS[2:]:
            progress = min(1, (x-STATIONS[1])/(STATIONS[-2]-STATIONS[1]))
            height = progress**2 * (3-2*progress) * rise
            lower.append(BOTTOM + height)
            upper.append(top_at(x) + height)
        return (*lower, *upper)
    return profile


class SpiderFinger(AssemblyNode):
    phase = Angle(0)
    rise = Port(unit='mm')
    arm = TaperedArm()
    tip = FingerTip(phase=phase, lift=Prismatic(axis=(0, 0, 1)))
    rise.drives(tip.lift)
    rise.drives((arm.bottom_1, arm.bottom_2, arm.bottom_3, arm.bottom_4,
                 arm.bottom_5, arm.bottom_6, arm.top_1, arm.top_2, arm.top_3,
                 arm.top_4, arm.top_5, arm.top_6), law=profile_coordinates)

    def render(self):
        self.arm.rotate(90, (1, 0, 0)).translate((STATIONS[0], WIDTH/2, 0))
        self.arm.rotate(self.phase, (0, 0, 1))


class FlexibleSpider(AssemblyNode):
    """One source spring: native mounting ring and seventeen bending fingers."""
    mount = SpiderMount()
    result_1 = SpiderFinger(phase=0)
    result_2 = SpiderFinger(phase=-20)
    result_3 = SpiderFinger(phase=-40)
    result_4 = SpiderFinger(phase=-60)
    result_5 = SpiderFinger(phase=-80)
    result_6 = SpiderFinger(phase=-100)
    result_7 = SpiderFinger(phase=-120)
    result_8 = SpiderFinger(phase=-140)
    result_9 = SpiderFinger(phase=-160)
    result_10 = SpiderFinger(phase=-180)
    result_11 = SpiderFinger(phase=-200)
    turns_1 = SpiderFinger(phase=130)
    turns_2 = SpiderFinger(phase=110)
    turns_3 = SpiderFinger(phase=90)
    turns_4 = SpiderFinger(phase=70)
    turns_5 = SpiderFinger(phase=50)
    turns_6 = SpiderFinger(phase=30)
