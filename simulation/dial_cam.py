"""A 3 mm ball follows the native dial's circular cam edge.

The dial has R7.2 lands cut by R4.5 scallops on an R6 circle. Their
intersection fixes the short dwell. The measured envelope in
dial_detent_motion.py independently checks this compact geometric law.
"""

from math import acos, degrees
from solid_node.math import abs, max, sin, cos, sqrt

CAM_RADIUS = 7.2
BALL_RADIUS = 3
HALF_DWELL = degrees(acos((7.2**2 + 6**2 - 4.5**2) / (2*7.2*6))) - 36
SEAT_GAP = .05
MEASUREMENT_BRACKET = 5 / 2**17  # upper-bracket resolution of the native probe


def rise(phase):
    angle = max(0, abs((phase + 2) % 36 - 18) - HALF_DWELL)
    horizontal = CAM_RADIUS * sin(angle)
    height = CAM_RADIUS * cos(angle) + sqrt(max(0, BALL_RADIUS**2 - horizontal**2))
    # Source sphere center is 9.45 mm above the dial axis.
    return max(SEAT_GAP, height - 9.45 + SEAT_GAP + MEASUREMENT_BRACKET)
