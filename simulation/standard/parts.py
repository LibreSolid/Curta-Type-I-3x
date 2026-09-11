"""Parts scaffolded from 'curta.step' by `solid import-step`.

Generated once; edit freely -- running the command again
refuses to overwrite this file (see docs/cli.rst).
"""
from solid_node.node import StepNode
from simulation.source import STEP, prepare
prepare()

class SourcePart(StepNode):
    step_source = str(STEP)
    angular_deflection = 0.5

class M4Nut(SourcePart):
    part = 'M4 Nut'

class CoverRing(SourcePart):
    part = 'cover ring'

class M3x10Pan(SourcePart):
    part = 'M3x10 pan'

class M4x16Hex(SourcePart):
    part = 'M4x16 hex'

class ThrustRing(SourcePart):
    part = 'thrust ring'

class CarriageSpringSleeve(SourcePart):
    part = 'carriage spring sleeve'

class SelectorShaftBearing(SourcePart):
    part = 'selector shaft bearing'

class M4x10_419010(SourcePart):
    part = 'M4x10 [#419010]'

class M3x10CountersinkScrew(SourcePart):
    part = 'M3x10 countersink screw'

class SpringSleeveCClip(SourcePart):
    part = 'spring sleeve c-clip'

class CarryLeverSpring(SourcePart):
    part = 'carry lever spring'

class TensSlideBearing(SourcePart):
    part = 'tens slide bearing'

class TensSliderForResults(SourcePart):
    part = 'tens slider for results'

class UpperOuterSleeve(SourcePart):
    part = 'upper outer sleeve'

class CarriageSpring(SourcePart):
    part = 'carriage spring'

class MainCrank(SourcePart):
    part = 'main crank'

class CrankHandlePinScrew(SourcePart):
    part = 'crank handle pin screw'

class CrankHandle(SourcePart):
    part = 'crank handle'

class M5x30Countersunk(SourcePart):
    part = 'M5x30 countersunk'

class DecimalMarkerSpring(SourcePart):
    part = 'decimal marker spring'

class Part3mmBall(SourcePart):
    part = '3mm ball'

class PositionMarker(SourcePart):
    part = 'position marker'

class TransmissionGear0_5(SourcePart):
    part = 'Transmission Gear (0.5)'

class Part1_6mmSpacer(SourcePart):
    part = '1.6mm spacer'

class Part2_5mmLockoutSleeve(SourcePart):
    part = '2.5mm lockout sleeve'

class TransmissionShaft(SourcePart):
    part = 'transmission shaft'

class TransmissionGearTip(SourcePart):
    part = 'Transmission Gear Tip'

class PentagonalLockout(SourcePart):
    part = 'pentagonal lockout'

class TransmissionGear0_6(SourcePart):
    part = 'Transmission Gear (0.6)'

class Part4_8mmTensRatchetSleeve(SourcePart):
    part = '4.8mm tens ratchet sleeve'

class Part1_3mmSpacer(SourcePart):
    part = '1.3mm spacer'

class Part1_9mmSpacer(SourcePart):
    part = '1.9mm spacer'

class TensSliderForTurnsCounter(SourcePart):
    part = 'tens slider for turns counter'

class CrankHandlePin(SourcePart):
    part = 'crank handle pin'

class SelectorShaftBottom(SourcePart):
    part = 'selector shaft bottom'

class SelectorShaftTop(SourcePart):
    part = 'selector shaft top'

class NumberRoll(SourcePart):
    part = 'number roll'

class SelectorKnobSpring(SourcePart):
    part = 'selector knob spring'

class Part5mmBall(SourcePart):
    part = '5mm ball'

class DigitSelectorScrew(SourcePart):
    part = 'digit selector screw'

class SelectorKnob(SourcePart):
    part = 'selector knob'

class SettingAxleHoldingPlate(SourcePart):
    part = 'setting axle holding plate'

class Part6mmBall419094(SourcePart):
    part = '6mm ball [#419094]'

class LowerHousing(SourcePart):
    part = 'lower housing'

class BottomHousing(SourcePart):
    part = 'bottom housing'

class SpringClipForTransmissionAxle(SourcePart):
    part = 'Spring clip for transmission axle'

class Part9_10_11DigitsTransmissionShaft(SourcePart):
    part = '9,10,11 digits transmission shaft'

class TransmissionShaftType4(SourcePart):
    part = 'transmission shaft type 4'

class Part2_5mmSleeve(SourcePart):
    part = '2.5mm sleeve'

class Part5_8Sleeve(SourcePart):
    part = '5.8 sleeve'

class Part1mmSpacer(SourcePart):
    part = '1mm spacer'

class Part1_8mmSpacer(SourcePart):
    part = '1.8mm spacer'

class OnesTransmissionShaft(SourcePart):
    part = 'ones transmission shaft'

class Part4_7mmOnesSleeve(SourcePart):
    part = '4.7mm ones sleeve'

class Part1_5mmSpacer(SourcePart):
    part = '1.5mm spacer'

class ReversingShaft(SourcePart):
    part = 'reversing shaft'

class ReversingLeverKnob(SourcePart):
    part = 'reversing lever knob'

class ReversingActuator(SourcePart):
    part = 'reversing actuator'

class UpperReversingLeverSpacer(SourcePart):
    part = 'upper reversing lever spacer'

class LowerReversingLeverSpacer(SourcePart):
    part = 'lower reversing lever spacer'

class M4x10_419159(SourcePart):
    part = 'M4x10 [#419159]'

class FrameSupport(SourcePart):
    part = 'frame support'

class MainBody(SourcePart):
    part = 'main body'

class TensBellSpring(SourcePart):
    part = 'tens bell spring'

