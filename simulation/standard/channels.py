"""Source-specific keyed shafts, separated into sliding printed groups."""

from solid_node.motion.joints import Revolute, Prismatic
from solid_node.motion.ports import Port
from simulation.fit import FittedBevelTip, TENS_SHAFT_X_CORRECTION
import simulation.standard.assembly as source
import simulation.standard.printed as printed


class ResultOnesShaft(source.Part10208_1):
    transmission_gear_tip = FittedBevelTip()


class ResultOnes(source.Part10237_1):
    turn = Revolute(axis=(0, 0, 1), at=(40.5, 0.0, 0))
    setting = Port()
    carry = Port()
    p_10208_1 = ResultOnesShaft()
    p_10219_410002_1 = printed.Part10219_410002_1(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10221_1 = printed.Part10221_1(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10219_410002_1.travel, ratio=6)
    carry.drives(p_10221_1.travel, ratio=0)


class ResultTensShaft(source.Part10207_1_419228):
    transmission_gear_tip = FittedBevelTip()


class ResultTens(source.Part10236_1):
    turn = Revolute(axis=(0, 0, 1), at=(38.137315415, -13.851815805, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419228 = ResultTensShaft()
    p_10230_410008_1_419229 = printed.Part10230_410008_1_419229(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419227 = printed.Part10220_410003_1_419227(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419229.travel, ratio=6)
    carry.drives(p_10220_410003_1_419227.travel, ratio=4.2, offset=-4.2)

    def render(self):
        super().render()
        self.translate((TENS_SHAFT_X_CORRECTION, 0, 0))


class ResultHundredsShaft(source.Part10207_1_419087):
    transmission_gear_tip = FittedBevelTip()


class ResultHundreds(source.Part10236_2):
    turn = Revolute(axis=(0, 0, 1), at=(31.024799946, -26.032898192, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419087 = ResultHundredsShaft()
    p_10230_410008_1_419088 = printed.Part10230_410008_1_419088(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419086 = printed.Part10220_410003_1_419086(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419088.travel, ratio=6)
    carry.drives(p_10220_410003_1_419086.travel, ratio=4.2, offset=0.0)


class ResultDigit4Shaft(source.Part10207_1_419233):
    transmission_gear_tip = FittedBevelTip()


class ResultDigit4(source.Part10236_3):
    turn = Revolute(axis=(0, 0, 1), at=(20.25, -35.074028853, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419233 = ResultDigit4Shaft()
    p_10230_410008_1_419232 = printed.Part10230_410008_1_419232(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419234 = printed.Part10220_410003_1_419234(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419232.travel, ratio=6)
    carry.drives(p_10220_410003_1_419234.travel, ratio=4.2, offset=0.0)


class ResultDigit5Shaft(source.Part10207_1_419091):
    transmission_gear_tip = FittedBevelTip()


class ResultDigit5(source.Part10236_4):
    turn = Revolute(axis=(0, 0, 1), at=(7.032751196, -39.884713997, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419091 = ResultDigit5Shaft()
    p_10230_410008_1_419092 = printed.Part10230_410008_1_419092(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419093 = printed.Part10220_410003_1_419093(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419092.travel, ratio=6)
    carry.drives(p_10220_410003_1_419093.travel, ratio=4.2, offset=0.0)


class ResultDigit6Shaft(source.Part10207_1_419065):
    transmission_gear_tip = FittedBevelTip()


class ResultDigit6(source.Part10236_5):
    turn = Revolute(axis=(0, 0, 1), at=(-7.032751196, -39.884713997, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419065 = ResultDigit6Shaft()
    p_10230_410008_1_419066 = printed.Part10230_410008_1_419066(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419064 = printed.Part10220_410003_1_419064(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419066.travel, ratio=6)
    carry.drives(p_10220_410003_1_419064.travel, ratio=4.2, offset=0.0)


class ResultDigit7Shaft(source.Part10207_1_419036):
    transmission_gear_tip = FittedBevelTip()


class ResultDigit7(source.Part10236_6):
    turn = Revolute(axis=(0, 0, 1), at=(-20.25, -35.074028853, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419036 = ResultDigit7Shaft()
    p_10230_410008_1_419032 = printed.Part10230_410008_1_419032(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419039 = printed.Part10220_410003_1_419039(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419032.travel, ratio=6)
    carry.drives(p_10220_410003_1_419039.travel, ratio=4.2, offset=-4.2)


class ResultDigit8Shaft(source.Part10207_1_419076):
    transmission_gear_tip = FittedBevelTip()


class ResultDigit8(source.Part10236_7):
    turn = Revolute(axis=(0, 0, 1), at=(-31.024799946, -26.032898192, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419076 = ResultDigit8Shaft()
    p_10230_410008_1_419075 = printed.Part10230_410008_1_419075(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419074 = printed.Part10220_410003_1_419074(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419075.travel, ratio=6)
    carry.drives(p_10220_410003_1_419074.travel, ratio=4.2, offset=0.0)


class ResultDigit9Shaft(source.Part10209_1_419138):
    transmission_gear_tip = FittedBevelTip()


class ResultDigit9(source.Part10238_1):
    turn = Revolute(axis=(0, 0, 1), at=(-38.057551142, -13.851815805, 0))
    setting = Port()
    carry = Port()
    p_10209_1_419138 = ResultDigit9Shaft()
    p_10230_410008_1_419137 = printed.Part10230_410008_1_419137(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419139 = printed.Part10220_410003_1_419139(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419137.travel, ratio=6)
    carry.drives(p_10220_410003_1_419139.travel, ratio=4.2, offset=-4.2)


class ResultDigit10Shaft(source.Part10209_1_419116):
    transmission_gear_tip = FittedBevelTip()


class ResultDigit10(source.Part10238_2):
    turn = Revolute(axis=(0, 0, 1), at=(-40.5, 0.0, 0))
    setting = Port()
    carry = Port()
    p_10209_1_419116 = ResultDigit10Shaft()
    p_10230_410008_1_419118 = printed.Part10230_410008_1_419118(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419117 = printed.Part10220_410003_1_419117(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419118.travel, ratio=6)
    carry.drives(p_10220_410003_1_419117.travel, ratio=4.2, offset=-4.2)


class ResultDigit11Shaft(source.Part10209_1_419112):
    transmission_gear_tip = FittedBevelTip()


class ResultDigit11(source.Part10238_3):
    turn = Revolute(axis=(0, 0, 1), at=(-38.057551142, 13.851815805, 0))
    setting = Port()
    carry = Port()
    p_10209_1_419112 = ResultDigit11Shaft()
    p_10230_410008_1_419111 = printed.Part10230_410008_1_419111(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419114 = printed.Part10220_410003_1_419114(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419111.travel, ratio=6)
    carry.drives(p_10220_410003_1_419114.travel, ratio=4.2, offset=-4.2)


class TurnsOnesShaft(source.Part10216_1):
    transmission_gear_tip = FittedBevelTip()


class TurnsOnes(source.Part10239_1):
    turn = Revolute(axis=(0, 0, 1), at=(-26.032898192, 31.024799946, 0))
    setting = Port()
    carry = Port()
    p_10216_1 = TurnsOnesShaft()
    p_10218_1 = printed.Part10218_1(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10222_1 = printed.Part10222_1(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10218_1.travel, ratio=6)
    carry.drives(p_10222_1.travel, ratio=0)


class TurnsTensShaft(source.Part10207_1_419079):
    transmission_gear_tip = FittedBevelTip()


class TurnsTens(source.Part10236_8):
    turn = Revolute(axis=(0, 0, 1), at=(-13.851815805, 38.057551142, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419079 = TurnsTensShaft()
    p_10230_410008_1_419080 = printed.Part10230_410008_1_419080(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419081 = printed.Part10220_410003_1_419081(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419080.travel, ratio=6)
    carry.drives(p_10220_410003_1_419081.travel, ratio=4.2, offset=-1.8)


class TurnsHundredsShaft(source.Part10207_1_419069):
    transmission_gear_tip = FittedBevelTip()


class TurnsHundreds(source.Part10236_9):
    turn = Revolute(axis=(0, 0, 1), at=(0.0, 40.5, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419069 = TurnsHundredsShaft()
    p_10230_410008_1_419068 = printed.Part10230_410008_1_419068(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419070 = printed.Part10220_410003_1_419070(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419068.travel, ratio=6)
    carry.drives(p_10220_410003_1_419070.travel, ratio=4.2, offset=-1.8)


class TurnsDigit4Shaft(source.Part10207_1_419180):
    transmission_gear_tip = FittedBevelTip()


class TurnsDigit4(source.Part10236_10):
    turn = Revolute(axis=(0, 0, 1), at=(13.851815805, 38.057551142, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419180 = TurnsDigit4Shaft()
    p_10230_410008_1_419182 = printed.Part10230_410008_1_419182(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419181 = printed.Part10220_410003_1_419181(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419182.travel, ratio=6)
    carry.drives(p_10220_410003_1_419181.travel, ratio=4.2, offset=-1.8)


class TurnsDigit5Shaft(source.Part10207_1_419106):
    transmission_gear_tip = FittedBevelTip()


class TurnsDigit5(source.Part10236_11):
    turn = Revolute(axis=(0, 0, 1), at=(26.032898192, 31.024799946, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419106 = TurnsDigit5Shaft()
    p_10230_410008_1_419105 = printed.Part10230_410008_1_419105(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419107 = printed.Part10220_410003_1_419107(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419105.travel, ratio=6)
    carry.drives(p_10220_410003_1_419107.travel, ratio=4.2, offset=-1.8)


class TurnsDigit6Shaft(source.Part10207_1_419236):
    transmission_gear_tip = FittedBevelTip()


class TurnsDigit6(source.Part10236_12):
    turn = Revolute(axis=(0, 0, 1), at=(35.074028853, 20.25, 0))
    setting = Port()
    carry = Port()
    p_10207_1_419236 = TurnsDigit6Shaft()
    p_10230_410008_1_419237 = printed.Part10230_410008_1_419237(
        travel=Prismatic(axis=(0, 0, -1)))
    p_10220_410003_1_419238 = printed.Part10220_410003_1_419238(
        travel=Prismatic(axis=(0, 0, -1)))
    setting.drives(p_10230_410008_1_419237.travel, ratio=6)
    carry.drives(p_10220_410003_1_419238.travel, ratio=4.2, offset=-1.8)
