"""Sand only clearing-gear flanks; keep dial faces, axles and bevels unchanged."""

import cadquery as cq
from simulation.standard.parts import ResultsDialType1, ResultsDialType2
import simulation.standard.assembly as source
from simulation.pin_mounts import HalfPin, Type2HalfPin


class ClearingGearFit:
    cam_relief = .1

    def adjust(self, shape):
        start, height = self.cam_band
        face = max((face for face in shape.Faces() if face.geomType() == 'PLANE'
                    and abs(face.Center().z - start) < .000001), key=lambda face: face.Area())
        outline, = face.outerWire().offset2D(-self.cam_relief)
        retained = cq.Solid.extrudeLinear(outline, [], cq.Vector(0, 0, height))
        band = cq.Solid.makeCylinder(8, height, cq.Vector(0, 0, start))
        return shape.cut(band.cut(retained))


class FittedDialType1(ClearingGearFit, ResultsDialType1):
    cam_band = (18.45, 1.95)


class FittedDialType2(ClearingGearFit, ResultsDialType2):
    cam_band = (21, 2.7)


class Part10203_1(source.Part10203_1):
    results_dial_type_1 = FittedDialType1()
    number_roll_carry_pin_half = HalfPin()


class Part10203_2(source.Part10203_2):
    results_dial_type_1 = FittedDialType1()
    number_roll_carry_pin_half = HalfPin()


class Part10203_3(source.Part10203_3):
    results_dial_type_1 = FittedDialType1()
    number_roll_carry_pin_half = HalfPin()


class Part10203_4(source.Part10203_4):
    results_dial_type_1 = FittedDialType1()
    number_roll_carry_pin_half = HalfPin()


class Part10204_1(source.Part10204_1):
    results_dial_type_2 = FittedDialType2()


class Part10204_2(source.Part10204_2):
    results_dial_type_2 = FittedDialType2()


class Part10204_3(source.Part10204_3):
    results_dial_type_2 = FittedDialType2()


class Part10204_4(source.Part10204_4):
    results_dial_type_2 = FittedDialType2()


class Part10204_5(source.Part10204_5):
    results_dial_type_2 = FittedDialType2()


class Part10204_6(source.Part10204_6):
    results_dial_type_2 = FittedDialType2()


class Part10204_7(source.Part10204_7):
    results_dial_type_2 = FittedDialType2()


class Part10205_1(source.Part10205_1):
    results_dial_type_2 = FittedDialType2()
    number_roll_carry_pin_half = Type2HalfPin()


class Part10205_2(source.Part10205_2):
    results_dial_type_2 = FittedDialType2()
    number_roll_carry_pin_half = Type2HalfPin()


class Part10205_3(source.Part10205_3):
    results_dial_type_2 = FittedDialType2()
    number_roll_carry_pin_half = Type2HalfPin()


class Part10205_4(source.Part10205_4):
    results_dial_type_2 = FittedDialType2()
    number_roll_carry_pin_half = Type2HalfPin()
