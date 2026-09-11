"""Clock half pins to 36°, with the cutaway clearing the neighbouring bank."""

from simulation.standard.parts import NumberRollCarryPinHalf
from solid_node.parameters import Angle


class HalfPin(NumberRollCarryPinHalf):
    clocking = Angle(180)

    def adjust(self, shape):
        # A flat's angle alone leaves two possible sides. The neighbouring
        # bank's parked digits select the cutaway side; the bore seat is fixed.
        return shape.rotate((0, 0, 0), (0, 0, 1), self.clocking)


class Type2HalfPin(HalfPin):
    # These four source mounts also differ by nine degrees from the type-1s.
    clocking = Angle(189)
