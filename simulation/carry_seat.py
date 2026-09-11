"""A .70 mm groove for the fixed .60 mm U-wire; the slider guide is unchanged."""

from math import pi
import cadquery as cq
from molejo import Shape, Circle, Arc, Line
from simulation.standard.parts import TensSlideBearing
from simulation.carry_spring import HALF_SPAN, FOLD_AXIS, SLOPE


def closed_fold_gauge():
    """Only the closed fold is relieved, not the long legs or detent hooks."""
    radius = .6
    rise = tuple(radius * value for value in SLOPE)
    width = 2 * HALF_SPAN
    gauge = Shape(profile=Circle(.35), path=[
        Arc(center=(radius, 0, 0), axis=FOLD_AXIS, angle=pi/2),
        Line((width - radius, rise[1], rise[2])),
        Arc(center=(width - radius, 0, 0), axis=FOLD_AXIS, angle=pi/2),
    ], path_samples=24, profile_samples=24)
    return cq.Shape.cast(gauge.brep().solid).translate(
        (-HALF_SPAN, 1.216656167, 17.995681156))


class ResultsSpringSeat(TensSlideBearing):
    """Source spring-to-bearing placement, measured in tools/carry_frames.py."""
    spring_angle = 94.51311161574411
    spring_axis = (.9999984594183192, .0013973618568333102, .0010623280235487515)
    spring_translation = (-.04712525673880208, -3.12550063954075, 1.317666364388101)

    def adjust(self, shape):
        groove = closed_fold_gauge().rotate((0, 0, 0), self.spring_axis, self.spring_angle)
        return shape.cut(groove.translate(self.spring_translation))


class TurnsSpringSeat(ResultsSpringSeat):
    spring_angle = 94.01311238915856
    spring_axis = (.9999984468883637, .0014076736217867364, .0010605073478778576)
    spring_translation = (-.0471252567388305, -3.12355097539265, 1.1838751075358047)