class TensBellCClip(SourcePart):
    part = 'tens bell c-clip'

class RetainingRingForTensBell(SourcePart):
    part = 'retaining ring for tens bell'

class ResultsLockingDisc(SourcePart):
    part = 'results locking disc'

class TensTurnsCounterLockingDisc(SourcePart):
    part = 'tens turns counter locking disc'

class TensBellBody(SourcePart):
    part = 'tens bell body'

class TensResultsLockingDisc(SourcePart):
    part = 'tens results locking disc'

class TurnsCounterCarryRing(SourcePart):
    part = 'turns counter carry ring'

class TensBellSpacer2(SourcePart):
    part = 'tens bell spacer 2'

class TensBellSupportPlate(SourcePart):
    part = 'tens bell support plate'

class TensBellSpacer1(SourcePart):
    part = 'tens bell spacer 1'

class TurnsCounterLockingDisc(SourcePart):
    part = 'turns counter locking disc'

class ResultsCounterCarryRing(SourcePart):
    part = 'results counter carry ring'

class AntiReversalSpring(SourcePart):
    part = 'anti-reversal spring'

class M5Nut(SourcePart):
    part = 'M5 Nut'

class ZeroPositioningDiscRoller(SourcePart):
    part = 'zero positioning disc roller'

class ZeroPositioningDiscSecuringSpring(SourcePart):
    part = 'zero positioning disc securing spring'

class AntiReversalM5BoltSleeve(SourcePart):
    part = 'anti-reversal m5 bolt sleeve'

class ReverseRotationPreventionPawl(SourcePart):
    part = 'reverse rotation prevention pawl'

class DiscRollerBoltSleeve(SourcePart):
    part = 'disc roller bolt sleeve'

class ZeroPositioningM5BoltSleeve(SourcePart):
    part = 'zero positioning m5 bolt sleeve'

class ZeroPositioningDisc(SourcePart):
    part = 'zero positioning disc'

class BearingPlate(SourcePart):
    part = 'bearing plate'

class M5x15HexBolt(SourcePart):
    part = 'M5x15 hex bolt'

class BearingPlateScrew(SourcePart):
    part = 'bearing plate screw'

class ZeroPositioningLever(SourcePart):
    part = 'zero positioning lever'

class M5x30HexBolt(SourcePart):
    part = 'M5x30 hex bolt'

class ZeroPositioningDiscPin(SourcePart):
    part = 'zero positioning disc pin'

class ReverseNosePlate(SourcePart):
    part = 'reverse nose plate'

class StepDrumJoiningPin(SourcePart):
    part = 'step drum joining pin'

class OneToothTurnsStepDrumSegment(SourcePart):
    part = 'one tooth turns step drum segment'

class NineToothTurnsStepDrumSegment(SourcePart):
    part = 'nine tooth turns step drum segment'

class StepDrumFrameTop(SourcePart):
    part = 'step drum frame top'

class EightToothStepDrumSegment(SourcePart):
    part = 'eight tooth step drum segment'

class TwoToothStepDrumSegment(SourcePart):
    part = 'two tooth step drum segment'

class StepDrumTerminationSegment(SourcePart):
    part = 'step drum termination segment'

class FourToothStepDrumSegment(SourcePart):
    part = 'four tooth step drum segment'

class ThreeToothStepDrumSegment(SourcePart):
    part = 'three tooth step drum segment'

class SixToothStepDrumSegment(SourcePart):
    part = 'six tooth step drum segment'

class FiveToothStepDrumSegment(SourcePart):
    part = 'five tooth step drum segment'

class OneToothStepDrumSegment(SourcePart):
    part = 'one tooth step drum segment'

class NineToothStepDrumSegment(SourcePart):
    part = 'nine tooth step drum segment'

class TenToothStepDrumSegment(SourcePart):
    part = 'ten tooth step drum segment'

class SevenToothStepDrumSegment(SourcePart):
    part = 'seven tooth step drum segment'

class StepDrumFrameBottom(SourcePart):
    part = 'step drum frame bottom'

class ZeroPositioningSpring(SourcePart):
    part = 'zero positioning spring'

class BasePlate(SourcePart):
    part = 'base plate'

class Part6mmBall419241(SourcePart):
    part = '6mm ball [#419241]'

class CrankCollarWasher(SourcePart):
    part = 'crank collar washer'

class NumberRollCarryPinFull(SourcePart):
    part = 'number roll carry pin full'

class ResultsDialType2(SourcePart):
    part = 'results dial type 2'

class NumberRollCarryPinHalf(SourcePart):
    part = 'number roll carry pin half'

class CrankCollarNut(SourcePart):
    part = 'crank collar nut'

class ClearingRingRivet(SourcePart):
    part = 'clearing ring rivet'

class ResultsDialType1(SourcePart):
    part = 'results dial type 1'

class DigitsCover(SourcePart):
    part = 'digits cover'

class UpperHousing(SourcePart):
    part = 'upper housing'

class CrankCollar(SourcePart):
    part = 'crank collar'

class ClearingCover(SourcePart):
    part = 'clearing cover'

class SpiderSpring(SourcePart):
    part = 'spider spring'

class DigitsAxle(SourcePart):
    part = 'digits axle'

class CounterBodyPin(SourcePart):
    part = 'counter body pin'

class ClearingPin(SourcePart):
    part = 'clearing pin'

class CounterBodyStopPin(SourcePart):
    part = 'counter body stop pin'

class CounterBody(SourcePart):
    part = 'counter body'

class ClearingStopPinSleeve(SourcePart):
    part = 'clearing stop pin sleeve'

class ClearingPinSpring(SourcePart):
    part = 'clearing pin spring'

class ClearingRing(SourcePart):
    part = 'clearing ring'
