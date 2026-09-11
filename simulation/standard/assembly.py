"""Assembly scaffolded from 'curta.step' by `solid import-step`.

Generated once; edit freely -- running the command again
refuses to overwrite this file (see docs/cli.rst). This is
the machine at rest: no driver, no simulate() -- add motion
once the layout looks right.
"""
from solid_node.node import AssemblyNode
from .parts import AntiReversalM5BoltSleeve, AntiReversalSpring, BasePlate, BearingPlate, BearingPlateScrew, BottomHousing, CarriageSpring, CarriageSpringSleeve, CarryLeverSpring, ClearingCover, ClearingPin, ClearingPinSpring, ClearingRing, ClearingRingRivet, ClearingStopPinSleeve, CounterBody, CounterBodyPin, CounterBodyStopPin, CoverRing, CrankCollar, CrankCollarNut, CrankCollarWasher, CrankHandle, CrankHandlePin, CrankHandlePinScrew, DecimalMarkerSpring, DigitSelectorScrew, DigitsAxle, DigitsCover, DiscRollerBoltSleeve, EightToothStepDrumSegment, FiveToothStepDrumSegment, FourToothStepDrumSegment, FrameSupport, LowerHousing, LowerReversingLeverSpacer, M3x10CountersinkScrew, M3x10Pan, M4Nut, M4x10_419010, M4x10_419159, M4x16Hex, M5Nut, M5x15HexBolt, M5x30Countersunk, M5x30HexBolt, MainBody, MainCrank, NineToothStepDrumSegment, NineToothTurnsStepDrumSegment, NumberRoll, NumberRollCarryPinFull, NumberRollCarryPinHalf, OneToothStepDrumSegment, OneToothTurnsStepDrumSegment, OnesTransmissionShaft, Part1_3mmSpacer, Part1_5mmSpacer, Part1_6mmSpacer, Part1_8mmSpacer, Part1_9mmSpacer, Part1mmSpacer, Part2_5mmLockoutSleeve, Part2_5mmSleeve, Part3mmBall, Part4_7mmOnesSleeve, Part4_8mmTensRatchetSleeve, Part5_8Sleeve, Part5mmBall, Part6mmBall419094, Part6mmBall419241, Part9_10_11DigitsTransmissionShaft, PentagonalLockout, PositionMarker, ResultsCounterCarryRing, ResultsDialType1, ResultsDialType2, ResultsLockingDisc, RetainingRingForTensBell, ReverseNosePlate, ReverseRotationPreventionPawl, ReversingActuator, ReversingLeverKnob, ReversingShaft, SelectorKnob, SelectorKnobSpring, SelectorShaftBearing, SelectorShaftBottom, SelectorShaftTop, SettingAxleHoldingPlate, SevenToothStepDrumSegment, SixToothStepDrumSegment, SpiderSpring, SpringClipForTransmissionAxle, SpringSleeveCClip, StepDrumFrameBottom, StepDrumFrameTop, StepDrumJoiningPin, StepDrumTerminationSegment, TenToothStepDrumSegment, TensBellBody, TensBellCClip, TensBellSpacer1, TensBellSpacer2, TensBellSpring, TensBellSupportPlate, TensResultsLockingDisc, TensSlideBearing, TensSliderForResults, TensSliderForTurnsCounter, TensTurnsCounterLockingDisc, ThreeToothStepDrumSegment, ThrustRing, TransmissionGear0_5, TransmissionGear0_6, TransmissionGearTip, TransmissionShaft, TransmissionShaftType4, TurnsCounterCarryRing, TurnsCounterLockingDisc, TwoToothStepDrumSegment, UpperHousing, UpperOuterSleeve, UpperReversingLeverSpacer, ZeroPositioningDisc, ZeroPositioningDiscPin, ZeroPositioningDiscRoller, ZeroPositioningDiscSecuringSpring, ZeroPositioningLever, ZeroPositioningM5BoltSleeve, ZeroPositioningSpring

class ResultsTensLeverAssembly10(AssemblyNode):
    carry_lever_spring = CarryLeverSpring()
    tens_slide_bearing = TensSlideBearing()
    tens_slider_for_results = TensSliderForResults()

    def render(self):
        self.carry_lever_spring.rotate(-175.486980131, (0.999999168, 0.000174118, 0.001278307))
        self.carry_lever_spring.translate((-57.347125257, 10.472333636, -1.77550064))
        self.tens_slide_bearing.rotate(90.0, (1.0, 0.0, 0.0))
        self.tens_slide_bearing.translate((-57.3, 11.79, 1.35))
        self.tens_slider_for_results.rotate(120.0, (0.577350269, -0.577350269, 0.577350269))
        self.tens_slider_for_results.translate((-57.225, 7.89, -2.1))

class CrankHandle1(AssemblyNode):
    main_crank = MainCrank()
    crank_handle_pin_screw = CrankHandlePinScrew()
    crank_handle = CrankHandle()

    def render(self):
        self.main_crank.rotate(-74.895917198, (0.0, 0.0, 1.0))
        self.main_crank.translate((0.081490712, -0.263733179, 59.85))
        self.crank_handle_pin_screw.rotate(90.0, (0.0, 1.0, 0.0))
        self.crank_handle_pin_screw.translate((50.720609937, 13.025505425, 115.35))
        self.crank_handle.translate((49.319648043, 13.025505425, 94.35))

class ResultsTensLeverAssembly8(AssemblyNode):
    carry_lever_spring = CarryLeverSpring()
    tens_slider_for_results = TensSliderForResults()
    tens_slide_bearing = TensSlideBearing()

    def render(self):
        self.carry_lever_spring.rotate(-175.709180801, (0.939562264, 0.342157976, -0.012274798))
        self.carry_lever_spring.translate((-50.661932937, -28.839748578, -1.77550064))
        self.tens_slider_for_results.rotate(145.22456333, (0.671542934, -0.313145613, 0.671542934))
        self.tens_slider_for_results.translate((-48.908487498, -30.739430308, -2.1))
        self.tens_slide_bearing.rotate(96.717713464, (0.889126491, 0.323615577, 0.323615577))
        self.tens_slide_bearing.translate((-51.472812509, -27.800066051, 1.35))

class ResultsTensLeverAssembly5(AssemblyNode):
    tens_slider_for_results = TensSliderForResults()
    carry_lever_spring = CarryLeverSpring()
    tens_slide_bearing = TensSlideBearing()

    def render(self):
        self.tens_slider_for_results.rotate(-172.933425611, (0.705757557, 0.061745785, 0.705757557))
        self.tens_slider_for_results.translate((2.166883796, -57.725707788, 2.1))
        self.carry_lever_spring.rotate(-176.987363988, (0.642377344, 0.76582627, -0.029350834))
        self.carry_lever_spring.translate((-0.355011561, -58.294395218, -1.77550064))
        self.tens_slide_bearing.rotate(125.93195832, (0.510273605, 0.608120402, 0.608120402))
        self.tens_slide_bearing.translate((-1.660842828, -58.476796262, 1.35))

class DecimalMarker7(AssemblyNode):
    decimal_marker_spring = DecimalMarkerSpring()
    p_3mm_ball = Part3mmBall()
    position_marker = PositionMarker()

    def render(self):
        self.decimal_marker_spring.rotate(-135.880481659, (0.191265195, 0.978335874, 0.079224638))
        self.decimal_marker_spring.translate((54.49320552, -22.024904569, 52.857359313))
        self.p_3mm_ball.rotate(159.579224265, (0.381616919, -0.074606315, 0.921304741))
        self.p_3mm_ball.translate((51.447247568, -20.78660325, 49.56931278))
        self.position_marker.rotate(159.579224265, (0.381616919, -0.074606315, 0.921304741))
        self.position_marker.translate((50.955964028, -20.586877231, 49.038982694))

class ResultsTensLeverAssembly2(AssemblyNode):
    tens_slider_for_results = TensSliderForResults()
    tens_slide_bearing = TensSlideBearing()
    carry_lever_spring = CarryLeverSpring()

    def render(self):
        self.tens_slider_for_results.rotate(-132.145070558, (0.633687274, 0.443712606, 0.633687274))
        self.tens_slider_for_results.translate((51.075371294, -26.98627748, 2.1))
        self.tens_slide_bearing.rotate(165.893955739, (0.12372403, 0.701673843, 0.701673843))
        self.tens_slide_bearing.translate((49.811969681, -30.676730212, 1.35))
        self.carry_lever_spring.rotate(-179.072368892, (0.173347721, 0.98410574, -0.038554638))
        self.carry_lever_spring.translate((50.306921376, -29.454646639, -1.77550064))

class Part10230_410008_1_419032(AssemblyNode):
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((-20.25, -35.074028853, -64.92499975))
        self.p_1_6mm_spacer.translate((-20.25, -35.074028853, -70.92499975))
        self.p_2_5mm_lockout_sleeve.translate((-20.25, -35.074028853, -63.42499975))

class Part10207_1_419036(AssemblyNode):
    transmission_shaft = TransmissionShaft()
    transmission_gear_tip = TransmissionGearTip()

    def render(self):
        self.transmission_shaft.translate((-20.25, -35.074028853, -140.1))
        self.transmission_gear_tip.translate((-20.25, -35.074028853, 22.05))

class Part10220_410003_1_419039(AssemblyNode):
    pentagonal_lockout = PentagonalLockout()
    transmission_gear_0_6 = TransmissionGear0_6()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_1_9mm_spacer = Part1_9mmSpacer()

    def render(self):
        self.pentagonal_lockout.translate((-20.25, -35.074028853, -26.1))
        self.transmission_gear_0_6.translate((-20.25, -35.074028853, -33.6))
        self.p_4_8mm_tens_ratchet_sleeve.translate((-20.25, -35.074028853, -24.6))
        self.p_1_3mm_spacer.translate((-20.25, -35.074028853, -39.0))
        self.p_1_9mm_spacer.translate((-20.25, -35.074028853, -31.8))

class Part10236_6(AssemblyNode):
    p_10230_410008_1_419032 = Part10230_410008_1_419032()
    p_10207_1_419036 = Part10207_1_419036()
    p_10220_410003_1_419039 = Part10220_410003_1_419039()

class TurnsTensLeverAssembly5(AssemblyNode):
    tens_slider_for_turns_counter = TensSliderForTurnsCounter()
    tens_slide_bearing = TensSlideBearing()
    carry_lever_spring = CarryLeverSpring()

    def render(self):
        self.tens_slider_for_turns_counter.rotate(152.009109282, (0.684791079, -0.249243569, 0.684791079))
        self.tens_slider_for_turns_counter.translate((42.264568955, 39.23774791, -27.9))
        self.tens_slide_bearing.rotate(-145.22456333, (-0.313145613, 0.671542934, 0.671542934))
        self.tens_slide_bearing.translate((45.863394019, 36.315880673, 1.35))
        self.carry_lever_spring.rotate(178.436898275, (-0.422560828, 0.905759717, -0.032275094))
        self.carry_lever_spring.translate((44.986784603, 37.112960964, -1.773550975))

class TurnsTensLeverAssembly3(AssemblyNode):
    carry_lever_spring = CarryLeverSpring()
    tens_slide_bearing = TensSlideBearing()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter()

    def render(self):
        self.carry_lever_spring.rotate(-177.266123197, (0.707000796, -0.706746795, 0.025667923))
        self.carry_lever_spring.translate((10.606124892, 57.347125257, -1.773550975))
        self.tens_slide_bearing.rotate(120.0, (0.577350269, -0.577350269, -0.577350269))
        self.tens_slide_bearing.translate((11.79, 57.3, 1.35))
        self.tens_slider_for_turns_counter.rotate(180.0, (0.707106781, 0.0, 0.707106781))
        self.tens_slider_for_turns_counter.translate((7.155, 57.225, -27.9))

class ResultsTensLeverAssembly4(AssemblyNode):
    tens_slide_bearing = TensSlideBearing()
    tens_slider_for_results = TensSliderForResults()
    carry_lever_spring = CarryLeverSpring()

    def render(self):
        self.tens_slide_bearing.rotate(138.590377891, (0.377964473, 0.654653671, 0.654653671))
        self.tens_slide_bearing.translate((18.439560489, -55.518255637, 1.35))
        self.tens_slider_for_results.rotate(-158.909418821, (0.694746591, 0.186156788, 0.694746591))
        self.tens_slider_for_results.translate((21.779559564, -53.503303732, 2.1))
        self.carry_lever_spring.rotate(-177.617141875, (0.4995692, 0.865627276, -0.033466897))
        self.carry_lever_spring.translate((19.604255663, -54.900234124, -1.77550064))

class TurnsTensLeverAssembly2(AssemblyNode):
    tens_slide_bearing = TensSlideBearing()
    carry_lever_spring = CarryLeverSpring()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter()

    def render(self):
        self.tens_slide_bearing.rotate(109.207479725, (0.710564775, -0.497542812, -0.497542812))
        self.tens_slide_bearing.translate((-8.518778213, 57.876804661, 1.35))
        self.carry_lever_spring.rotate(-176.796884445, (0.819072059, -0.573301149, 0.021136601))
        self.carry_lever_spring.translate((-9.647374703, 57.516178783, -1.773550975))
        self.tens_slider_for_turns_counter.rotate(-165.893955739, (0.701673843, 0.12372403, 0.701673843))
        self.tens_slider_for_turns_counter.translate((-12.848602, 56.22106435, -27.9))

class DecimalMarker10(AssemblyNode):
    p_3mm_ball = Part3mmBall()
    position_marker = PositionMarker()
    decimal_marker_spring = DecimalMarkerSpring()

    def render(self):
        self.p_3mm_ball.rotate(136.223094285, (0.377347166, -0.166415823, 0.910996646))
        self.p_3mm_ball.translate((37.555914845, -40.728986171, 49.56931278))
        self.position_marker.rotate(136.223094285, (0.377347166, -0.166415823, 0.910996646))
        self.position_marker.translate((37.198287488, -40.337383472, 49.038982694))
        self.decimal_marker_spring.rotate(-139.007663453, (0.397995656, 0.902453445, 0.164855199))
        self.decimal_marker_spring.translate((39.773204456, -43.156922904, 52.857359313))

class SelectorShaftTop1_419054(AssemblyNode):
    selector_shaft_top = SelectorShaftTop()
    number_roll = NumberRoll()

    def render(self):
        self.selector_shaft_top.rotate(4.4, (0.0, 0.0, 1.0))
        self.selector_shaft_top.translate((58.5, 0.0, -127.8))
        self.number_roll.rotate(-180.0, (-0.038387809, 0.999262916, 0.0))
        self.number_roll.translate((58.5, 0.0, -36.3))

class SelectorKnob1_419057(AssemblyNode):
    selector_knob_spring = SelectorKnobSpring()
    p_5mm_ball = Part5mmBall()
    digit_selector_screw = DigitSelectorScrew()
    selector_knob = SelectorKnob()

    def render(self):
        self.selector_knob_spring.rotate(-180.0, (0.707106781, 0.0, -0.707106781))
        self.selector_knob_spring.translate((74.1, 0.0, -55.785999642))
        self.p_5mm_ball.rotate(180.0, (-0.707106781, 0.0, 0.707106781))
        self.p_5mm_ball.translate((63.695521812, 0.0, -55.785999642))
        self.digit_selector_screw.rotate(180.0, (-0.707106781, 0.0, 0.707106781))
        self.digit_selector_screw.translate((56.1, 0.0, -70.924999571))
        self.selector_knob.rotate(-180.0, (0.707106781, 0.0, -0.707106781))
        self.selector_knob.translate((78.599999428, 0.0, -69.725))

class DigitSelectorAxle1(AssemblyNode):
    selector_shaft_bottom = SelectorShaftBottom()
    selector_shaft_top_1_419054 = SelectorShaftTop1_419054()
    selector_knob_1_419057 = SelectorKnob1_419057()

    def render(self):
        self.selector_shaft_bottom.rotate(4.4, (0.0, 0.0, 1.0))
        self.selector_shaft_bottom.translate((58.5, 0.0, -127.775))

class DecimalMarker2(AssemblyNode):
    decimal_marker_spring = DecimalMarkerSpring()
    p_3mm_ball = Part3mmBall()
    position_marker = PositionMarker()

    def render(self):
        self.decimal_marker_spring.rotate(-137.303606873, (0.305877703, 0.943602815, 0.126698693))
        self.decimal_marker_spring.translate((61.781005735, -44.30573223, -140.321864305))
        self.p_3mm_ball.rotate(146.895452206, (0.379772522, -0.123106825, 0.916851973))
        self.p_3mm_ball.translate((59.118263899, -42.376728363, -143.609910838))
        self.position_marker.rotate(146.895452206, (0.379772522, -0.123106825, 0.916851973))
        self.position_marker.translate((58.68878941, -42.065598708, -144.140240924))

class Part10220_410003_1_419064(AssemblyNode):
    pentagonal_lockout = PentagonalLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()
    transmission_gear_0_6 = TransmissionGear0_6()
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()

    def render(self):
        self.pentagonal_lockout.translate((-7.032751196, -39.884713997, -21.9))
        self.p_1_3mm_spacer.translate((-7.032751196, -39.884713997, -34.8))
        self.transmission_gear_0_6.translate((-7.032751196, -39.884713997, -29.4))
        self.p_1_9mm_spacer.translate((-7.032751196, -39.884713997, -27.6))
        self.p_4_8mm_tens_ratchet_sleeve.translate((-7.032751196, -39.884713997, -20.4))

class Part10207_1_419065(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    transmission_shaft = TransmissionShaft()

    def render(self):
        self.transmission_gear_tip.translate((-7.032751196, -39.884713997, 22.05))
        self.transmission_shaft.translate((-7.032751196, -39.884713997, -140.1))

class Part10230_410008_1_419066(AssemblyNode):
    p_1_6mm_spacer = Part1_6mmSpacer()
    transmission_gear_0_5 = TransmissionGear0_5()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()

    def render(self):
        self.p_1_6mm_spacer.translate((-7.032751196, -39.884713997, -70.92499975))
        self.transmission_gear_0_5.translate((-7.032751196, -39.884713997, -64.92499975))
        self.p_2_5mm_lockout_sleeve.translate((-7.032751196, -39.884713997, -63.42499975))

class Part10236_5(AssemblyNode):
    p_10220_410003_1_419064 = Part10220_410003_1_419064()
    p_10207_1_419065 = Part10207_1_419065()
    p_10230_410008_1_419066 = Part10230_410008_1_419066()

class Part10230_410008_1_419068(AssemblyNode):
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((0.0, 40.5, -44.85))
        self.p_1_6mm_spacer.translate((0.0, 40.5, -50.85))
        self.p_2_5mm_lockout_sleeve.translate((0.0, 40.5, -43.35))

class Part10207_1_419069(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    transmission_shaft = TransmissionShaft()

    def render(self):
        self.transmission_gear_tip.translate((0.0, 40.5, 22.05))
        self.transmission_shaft.translate((0.0, 40.5, -140.1))

class Part10220_410003_1_419070(AssemblyNode):
    p_1_3mm_spacer = Part1_3mmSpacer()
    pentagonal_lockout = PentagonalLockout()
    transmission_gear_0_6 = TransmissionGear0_6()
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()

    def render(self):
        self.p_1_3mm_spacer.translate((0.0, 40.5, -21.9))
        self.pentagonal_lockout.translate((0.0, 40.5, -9.0))
        self.transmission_gear_0_6.translate((0.0, 40.5, -16.5))
        self.p_1_9mm_spacer.translate((0.0, 40.5, -14.7))
        self.p_4_8mm_tens_ratchet_sleeve.translate((0.0, 40.5, -7.5))

class Part10236_9(AssemblyNode):
    p_10230_410008_1_419068 = Part10230_410008_1_419068()
    p_10207_1_419069 = Part10207_1_419069()
    p_10220_410003_1_419070 = Part10220_410003_1_419070()

class DecimalMarker9(AssemblyNode):
    p_3mm_ball = Part3mmBall()
    position_marker = PositionMarker()
    decimal_marker_spring = DecimalMarkerSpring()

    def render(self):
        self.p_3mm_ball.rotate(143.950964018, (0.379191545, -0.134782135, 0.91544937))
        self.p_3mm_ball.translate((43.140082758, -34.816821341, 49.56931278))
        self.position_marker.rotate(143.950964018, (0.379191545, -0.134782135, 0.91544937))
        self.position_marker.translate((42.728727038, -34.482102846, 49.038982694))
        self.decimal_marker_spring.rotate(-137.728063245, (0.331741038, 0.933309126, 0.137411637))
        self.decimal_marker_spring.translate((45.690488223, -36.892076016, 52.857359313))

class ResultsTensLeverAssembly6(AssemblyNode):
    carry_lever_spring = CarryLeverSpring()
    tens_slider_for_results = TensSliderForResults()
    tens_slide_bearing = TensSlideBearing()

    def render(self):
        self.carry_lever_spring.rotate(-176.449067053, (0.765705559, 0.642730479, -0.024341906))
        self.carry_lever_spring.translate((-20.271459152, -54.657391914, -1.77550064))
        self.tens_slider_for_results.rotate(172.933425611, (0.705757557, -0.061745785, 0.705757557))
        self.tens_slider_for_results.translate((-17.707150138, -54.985539544, -2.1))
        self.tens_slide_bearing.rotate(114.404497338, (0.644400478, 0.540716203, 0.540716203))
        self.tens_slide_bearing.translate((-21.560923988, -54.382172233, 1.35))

class Part10220_410003_1_419074(AssemblyNode):
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    transmission_gear_0_6 = TransmissionGear0_6()
    pentagonal_lockout = PentagonalLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()

    def render(self):
        self.p_1_9mm_spacer.translate((-31.024799946, -26.032898192, -27.6))
        self.p_4_8mm_tens_ratchet_sleeve.translate((-31.024799946, -26.032898192, -20.4))
        self.transmission_gear_0_6.translate((-31.024799946, -26.032898192, -29.4))
        self.pentagonal_lockout.translate((-31.024799946, -26.032898192, -21.9))
        self.p_1_3mm_spacer.translate((-31.024799946, -26.032898192, -34.8))

class Part10230_410008_1_419075(AssemblyNode):
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((-31.024799946, -26.032898192, -63.42499975))
        self.transmission_gear_0_5.translate((-31.024799946, -26.032898192, -64.92499975))
        self.p_1_6mm_spacer.translate((-31.024799946, -26.032898192, -70.92499975))

class Part10207_1_419076(AssemblyNode):
    transmission_shaft = TransmissionShaft()
    transmission_gear_tip = TransmissionGearTip()

    def render(self):
        self.transmission_shaft.translate((-31.024799946, -26.032898192, -140.1))
        self.transmission_gear_tip.translate((-31.024799946, -26.032898192, 22.05))

class Part10236_7(AssemblyNode):
    p_10220_410003_1_419074 = Part10220_410003_1_419074()
    p_10230_410008_1_419075 = Part10230_410008_1_419075()
    p_10207_1_419076 = Part10207_1_419076()

class DecimalMarker4(AssemblyNode):
    decimal_marker_spring = DecimalMarkerSpring()
    p_3mm_ball = Part3mmBall()
    position_marker = PositionMarker()

    def render(self):
        self.decimal_marker_spring.rotate(-139.163502465, (0.405154938, 0.898713357, 0.16782067))
        self.decimal_marker_spring.translate((50.443460043, -56.797366575, -140.321864305))
        self.p_3mm_ball.rotate(135.369868621, (0.377112548, -0.170008612, 0.910430227))
        self.p_3mm_ball.translate((48.266165606, -54.333499912, -143.609910838))
        self.position_marker.rotate(135.369868621, (0.377112548, -0.170008612, 0.910430227))
        self.position_marker.translate((47.914989084, -53.936102063, -144.140240924))

class Part10207_1_419079(AssemblyNode):
    transmission_shaft = TransmissionShaft()
    transmission_gear_tip = TransmissionGearTip()

    def render(self):
        self.transmission_shaft.translate((-13.851815805, 38.057551142, -140.1))
        self.transmission_gear_tip.translate((-13.851815805, 38.057551142, 22.05))

class Part10230_410008_1_419080(AssemblyNode):
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((-13.851815805, 38.057551142, -43.35))
        self.transmission_gear_0_5.translate((-13.851815805, 38.057551142, -44.85))
        self.p_1_6mm_spacer.translate((-13.851815805, 38.057551142, -50.85))

class Part10220_410003_1_419081(AssemblyNode):
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_9mm_spacer = Part1_9mmSpacer()
    transmission_gear_0_6 = TransmissionGear0_6()
    pentagonal_lockout = PentagonalLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((-13.851815805, 38.057551142, -7.5))
        self.p_1_9mm_spacer.translate((-13.851815805, 38.057551142, -14.7))
        self.transmission_gear_0_6.translate((-13.851815805, 38.057551142, -16.5))
        self.pentagonal_lockout.translate((-13.851815805, 38.057551142, -9.0))
        self.p_1_3mm_spacer.translate((-13.851815805, 38.057551142, -21.9))

class Part10236_8(AssemblyNode):
    p_10207_1_419079 = Part10207_1_419079()
    p_10230_410008_1_419080 = Part10230_410008_1_419080()
    p_10220_410003_1_419081 = Part10220_410003_1_419081()

class SelectorShaftTop1_419083(AssemblyNode):
    selector_shaft_top = SelectorShaftTop()
    number_roll = NumberRoll()

    def render(self):
        self.selector_shaft_top.rotate(-55.6, (0.0, 0.0, 1.0))
        self.selector_shaft_top.translate((29.25, -50.662486121, -127.8))
        self.number_roll.rotate(-180.0, (0.46638664, 0.884580975, 0.0))
        self.number_roll.translate((29.25, -50.662486121, -36.3))

class SelectorKnob1_419084(AssemblyNode):
    selector_knob = SelectorKnob()
    selector_knob_spring = SelectorKnobSpring()
    p_5mm_ball = Part5mmBall()
    digit_selector_screw = DigitSelectorScrew()

    def render(self):
        self.selector_knob.rotate(138.590377891, (-0.654653671, 0.377964473, 0.654653671))
        self.selector_knob.translate((39.299999714, -68.069596242, -69.725))
        self.selector_knob_spring.rotate(138.590377891, (-0.654653671, 0.377964473, 0.654653671))
        self.selector_knob_spring.translate((37.05, -64.17248242, -55.785999642))
        self.p_5mm_ball.rotate(138.590377891, (-0.654653671, 0.377964473, 0.654653671))
        self.p_5mm_ball.translate((31.847760906, -55.161939996, -55.785999642))
        self.digit_selector_screw.rotate(138.590377891, (-0.654653671, 0.377964473, 0.654653671))
        self.digit_selector_screw.translate((28.05, -48.584025152, -70.924999571))

class DigitSelectorAxle4(AssemblyNode):
    selector_shaft_top_1_419083 = SelectorShaftTop1_419083()
    selector_shaft_bottom = SelectorShaftBottom()
    selector_knob_1_419084 = SelectorKnob1_419084()

    def render(self):
        self.selector_shaft_bottom.rotate(-55.6, (0.0, 0.0, 1.0))
        self.selector_shaft_bottom.translate((29.25, -50.662486121, -127.775))

class Part10220_410003_1_419086(AssemblyNode):
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    transmission_gear_0_6 = TransmissionGear0_6()
    p_1_3mm_spacer = Part1_3mmSpacer()
    pentagonal_lockout = PentagonalLockout()

    def render(self):
        self.p_1_9mm_spacer.translate((31.024799946, -26.032898192, -27.6))
        self.p_4_8mm_tens_ratchet_sleeve.translate((31.024799946, -26.032898192, -20.4))
        self.transmission_gear_0_6.translate((31.024799946, -26.032898192, -29.4))
        self.p_1_3mm_spacer.translate((31.024799946, -26.032898192, -34.8))
        self.pentagonal_lockout.translate((31.024799946, -26.032898192, -21.9))

class Part10207_1_419087(AssemblyNode):
    transmission_shaft = TransmissionShaft()
    transmission_gear_tip = TransmissionGearTip()

    def render(self):
        self.transmission_shaft.translate((31.024799946, -26.032898192, -140.1))
        self.transmission_gear_tip.translate((31.024799946, -26.032898192, 22.05))

class Part10230_410008_1_419088(AssemblyNode):
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    p_1_6mm_spacer = Part1_6mmSpacer()
    transmission_gear_0_5 = TransmissionGear0_5()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((31.024799946, -26.032898192, -63.42499975))
        self.p_1_6mm_spacer.translate((31.024799946, -26.032898192, -70.92499975))
        self.transmission_gear_0_5.translate((31.024799946, -26.032898192, -64.92499975))

class Part10236_2(AssemblyNode):
    p_10220_410003_1_419086 = Part10220_410003_1_419086()
    p_10207_1_419087 = Part10207_1_419087()
    p_10230_410008_1_419088 = Part10230_410008_1_419088()

class Part10207_1_419091(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    transmission_shaft = TransmissionShaft()

    def render(self):
        self.transmission_gear_tip.translate((7.032751196, -39.884713997, 22.05))
        self.transmission_shaft.translate((7.032751196, -39.884713997, -140.1))

class Part10230_410008_1_419092(AssemblyNode):
    transmission_gear_0_5 = TransmissionGear0_5()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.transmission_gear_0_5.translate((7.032751196, -39.884713997, -64.92499975))
        self.p_2_5mm_lockout_sleeve.translate((7.032751196, -39.884713997, -63.42499975))
        self.p_1_6mm_spacer.translate((7.032751196, -39.884713997, -70.92499975))

class Part10220_410003_1_419093(AssemblyNode):
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_1_3mm_spacer = Part1_3mmSpacer()
    transmission_gear_0_6 = TransmissionGear0_6()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    pentagonal_lockout = PentagonalLockout()

    def render(self):
        self.p_1_9mm_spacer.translate((7.032751196, -39.884713997, -27.6))
        self.p_1_3mm_spacer.translate((7.032751196, -39.884713997, -34.8))
        self.transmission_gear_0_6.translate((7.032751196, -39.884713997, -29.4))
        self.p_4_8mm_tens_ratchet_sleeve.translate((7.032751196, -39.884713997, -20.4))
        self.pentagonal_lockout.translate((7.032751196, -39.884713997, -21.9))

class Part10236_4(AssemblyNode):
    p_10207_1_419091 = Part10207_1_419091()
    p_10230_410008_1_419092 = Part10230_410008_1_419092()
    p_10220_410003_1_419093 = Part10220_410003_1_419093()

class LowerHousing1(AssemblyNode):
    lower_housing = LowerHousing()
    bottom_housing = BottomHousing()

    def render(self):
        self.lower_housing.rotate(72.0, (0.0, 0.0, 1.0))
        self.lower_housing.translate((-0.406900356, 0.745841949, -186.45))
        self.bottom_housing.translate((-0.406900356, 0.745841949, -150.45))

class TurnsTensLeverAssembly4(AssemblyNode):
    carry_lever_spring = CarryLeverSpring()
    tens_slide_bearing = TensSlideBearing()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter()

    def render(self):
        self.carry_lever_spring.rotate(177.818391321, (-0.573475281, 0.81869448, -0.029418539))
        self.carry_lever_spring.translate((29.580369296, 50.261162071, -1.773550975))
        self.tens_slide_bearing.rotate(-132.145070558, (-0.443712606, 0.633687274, 0.633687274))
        self.tens_slide_bearing.translate((30.676730212, 49.811969681, 1.35))
        self.tens_slider_for_turns_counter.rotate(165.893955739, (0.701673843, -0.12372403, 0.701673843))
        self.tens_slider_for_turns_counter.translate((26.295603404, 51.326756099, -27.9))

class DecimalMarker6(AssemblyNode):
    p_3mm_ball = Part3mmBall()
    position_marker = PositionMarker()
    decimal_marker_spring = DecimalMarkerSpring()

    def render(self):
        self.p_3mm_ball.rotate(167.245626034, (0.382273132, -0.046294504, 0.922888981))
        self.p_3mm_ball.translate((53.912105303, -13.185618206, 49.56931278))
        self.position_marker.rotate(167.245626034, (0.382273132, -0.046294504, 0.922888981))
        self.position_marker.translate((53.397106005, -13.059025462, 49.038982694))
        self.decimal_marker_spring.rotate(-135.344067558, (0.120076014, 0.991518013, 0.049737114))
        self.decimal_marker_spring.translate((57.105100952, -13.97049322, 52.857359313))

class TurnsTensLeverAssembly1(AssemblyNode):
    tens_slide_bearing = TensSlideBearing()
    carry_lever_spring = CarryLeverSpring()
    tens_slider_for_turns_counter = TensSliderForTurnsCounter()

    def render(self):
        self.tens_slide_bearing.rotate(100.288585137, (0.834817129, -0.389281621, -0.389281621))
        self.tens_slide_bearing.translate((-27.800066051, 51.472812509, 1.35))
        self.carry_lever_spring.rotate(-176.424953014, (0.90626823, -0.422401603, 0.015961864))
        self.carry_lever_spring.translate((-28.737258529, 50.747932299, -1.773550975))
        self.tens_slider_for_turns_counter.rotate(-152.009109282, (0.684791079, 0.249243569, 0.684791079))
        self.tens_slider_for_turns_counter.translate((-31.302472974, 48.436038605, -27.9))

class SelectorKnob1_419102(AssemblyNode):
    selector_knob = SelectorKnob()
    selector_knob_spring = SelectorKnobSpring()
    p_5mm_ball = Part5mmBall()
    digit_selector_screw = DigitSelectorScrew()

    def render(self):
        self.selector_knob.rotate(104.477512186, (-0.447213595, 0.774596669, 0.447213595))
        self.selector_knob.translate((-39.299999714, -68.069596242, -69.725))
        self.selector_knob_spring.rotate(104.477512186, (-0.447213595, 0.774596669, 0.447213595))
        self.selector_knob_spring.translate((-37.05, -64.17248242, -55.785999642))
        self.p_5mm_ball.rotate(104.477512186, (-0.447213595, 0.774596669, 0.447213595))
        self.p_5mm_ball.translate((-31.847760906, -55.161939996, -55.785999642))
        self.digit_selector_screw.rotate(104.477512186, (-0.447213595, 0.774596669, 0.447213595))
        self.digit_selector_screw.translate((-28.05, -48.584025152, -70.924999571))

class SelectorShaftTop1_419103(AssemblyNode):
    number_roll = NumberRoll()
    selector_shaft_top = SelectorShaftTop()

    def render(self):
        self.number_roll.rotate(-180.0, (0.846193166, 0.532876276, 0.0))
        self.number_roll.translate((-29.25, -50.662486121, -36.3))
        self.selector_shaft_top.rotate(-115.6, (0.0, 0.0, 1.0))
        self.selector_shaft_top.translate((-29.25, -50.662486121, -127.8))

class DigitSelectorAxle7(AssemblyNode):
    selector_knob_1_419102 = SelectorKnob1_419102()
    selector_shaft_top_1_419103 = SelectorShaftTop1_419103()
    selector_shaft_bottom = SelectorShaftBottom()

    def render(self):
        self.selector_shaft_bottom.rotate(-115.6, (0.0, 0.0, 1.0))
        self.selector_shaft_bottom.translate((-29.25, -50.662486121, -127.775))

class Part10230_410008_1_419105(AssemblyNode):
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((26.032898192, 31.024799946, -44.85))
        self.p_1_6mm_spacer.translate((26.032898192, 31.024799946, -50.85))
        self.p_2_5mm_lockout_sleeve.translate((26.032898192, 31.024799946, -43.35))

class Part10207_1_419106(AssemblyNode):
    transmission_shaft = TransmissionShaft()
    transmission_gear_tip = TransmissionGearTip()

    def render(self):
        self.transmission_shaft.translate((26.032898192, 31.024799946, -140.1))
        self.transmission_gear_tip.translate((26.032898192, 31.024799946, 22.05))

class Part10220_410003_1_419107(AssemblyNode):
    transmission_gear_0_6 = TransmissionGear0_6()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    pentagonal_lockout = PentagonalLockout()
    p_1_9mm_spacer = Part1_9mmSpacer()

    def render(self):
        self.transmission_gear_0_6.translate((26.032898192, 31.024799946, -16.5))
        self.p_1_3mm_spacer.translate((26.032898192, 31.024799946, -21.9))
        self.p_4_8mm_tens_ratchet_sleeve.translate((26.032898192, 31.024799946, -7.5))
        self.pentagonal_lockout.translate((26.032898192, 31.024799946, -9.0))
        self.p_1_9mm_spacer.translate((26.032898192, 31.024799946, -14.7))

class Part10236_11(AssemblyNode):
    p_10230_410008_1_419105 = Part10230_410008_1_419105()
    p_10207_1_419106 = Part10207_1_419106()
    p_10220_410003_1_419107 = Part10220_410003_1_419107()

class ResultsTensLeverAssembly3(AssemblyNode):
    carry_lever_spring = CarryLeverSpring()
    tens_slide_bearing = TensSlideBearing()
    tens_slider_for_results = TensSliderForResults()

    def render(self):
        self.carry_lever_spring.rotate(-178.319252635, (0.341627902, 0.939123693, -0.03656591))
        self.carry_lever_spring.translate((37.198960326, -44.884294554, -1.77550064))
        self.tens_slide_bearing.rotate(152.009109282, (0.249243569, 0.684791079, 0.684791079))
        self.tens_slide_bearing.translate((36.315880673, -45.863394019, 1.35))
        self.tens_slider_for_results.rotate(-145.22456333, (0.671542934, 0.313145613, 0.671542934))
        self.tens_slider_for_results.translate((38.765299017, -42.827611621, 2.1))

class Part10230_410008_1_419111(AssemblyNode):
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((-38.057551142, 13.851815805, -65.1))
        self.p_1_6mm_spacer.translate((-38.057551142, 13.851815805, -71.1))
        self.p_2_5mm_lockout_sleeve.translate((-38.057551142, 13.851815805, -63.6))

class Part10209_1_419112(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    p_9_10_11_digits_transmission_shaft = Part9_10_11DigitsTransmissionShaft()

    def render(self):
        self.transmission_gear_tip.translate((-38.057551142, 13.851815805, 22.05))
        self.p_9_10_11_digits_transmission_shaft.translate((-38.057551142, 13.851815805, -140.1))

class Part10220_410003_1_419114(AssemblyNode):
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_9mm_spacer = Part1_9mmSpacer()
    transmission_gear_0_6 = TransmissionGear0_6()
    p_1_3mm_spacer = Part1_3mmSpacer()
    pentagonal_lockout = PentagonalLockout()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((-38.057551142, 13.851815805, -24.6))
        self.p_1_9mm_spacer.translate((-38.057551142, 13.851815805, -31.8))
        self.transmission_gear_0_6.translate((-38.057551142, 13.851815805, -33.6))
        self.p_1_3mm_spacer.translate((-38.057551142, 13.851815805, -39.0))
        self.pentagonal_lockout.translate((-38.057551142, 13.851815805, -26.1))

class Part10238_3(AssemblyNode):
    spring_clip_for_transmission_axle_1 = SpringClipForTransmissionAxle()
    spring_clip_for_transmission_axle_2 = SpringClipForTransmissionAxle()
    p_10230_410008_1_419111 = Part10230_410008_1_419111()
    p_10209_1_419112 = Part10209_1_419112()
    p_10220_410003_1_419114 = Part10220_410003_1_419114()

    def render(self):
        self.spring_clip_for_transmission_axle_1.translate((-38.057551142, 13.851815805, -57.3))
        self.spring_clip_for_transmission_axle_2.translate((-38.057551142, 13.851815805, -73.8))

class Part10209_1_419116(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    p_9_10_11_digits_transmission_shaft = Part9_10_11DigitsTransmissionShaft()

    def render(self):
        self.transmission_gear_tip.translate((-40.5, 0.0, 22.05))
        self.p_9_10_11_digits_transmission_shaft.translate((-40.5, 0.0, -140.1))

class Part10220_410003_1_419117(AssemblyNode):
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_9mm_spacer = Part1_9mmSpacer()
    transmission_gear_0_6 = TransmissionGear0_6()
    pentagonal_lockout = PentagonalLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((-40.5, 0.0, -24.6))
        self.p_1_9mm_spacer.translate((-40.5, 0.0, -31.8))
        self.transmission_gear_0_6.translate((-40.5, 0.0, -33.6))
        self.pentagonal_lockout.translate((-40.5, 0.0, -26.1))
        self.p_1_3mm_spacer.translate((-40.5, 0.0, -39.0))

class Part10230_410008_1_419118(AssemblyNode):
    transmission_gear_0_5 = TransmissionGear0_5()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.transmission_gear_0_5.translate((-40.5, 0.0, -65.1))
        self.p_2_5mm_lockout_sleeve.translate((-40.5, 0.0, -63.6))
        self.p_1_6mm_spacer.translate((-40.5, 0.0, -71.1))

class Part10238_2(AssemblyNode):
    spring_clip_for_transmission_axle_1 = SpringClipForTransmissionAxle()
    spring_clip_for_transmission_axle_2 = SpringClipForTransmissionAxle()
    p_10209_1_419116 = Part10209_1_419116()
    p_10220_410003_1_419117 = Part10220_410003_1_419117()
    p_10230_410008_1_419118 = Part10230_410008_1_419118()

    def render(self):
        self.spring_clip_for_transmission_axle_1.translate((-40.5, 0.0, -57.3))
        self.spring_clip_for_transmission_axle_2.translate((-40.5, 0.0, -73.8))

class ResultsTensLeverAssembly9(AssemblyNode):
    tens_slider_for_results = TensSliderForResults()
    carry_lever_spring = CarryLeverSpring()
    tens_slide_bearing = TensSlideBearing()

    def render(self):
        self.tens_slider_for_results.rotate(132.145070558, (0.633687274, -0.443712606, 0.633687274))
        self.tens_slider_for_results.translate((-56.472449155, -12.157927924, -2.1))
        self.carry_lever_spring.rotate(-175.530141664, (0.984762153, 0.173816938, -0.005583447))
        self.carry_lever_spring.translate((-57.470419478, -9.77309736, -1.77550064))
        self.tens_slide_bearing.rotate(91.727941072, (0.970287525, 0.17108787, 0.17108787))
        self.tens_slide_bearing.translate((-57.876804661, -8.518778213, 1.35))

class Part10216_1(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    transmission_shaft_type_4 = TransmissionShaftType4()

    def render(self):
        self.transmission_gear_tip.translate((-26.032898192, 31.024799946, 22.05))
        self.transmission_shaft_type_4.translate((-26.032898192, 31.024799946, -140.1))

class Part10222_1(AssemblyNode):
    p_2_5mm_sleeve = Part2_5mmSleeve()
    pentagonal_lockout = PentagonalLockout()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.p_2_5mm_sleeve.translate((-26.032898192, 31.024799946, -6.15))
        self.pentagonal_lockout.translate((-26.032898192, 31.024799946, -7.65))
        self.p_1_6mm_spacer.translate((-26.032898192, 31.024799946, -13.65))

class Part10218_1(AssemblyNode):
    p_5_8_sleeve = Part5_8Sleeve()
    transmission_gear_0_5_1 = TransmissionGear0_5()
    p_1mm_spacer_1 = Part1mmSpacer()
    transmission_gear_0_5_2 = TransmissionGear0_5()
    p_1mm_spacer_2 = Part1mmSpacer()
    p_1_8mm_spacer = Part1_8mmSpacer()
    transmission_gear_0_5_3 = TransmissionGear0_5()

    def render(self):
        self.p_5_8_sleeve.translate((-26.032898192, 31.024799946, -38.85))
        self.transmission_gear_0_5_1.translate((-26.032898192, 31.024799946, -49.35))
        self.p_1mm_spacer_1.translate((-26.032898192, 31.024799946, -47.85))
        self.transmission_gear_0_5_2.translate((-26.032898192, 31.024799946, -40.35))
        self.p_1mm_spacer_2.translate((-26.032898192, 31.024799946, -43.35))
        self.p_1_8mm_spacer.translate((-26.032898192, 31.024799946, -55.95))
        self.transmission_gear_0_5_3.translate((-26.032898192, 31.024799946, -44.85))

class Part10239_1(AssemblyNode):
    p_10216_1 = Part10216_1()
    p_10222_1 = Part10222_1()
    p_10218_1 = Part10218_1()

class Part10208_1(AssemblyNode):
    ones_transmission_shaft = OnesTransmissionShaft()
    transmission_gear_tip = TransmissionGearTip()

    def render(self):
        self.ones_transmission_shaft.translate((40.5, 0.0, -140.1))
        self.transmission_gear_tip.translate((40.5, 0.0, 22.05))

class Part10219_410002_1(AssemblyNode):
    p_1_8mm_spacer = Part1_8mmSpacer()
    p_4_7mm_ones_sleeve = Part4_7mmOnesSleeve()
    p_1_5mm_spacer = Part1_5mmSpacer()
    transmission_gear_0_5_1 = TransmissionGear0_5()
    transmission_gear_0_5_2 = TransmissionGear0_5()

    def render(self):
        self.p_1_8mm_spacer.translate((40.5, 0.0, -71.52499975))
        self.p_4_7mm_ones_sleeve.translate((40.5, 0.0, -57.42499975))
        self.p_1_5mm_spacer.translate((40.5, 0.0, -63.42499975))
        self.transmission_gear_0_5_1.translate((40.5, 0.0, -64.92499975))
        self.transmission_gear_0_5_2.translate((40.5, 0.0, -58.92499975))

class Part10221_1(AssemblyNode):
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    pentagonal_lockout = PentagonalLockout()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((40.5, 0.0, -21.15))
        self.pentagonal_lockout.translate((40.5, 0.0, -22.65))
        self.p_1_6mm_spacer.translate((40.5, 0.0, -28.65))

class Part10237_1(AssemblyNode):
    p_10208_1 = Part10208_1()
    p_10219_410002_1 = Part10219_410002_1()
    p_10221_1 = Part10221_1()

class Part10230_410008_1_419137(AssemblyNode):
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()

    def render(self):
        self.transmission_gear_0_5.translate((-38.057551142, -13.851815805, -65.1))
        self.p_1_6mm_spacer.translate((-38.057551142, -13.851815805, -71.1))
        self.p_2_5mm_lockout_sleeve.translate((-38.057551142, -13.851815805, -63.6))

class Part10209_1_419138(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    p_9_10_11_digits_transmission_shaft = Part9_10_11DigitsTransmissionShaft()

    def render(self):
        self.transmission_gear_tip.translate((-38.057551142, -13.851815805, 22.05))
        self.p_9_10_11_digits_transmission_shaft.translate((-38.057551142, -13.851815805, -140.1))

class Part10220_410003_1_419139(AssemblyNode):
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    p_1_9mm_spacer = Part1_9mmSpacer()
    transmission_gear_0_6 = TransmissionGear0_6()
    p_1_3mm_spacer = Part1_3mmSpacer()
    pentagonal_lockout = PentagonalLockout()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((-38.057551142, -13.851815805, -24.6))
        self.p_1_9mm_spacer.translate((-38.057551142, -13.851815805, -31.8))
        self.transmission_gear_0_6.translate((-38.057551142, -13.851815805, -33.6))
        self.p_1_3mm_spacer.translate((-38.057551142, -13.851815805, -39.0))
        self.pentagonal_lockout.translate((-38.057551142, -13.851815805, -26.1))

class Part10238_1(AssemblyNode):
    p_10230_410008_1_419137 = Part10230_410008_1_419137()
    p_10209_1_419138 = Part10209_1_419138()
    p_10220_410003_1_419139 = Part10220_410003_1_419139()

class SelectorKnob1_419141(AssemblyNode):
    selector_knob = SelectorKnob()
    digit_selector_screw = DigitSelectorScrew()
    p_5mm_ball = Part5mmBall()
    selector_knob_spring = SelectorKnobSpring()

    def render(self):
        self.selector_knob.rotate(114.404497338, (-0.540716203, 0.644400478, 0.540716203))
        self.selector_knob.translate((-13.648746665, -77.405888823, -69.725))
        self.digit_selector_screw.rotate(114.404497338, (-0.540716203, 0.644400478, 0.540716203))
        self.digit_selector_screw.translate((-9.741662767, -55.247714944, -70.924999571))
        self.p_5mm_ball.rotate(114.404497338, (-0.540716203, 0.644400478, 0.540716203))
        self.p_5mm_ball.translate((-11.060611288, -62.727843712, -55.785999642))
        self.selector_knob_spring.rotate(114.404497338, (-0.540716203, 0.644400478, 0.540716203))
        self.selector_knob_spring.translate((-12.867329965, -72.974254498, -55.785999642))

class SelectorShaftTop1_419142(AssemblyNode):
    number_roll = NumberRoll()
    selector_shaft_top = SelectorShaftTop()

    def render(self):
        self.number_roll.rotate(180.0, (0.740804596, 0.671720589, 0.0))
        self.number_roll.translate((-10.158418394, -57.611253551, -36.3))
        self.selector_shaft_top.rotate(-95.6, (0.0, 0.0, 1.0))
        self.selector_shaft_top.translate((-10.158418394, -57.611253551, -127.8))

class DigitSelectorAxle6(AssemblyNode):
    selector_shaft_bottom = SelectorShaftBottom()
    selector_knob_1_419141 = SelectorKnob1_419141()
    selector_shaft_top_1_419142 = SelectorShaftTop1_419142()

    def render(self):
        self.selector_shaft_bottom.rotate(-95.6, (0.0, 0.0, 1.0))
        self.selector_shaft_bottom.translate((-10.158418394, -57.611253551, -127.775))

class ReversingLeverKnob1(AssemblyNode):
    reversing_lever_knob = ReversingLeverKnob()
    reversing_actuator = ReversingActuator()

    def render(self):
        self.reversing_lever_knob.rotate(-165.893955739, (0.701673843, -0.12372403, -0.701673843))
        self.reversing_lever_knob.translate((19.973907668, 60.694100512, -82.2575))
        self.reversing_actuator.rotate(-20.0, (0.0, 0.0, 1.0))
        self.reversing_actuator.translate((-1.88117949, 0.647742044, -44.0075))

class ReversingLever1(AssemblyNode):
    reversing_shaft = ReversingShaft()
    p_5mm_ball = Part5mmBall()
    reversing_lever_knob_1 = ReversingLeverKnob1()
    selector_knob_spring = SelectorKnobSpring()
    upper_reversing_lever_spacer = UpperReversingLeverSpacer()
    lower_reversing_lever_spacer = LowerReversingLeverSpacer()

    def render(self):
        self.reversing_shaft.rotate(70.0, (0.0, 0.0, 1.0))
        self.reversing_shaft.translate((17.613968679, 54.210221429, -139.2))
        self.p_5mm_ball.rotate(-91.727941072, (0.970287525, -0.17108787, 0.17108787))
        self.p_5mm_ball.translate((19.505705679, 59.407726119, -53.7575))
        self.selector_knob_spring.rotate(91.727941072, (0.970287525, -0.17108787, -0.17108787))
        self.selector_knob_spring.translate((23.325705073, 69.903088196, -53.7575))
        self.upper_reversing_lever_spacer.rotate(-20.0, (0.0, 0.0, 1.0))
        self.upper_reversing_lever_spacer.translate((17.613968679, 54.210221429, -41.1575))
        self.lower_reversing_lever_spacer.rotate(-20.0, (0.0, 0.0, 1.0))
        self.lower_reversing_lever_spacer.translate((17.613968679, 54.210221429, -124.7573))

class ResultsTensLeverAssembly7(AssemblyNode):
    tens_slider_for_results = TensSliderForResults()
    carry_lever_spring = CarryLeverSpring()
    tens_slide_bearing = TensSlideBearing()

    def render(self):
        self.tens_slider_for_results.rotate(158.909418821, (0.694746591, -0.186156788, 0.694746591))
        self.tens_slider_for_results.translate((-35.445440436, -45.613303732, 2.1))
        self.carry_lever_spring.rotate(-176.018634684, (0.865788662, 0.500064337, -0.018591707))
        self.carry_lever_spring.translate((-37.742869594, -44.427900489, -1.77550064))
        self.tens_slide_bearing.rotate(104.477512186, (0.774596669, 0.447213595, 0.447213595))
        self.tens_slide_bearing.translate((-38.860439511, -43.728255637, 1.35))

class SelectorKnob1_419152(AssemblyNode):
    p_5mm_ball = Part5mmBall()
    digit_selector_screw = DigitSelectorScrew()
    selector_knob_spring = SelectorKnobSpring()
    selector_knob = SelectorKnob()

    def render(self):
        self.p_5mm_ball.rotate(-165.893955739, (0.701673843, -0.12372403, -0.701673843))
        self.p_5mm_ball.translate((59.854211823, -21.785151499, -55.785999642))
        self.digit_selector_screw.rotate(-165.893955739, (0.701673843, -0.12372403, -0.701673843))
        self.digit_selector_screw.translate((52.716756026, -19.187330041, -70.924999571))
        self.selector_knob_spring.rotate(-165.893955739, (0.701673843, -0.12372403, -0.701673843))
        self.selector_knob_spring.translate((69.6312232, -25.34369262, -55.785999642))
        self.selector_knob.rotate(-165.893955739, (0.701673843, -0.12372403, -0.701673843))
        self.selector_knob.translate((73.859839456, -26.88278307, -69.725))

class SelectorShaftTop1_419153(AssemblyNode):
    number_roll = NumberRoll()
    selector_shaft_top = SelectorShaftTop()

    def render(self):
        self.number_roll.rotate(180.0, (0.135715572, 0.99074784, 0.0))
        self.number_roll.translate((54.972018316, -20.008178385, -36.3))
        self.selector_shaft_top.rotate(-15.6, (0.0, 0.0, 1.0))
        self.selector_shaft_top.translate((54.972018316, -20.008178385, -127.8))

class DigitSelectorAxle2(AssemblyNode):
    selector_shaft_bottom = SelectorShaftBottom()
    selector_knob_1_419152 = SelectorKnob1_419152()
    selector_shaft_top_1_419153 = SelectorShaftTop1_419153()

    def render(self):
        self.selector_shaft_bottom.rotate(-15.6, (0.0, 0.0, 1.0))
        self.selector_shaft_bottom.translate((54.972018316, -20.008178385, -127.775))

class SelectorKnob1_419155(AssemblyNode):
    selector_knob = SelectorKnob()
    selector_knob_spring = SelectorKnobSpring()
    p_5mm_ball = Part5mmBall()
    digit_selector_screw = DigitSelectorScrew()

    def render(self):
        self.selector_knob.rotate(96.717713464, (-0.323615577, 0.889126491, 0.323615577))
        self.selector_knob.translate((-60.211092791, -50.523105754, -69.725))
        self.selector_knob_spring.rotate(96.717713464, (-0.323615577, 0.889126491, 0.323615577))
        self.selector_knob_spring.translate((-56.763893235, -47.630561878, -55.785999642))
        self.p_5mm_ball.rotate(96.717713464, (-0.323615577, 0.889126491, 0.323615577))
        self.p_5mm_ball.translate((-48.793600535, -40.942692213, -55.785999642))
        self.digit_selector_screw.rotate(96.717713464, (-0.323615577, 0.889126491, 0.323615577))
        self.digit_selector_screw.translate((-42.975093259, -36.060384903, -70.924999571))

class SelectorShaftTop1_419156(AssemblyNode):
    selector_shaft_top = SelectorShaftTop()
    number_roll = NumberRoll()

    def render(self):
        self.selector_shaft_top.rotate(-135.6, (0.0, 0.0, 1.0))
        self.selector_shaft_top.translate((-44.813599922, -37.603075167, -127.8))
        self.number_roll.rotate(-180.0, (0.925870585, 0.377840787, 0.0))
        self.number_roll.translate((-44.813599922, -37.603075167, -36.3))

class DigitSelectorAxle8(AssemblyNode):
    selector_shaft_bottom = SelectorShaftBottom()
    selector_knob_1_419155 = SelectorKnob1_419155()
    selector_shaft_top_1_419156 = SelectorShaftTop1_419156()

    def render(self):
        self.selector_shaft_bottom.rotate(-135.6, (0.0, 0.0, 1.0))
        self.selector_shaft_bottom.translate((-44.813599922, -37.603075167, -127.775))

class DecimalMarker5(AssemblyNode):
    p_3mm_ball = Part3mmBall()
    position_marker = PositionMarker()
    decimal_marker_spring = DecimalMarkerSpring()

    def render(self):
        self.p_3mm_ball.rotate(129.676948332, (0.37536949, -0.19457448, 0.906222113))
        self.p_3mm_ball.translate((41.96267889, -59.317624522, -143.609910838))
        self.position_marker.rotate(129.676948332, (0.37536949, -0.19457448, 0.906222113))
        self.position_marker.translate((41.65698207, -58.884266178, -144.140240924))
        self.decimal_marker_spring.rotate(-140.276504171, (0.452062465, 0.872110551, 0.187250404))
        self.decimal_marker_spring.translate((43.857999174, -62.004446254, -140.321864305))

class TensBell1(AssemblyNode):
    results_locking_disc = ResultsLockingDisc()
    tens_turns_counter_locking_disc = TensTurnsCounterLockingDisc()
    tens_bell_body = TensBellBody()
    tens_results_locking_disc = TensResultsLockingDisc()
    turns_counter_carry_ring = TurnsCounterCarryRing()
    tens_bell_spacer_2_1 = TensBellSpacer2()
    tens_bell_support_plate = TensBellSupportPlate()
    tens_bell_spacer_2_2 = TensBellSpacer2()
    tens_bell_spacer_1 = TensBellSpacer1()
    turns_counter_locking_disc = TurnsCounterLockingDisc()
    results_counter_carry_ring = ResultsCounterCarryRing()

    def render(self):
        self.results_locking_disc.translate((0.0, 0.0, -23.1))
        self.tens_turns_counter_locking_disc.translate((0.0, 0.0, -10.8))
        self.tens_bell_body.translate((0.0, 0.0, -6.9))
        self.tens_results_locking_disc.translate((0.0, 0.0, -25.5))
        self.turns_counter_carry_ring.rotate(-103.0, (0.0, 0.0, 1.0))
        self.turns_counter_carry_ring.translate((0.0, 0.0, -18.3))
        self.tens_bell_spacer_2_1.rotate(77.0, (0.0, 0.0, 1.0))
        self.tens_bell_spacer_2_1.translate((0.0, 0.0, -31.5))
        self.tens_bell_support_plate.translate((0.0, 0.0, -33.0))
        self.tens_bell_spacer_2_2.rotate(-103.0, (0.0, 0.0, 1.0))
        self.tens_bell_spacer_2_2.translate((0.0, 0.0, -16.8))
        self.tens_bell_spacer_1.rotate(-13.0, (0.0, 0.0, 1.0))
        self.tens_bell_spacer_1.translate((0.0, 0.0, -21.6))
        self.turns_counter_locking_disc.translate((0.0, 0.0, -8.4))
        self.results_counter_carry_ring.rotate(77.0, (0.0, 0.0, 1.0))
        self.results_counter_carry_ring.translate((0.0, 0.0, -33.0))

class UpperFrame1(AssemblyNode):
    m4x10_419159_1 = M4x10_419159()
    frame_support_1 = FrameSupport()
    main_body = MainBody()
    tens_bell_spring = TensBellSpring()
    m4_nut_1 = M4Nut()
    m4_nut_2 = M4Nut()
    m4_nut_3 = M4Nut()
    frame_support_2 = FrameSupport()
    tens_bell_c_clip = TensBellCClip()
    m4x10_419159_2 = M4x10_419159()
    frame_support_3 = FrameSupport()
    retaining_ring_for_tens_bell = RetainingRingForTensBell()
    tens_bell_1 = TensBell1()

    def render(self):
        self.m4x10_419159_1.rotate(180.0, (1.0, 0.0, 0.0))
        self.m4x10_419159_1.translate((-10.5, 0.0, -2.7))
        self.frame_support_1.translate((-52.84947971, -21.352575825, -142.95))
        self.tens_bell_spring.translate((0.0, 0.0, -8.7))
        self.m4_nut_1.translate((52.84947971, 21.352575825, -15.9))
        self.m4_nut_2.translate((-52.84947971, -21.352575825, -15.9))
        self.m4_nut_3.translate((-38.140444562, 42.359255052, -15.9))
        self.frame_support_2.translate((-38.140444562, 42.359255052, -142.95))
        self.tens_bell_c_clip.translate((0.0, 0.0, 63.6))
        self.m4x10_419159_2.rotate(180.0, (1.0, 0.0, 0.0))
        self.m4x10_419159_2.translate((10.5, 0.0, -2.7))
        self.frame_support_3.translate((52.84947971, 21.352575825, -142.95))
        self.retaining_ring_for_tens_bell.translate((0.0, 0.0, 61.8))

class SelectorKnob1_419177(AssemblyNode):
    selector_knob_spring = SelectorKnobSpring()
    p_5mm_ball = Part5mmBall()
    digit_selector_screw = DigitSelectorScrew()
    selector_knob = SelectorKnob()

    def render(self):
        self.selector_knob_spring.rotate(-125.93195832, (0.608120402, -0.510273605, -0.608120402))
        self.selector_knob_spring.translate((12.867329965, -72.974254498, -55.785999642))
        self.p_5mm_ball.rotate(-125.93195832, (0.608120402, -0.510273605, -0.608120402))
        self.p_5mm_ball.translate((11.060611288, -62.727843712, -55.785999642))
        self.digit_selector_screw.rotate(-125.93195832, (0.608120402, -0.510273605, -0.608120402))
        self.digit_selector_screw.translate((9.741662767, -55.247714944, -70.924999571))
        self.selector_knob.rotate(-125.93195832, (0.608120402, -0.510273605, -0.608120402))
        self.selector_knob.translate((13.648746665, -77.405888823, -69.725))

class SelectorShaftTop1_419178(AssemblyNode):
    number_roll = NumberRoll()
    selector_shaft_top = SelectorShaftTop()

    def render(self):
        self.number_roll.rotate(180.0, (0.612907054, 0.790155012, 0.0))
        self.number_roll.translate((10.158418394, -57.611253551, -36.3))
        self.selector_shaft_top.rotate(-75.6, (0.0, 0.0, 1.0))
        self.selector_shaft_top.translate((10.158418394, -57.611253551, -127.8))

class DigitSelectorAxle5(AssemblyNode):
    selector_shaft_bottom = SelectorShaftBottom()
    selector_knob_1_419177 = SelectorKnob1_419177()
    selector_shaft_top_1_419178 = SelectorShaftTop1_419178()

    def render(self):
        self.selector_shaft_bottom.rotate(-75.6, (0.0, 0.0, 1.0))
        self.selector_shaft_bottom.translate((10.158418394, -57.611253551, -127.775))

class Part10207_1_419180(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    transmission_shaft = TransmissionShaft()

    def render(self):
        self.transmission_gear_tip.translate((13.851815805, 38.057551142, 22.05))
        self.transmission_shaft.translate((13.851815805, 38.057551142, -140.1))

class Part10220_410003_1_419181(AssemblyNode):
    transmission_gear_0_6 = TransmissionGear0_6()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    pentagonal_lockout = PentagonalLockout()

    def render(self):
        self.transmission_gear_0_6.translate((13.851815805, 38.057551142, -16.5))
        self.p_1_3mm_spacer.translate((13.851815805, 38.057551142, -21.9))
        self.p_1_9mm_spacer.translate((13.851815805, 38.057551142, -14.7))
        self.p_4_8mm_tens_ratchet_sleeve.translate((13.851815805, 38.057551142, -7.5))
        self.pentagonal_lockout.translate((13.851815805, 38.057551142, -9.0))

class Part10230_410008_1_419182(AssemblyNode):
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((13.851815805, 38.057551142, -43.35))
        self.transmission_gear_0_5.translate((13.851815805, 38.057551142, -44.85))
        self.p_1_6mm_spacer.translate((13.851815805, 38.057551142, -50.85))

class Part10236_10(AssemblyNode):
    p_10207_1_419180 = Part10207_1_419180()
    p_10220_410003_1_419181 = Part10220_410003_1_419181()
    p_10230_410008_1_419182 = Part10230_410008_1_419182()

class MainAxleStepDrumTop1(AssemblyNode):
    one_tooth_turns_step_drum_segment_1 = OneToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_2 = OneToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_3 = OneToothTurnsStepDrumSegment()
    nine_tooth_turns_step_drum_segment = NineToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_4 = OneToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_5 = OneToothTurnsStepDrumSegment()
    one_tooth_turns_step_drum_segment_6 = OneToothTurnsStepDrumSegment()
    step_drum_frame_top = StepDrumFrameTop()

    def render(self):
        self.one_tooth_turns_step_drum_segment_1.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_1.translate((-0.016356142, 0.223394941, -51.2))
        self.one_tooth_turns_step_drum_segment_2.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_2.translate((-0.016356142, 0.223394941, -45.2))
        self.one_tooth_turns_step_drum_segment_3.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_3.translate((-0.016356142, 0.223394941, -46.7))
        self.nine_tooth_turns_step_drum_segment.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.nine_tooth_turns_step_drum_segment.translate((-0.016356142, 0.223394941, -49.7))
        self.one_tooth_turns_step_drum_segment_4.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_4.translate((-0.016356142, 0.223394941, -52.7))
        self.one_tooth_turns_step_drum_segment_5.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_5.translate((-0.016356142, 0.223394941, -54.2))
        self.one_tooth_turns_step_drum_segment_6.rotate(2.604082802, (0.0, 0.0, 1.0))
        self.one_tooth_turns_step_drum_segment_6.translate((-0.016356142, 0.223394941, -48.2))
        self.step_drum_frame_top.rotate(-89.895917198, (0.0, 0.0, 1.0))
        self.step_drum_frame_top.translate((-0.009541016, 0.073549841, -66.3))

class MainAxleStepDrumBottom1(AssemblyNode):
    eight_tooth_step_drum_segment_1 = EightToothStepDrumSegment()
    two_tooth_step_drum_segment_1 = TwoToothStepDrumSegment()
    step_drum_termination_segment = StepDrumTerminationSegment()
    four_tooth_step_drum_segment_1 = FourToothStepDrumSegment()
    three_tooth_step_drum_segment_1 = ThreeToothStepDrumSegment()
    six_tooth_step_drum_segment_1 = SixToothStepDrumSegment()
    two_tooth_step_drum_segment_2 = TwoToothStepDrumSegment()
    five_tooth_step_drum_segment_1 = FiveToothStepDrumSegment()
    four_tooth_step_drum_segment_2 = FourToothStepDrumSegment()
    four_tooth_step_drum_segment_3 = FourToothStepDrumSegment()
    one_tooth_step_drum_segment_1 = OneToothStepDrumSegment()
    two_tooth_step_drum_segment_3 = TwoToothStepDrumSegment()
    five_tooth_step_drum_segment_2 = FiveToothStepDrumSegment()
    five_tooth_step_drum_segment_3 = FiveToothStepDrumSegment()
    four_tooth_step_drum_segment_4 = FourToothStepDrumSegment()
    two_tooth_step_drum_segment_4 = TwoToothStepDrumSegment()
    three_tooth_step_drum_segment_2 = ThreeToothStepDrumSegment()
    nine_tooth_step_drum_segment_1 = NineToothStepDrumSegment()
    two_tooth_step_drum_segment_5 = TwoToothStepDrumSegment()
    three_tooth_step_drum_segment_3 = ThreeToothStepDrumSegment()
    one_tooth_step_drum_segment_2 = OneToothStepDrumSegment()
    ten_tooth_step_drum_segment = TenToothStepDrumSegment()
    five_tooth_step_drum_segment_4 = FiveToothStepDrumSegment()
    two_tooth_step_drum_segment_6 = TwoToothStepDrumSegment()
    seven_tooth_step_drum_segment_1 = SevenToothStepDrumSegment()
    one_tooth_step_drum_segment_3 = OneToothStepDrumSegment()
    one_tooth_step_drum_segment_4 = OneToothStepDrumSegment()
    step_drum_frame_bottom = StepDrumFrameBottom()
    nine_tooth_step_drum_segment_2 = NineToothStepDrumSegment()
    eight_tooth_step_drum_segment_2 = EightToothStepDrumSegment()
    three_tooth_step_drum_segment_4 = ThreeToothStepDrumSegment()
    five_tooth_step_drum_segment_5 = FiveToothStepDrumSegment()
    seven_tooth_step_drum_segment_2 = SevenToothStepDrumSegment()
    one_tooth_step_drum_segment_5 = OneToothStepDrumSegment()
    three_tooth_step_drum_segment_5 = ThreeToothStepDrumSegment()
    three_tooth_step_drum_segment_6 = ThreeToothStepDrumSegment()
    four_tooth_step_drum_segment_5 = FourToothStepDrumSegment()
    four_tooth_step_drum_segment_6 = FourToothStepDrumSegment()
    six_tooth_step_drum_segment_2 = SixToothStepDrumSegment()
    one_tooth_step_drum_segment_6 = OneToothStepDrumSegment()

    def render(self):
        self.eight_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.eight_tooth_step_drum_segment_1.translate((0.0, 0.0, -79.8))
        self.two_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_1.translate((0.0, 0.0, -78.3))
        self.step_drum_termination_segment.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.step_drum_termination_segment.translate((0.0, 0.0, -124.8))
        self.four_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_1.translate((0.0, 0.0, -102.3))
        self.three_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_1.translate((0.0, 0.0, -81.3))
        self.six_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.six_tooth_step_drum_segment_1.translate((0.0, 0.0, -91.8))
        self.two_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_2.translate((0.0, 0.0, -115.8))
        self.five_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_1.translate((0.0, 0.0, -99.3))
        self.four_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_2.translate((0.0, 0.0, -87.3))
        self.four_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_3.translate((0.0, 0.0, -105.3))
        self.one_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_1.translate((0.0, 0.0, -73.8))
        self.two_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_3.translate((0.0, 0.0, -75.3))
        self.five_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_2.translate((0.0, 0.0, -94.8))
        self.five_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_3.translate((0.0, 0.0, -93.3))
        self.four_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_4.translate((0.0, 0.0, -90.3))
        self.two_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_4.translate((0.0, 0.0, -114.3))
        self.three_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_2.translate((0.0, 0.0, -109.8))
        self.nine_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.nine_tooth_step_drum_segment_1.translate((0.0, 0.0, -118.8))
        self.two_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_5.translate((0.0, 0.0, -117.3))
        self.three_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_3.translate((0.0, 0.0, -108.3))
        self.one_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_2.translate((0.0, 0.0, -120.3))
        self.ten_tooth_step_drum_segment.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.ten_tooth_step_drum_segment.translate((0.0, 0.0, -67.8))
        self.five_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_4.translate((0.0, 0.0, -96.3))
        self.two_tooth_step_drum_segment_6.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.two_tooth_step_drum_segment_6.translate((0.0, 0.0, -76.8))
        self.seven_tooth_step_drum_segment_1.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.seven_tooth_step_drum_segment_1.translate((0.0, 0.0, -106.8))
        self.one_tooth_step_drum_segment_3.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_3.translate((0.0, 0.0, -72.3))
        self.one_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_4.translate((0.0, 0.0, -70.8))
        self.step_drum_frame_bottom.rotate(-89.895917198, (0.0, 0.0, 1.0))
        self.step_drum_frame_bottom.translate((0.0, 0.0, -66.3))
        self.nine_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.nine_tooth_step_drum_segment_2.translate((0.0, 0.0, -73.8))
        self.eight_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.eight_tooth_step_drum_segment_2.translate((0.0, 0.0, -112.8))
        self.three_tooth_step_drum_segment_4.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_4.translate((0.0, 0.0, -84.3))
        self.five_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.five_tooth_step_drum_segment_5.translate((0.0, 0.0, -97.8))
        self.seven_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.seven_tooth_step_drum_segment_2.translate((0.0, 0.0, -85.8))
        self.one_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_5.translate((0.0, 0.0, -69.3))
        self.three_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_5.translate((0.0, 0.0, -82.8))
        self.three_tooth_step_drum_segment_6.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.three_tooth_step_drum_segment_6.translate((0.0, 0.0, -111.3))
        self.four_tooth_step_drum_segment_5.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_5.translate((0.0, 0.0, -88.8))
        self.four_tooth_step_drum_segment_6.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.four_tooth_step_drum_segment_6.translate((0.0, 0.0, -103.8))
        self.six_tooth_step_drum_segment_2.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.six_tooth_step_drum_segment_2.translate((0.0, 0.0, -100.8))
        self.one_tooth_step_drum_segment_6.rotate(170.104082802, (0.0, 0.0, 1.0))
        self.one_tooth_step_drum_segment_6.translate((0.0, 0.0, -121.8))

class MainAxleStepDrum1(AssemblyNode):
    step_drum_joining_pin_1 = StepDrumJoiningPin()
    step_drum_joining_pin_2 = StepDrumJoiningPin()
    main_axle_step_drum_top_1 = MainAxleStepDrumTop1()
    step_drum_joining_pin_3 = StepDrumJoiningPin()
    main_axle_step_drum_bottom_1 = MainAxleStepDrumBottom1()

    def render(self):
        self.step_drum_joining_pin_1.rotate(-89.895917198, (0.0, 0.0, 1.0))
        self.step_drum_joining_pin_1.translate((16.812898203, -17.875420569, -65.1))
        self.step_drum_joining_pin_2.rotate(-89.895917198, (0.0, 0.0, 1.0))
        self.step_drum_joining_pin_2.translate((-0.054229046, 24.673509251, -65.1))
        self.step_drum_joining_pin_3.rotate(-89.895917198, (0.0, 0.0, 1.0))
        self.step_drum_joining_pin_3.translate((-15.133219336, -19.328366406, -65.1))

class LowerFrame1(AssemblyNode):
    anti_reversal_spring = AntiReversalSpring()
    m5_nut_1 = M5Nut()
    zero_positioning_disc_roller = ZeroPositioningDiscRoller()
    m5_nut_2 = M5Nut()
    zero_positioning_disc_securing_spring = ZeroPositioningDiscSecuringSpring()
    anti_reversal_m5_bolt_sleeve = AntiReversalM5BoltSleeve()
    reverse_rotation_prevention_pawl = ReverseRotationPreventionPawl()
    disc_roller_bolt_sleeve = DiscRollerBoltSleeve()
    zero_positioning_m5_bolt_sleeve = ZeroPositioningM5BoltSleeve()
    zero_positioning_disc = ZeroPositioningDisc()
    bearing_plate = BearingPlate()
    m5x15_hex_bolt_1 = M5x15HexBolt()
    bearing_plate_screw = BearingPlateScrew()
    m5x15_hex_bolt_2 = M5x15HexBolt()
    zero_positioning_lever = ZeroPositioningLever()
    m5x30_hex_bolt = M5x30HexBolt()
    zero_positioning_disc_pin = ZeroPositioningDiscPin()
    reverse_nose_plate = ReverseNosePlate()
    main_axle_step_drum_1 = MainAxleStepDrum1()
    zero_positioning_spring = ZeroPositioningSpring()

    def render(self):
        self.anti_reversal_spring.rotate(24.099851655, (0.0, 0.0, 1.0))
        self.anti_reversal_spring.translate((-51.702407033, 9.116529328, -143.7))
        self.m5_nut_1.rotate(180.0, (1.0, 0.0, 0.0))
        self.m5_nut_1.translate((40.5, 33.6, -128.25))
        self.zero_positioning_disc_roller.translate((40.5, 0.0, -153.1))
        self.m5_nut_2.rotate(-90.0, (0.0, 0.0, 1.0))
        self.m5_nut_2.translate((40.5, 0.0, -160.5))
        self.zero_positioning_disc_securing_spring.rotate(180.0, (0.999999588, 0.000908294, 0.0))
        self.zero_positioning_disc_securing_spring.translate((0.029065386, -15.9999736, -142.2))
        self.anti_reversal_m5_bolt_sleeve.rotate(180.0, (0.0, 0.0, 1.0))
        self.anti_reversal_m5_bolt_sleeve.translate((-51.702407033, 9.116529328, -152.55))
        self.reverse_rotation_prevention_pawl.rotate(180.0, (-0.122734172, 0.992439582, 0.0))
        self.reverse_rotation_prevention_pawl.translate((-51.702407033, 9.116529328, -143.7))
        self.disc_roller_bolt_sleeve.rotate(-90.0, (0.0, 0.0, 1.0))
        self.disc_roller_bolt_sleeve.translate((40.5, 0.0, -153.3))
        self.zero_positioning_m5_bolt_sleeve.rotate(-90.0, (0.0, 0.0, 1.0))
        self.zero_positioning_m5_bolt_sleeve.translate((40.5, 33.6, -161.85))
        self.zero_positioning_disc.rotate(-180.0, (0.70774875, -0.706464229, 0.0))
        self.zero_positioning_disc.translate((0.0, 0.0, -138.45))
        self.bearing_plate.rotate(180.0, (1.0, 0.0, 0.0))
        self.bearing_plate.translate((0.0, 0.0, -118.35))
        self.m5x15_hex_bolt_1.rotate(-90.0, (0.0, 0.0, 1.0))
        self.m5x15_hex_bolt_1.translate((40.5, 0.0, -161.4))
        self.bearing_plate_screw.rotate(180.0, (1.0, 0.0, 0.0))
        self.bearing_plate_screw.translate((-14.4, 0.0, -111.75))
        self.m5x15_hex_bolt_2.rotate(-180.0, (0.707106781, 0.707106781, 0.0))
        self.m5x15_hex_bolt_2.translate((-51.702407033, 9.116529328, -133.95))
        self.zero_positioning_lever.rotate(-90.0, (0.0, 0.0, 1.0))
        self.zero_positioning_lever.translate((40.5, 33.6, -156.3))
        self.m5x30_hex_bolt.rotate(180.0, (0.0, 1.0, 0.0))
        self.m5x30_hex_bolt.translate((40.5, 33.6, -128.25))
        self.zero_positioning_disc_pin.rotate(-179.92640235, (0.707106635, 0.000642261, 0.707106635))
        self.zero_positioning_disc_pin.translate((-14.99997525, -0.027248799, -165.75))
        self.reverse_nose_plate.rotate(180.0, (0.0, 1.0, 0.0))
        self.reverse_nose_plate.translate((-14.4, 0.0, -116.85))
        self.zero_positioning_spring.rotate(180.0, (-0.656059029, 0.75470958, 0.0))
        self.zero_positioning_spring.translate((40.49999902, 33.599994789, -142.800003302))

class DecimalMarker3(AssemblyNode):
    position_marker = PositionMarker()
    decimal_marker_spring = DecimalMarkerSpring()
    p_3mm_ball = Part3mmBall()

    def render(self):
        self.position_marker.rotate(141.087342869, (0.378564418, -0.146325502, 0.913935353))
        self.position_marker.translate((53.59584881, -48.333920505, -144.140240924))
        self.decimal_marker_spring.rotate(-138.174394016, (0.356577937, 0.922516697, 0.147699417))
        self.decimal_marker_spring.translate((56.421574057, -50.90204761, -140.321864305))
        self.p_3mm_ball.rotate(141.087342869, (0.378564418, -0.146325502, 0.913935353))
        self.p_3mm_ball.translate((53.98831065, -48.690604825, -143.609910838))

class ResultsTensLeverAssembly1(AssemblyNode):
    tens_slider_for_results = TensSliderForResults()
    tens_slide_bearing = TensSlideBearing()
    carry_lever_spring = CarryLeverSpring()

    def render(self):
        self.tens_slider_for_results.rotate(-120.0, (0.577350269, 0.577350269, 0.577350269))
        self.tens_slider_for_results.translate((57.225, -7.89, -2.1))
        self.tens_slide_bearing.rotate(-180.0, (0.0, 0.707106781, 0.707106781))
        self.tens_slide_bearing.translate((57.3, -11.79, 1.35))
        self.carry_lever_spring.rotate(-179.853630404, (-0.000173983, 0.999224553, -0.03937338))
        self.carry_lever_spring.translate((57.347125257, -10.472333636, -1.77550064))

class SelectorShaftTop1_419224(AssemblyNode):
    number_roll = NumberRoll()
    selector_shaft_top = SelectorShaftTop()

    def render(self):
        self.number_roll.rotate(-180.0, (0.305695305, 0.952129393, 0.0))
        self.number_roll.translate((44.813599922, -37.603075167, -36.3))
        self.selector_shaft_top.rotate(-35.6, (0.0, 0.0, 1.0))
        self.selector_shaft_top.translate((44.813599922, -37.603075167, -127.8))

class SelectorKnob1_419225(AssemblyNode):
    selector_knob = SelectorKnob()
    p_5mm_ball = Part5mmBall()
    digit_selector_screw = DigitSelectorScrew()
    selector_knob_spring = SelectorKnobSpring()

    def render(self):
        self.selector_knob.rotate(152.009109282, (-0.684791079, 0.249243569, 0.684791079))
        self.selector_knob.translate((60.211092791, -50.523105754, -69.725))
        self.p_5mm_ball.rotate(152.009109282, (-0.684791079, 0.249243569, 0.684791079))
        self.p_5mm_ball.translate((48.793600535, -40.942692213, -55.785999642))
        self.digit_selector_screw.rotate(152.009109282, (-0.684791079, 0.249243569, 0.684791079))
        self.digit_selector_screw.translate((42.975093259, -36.060384903, -70.924999571))
        self.selector_knob_spring.rotate(152.009109282, (-0.684791079, 0.249243569, 0.684791079))
        self.selector_knob_spring.translate((56.763893235, -47.630561878, -55.785999642))

class DigitSelectorAxle3(AssemblyNode):
    selector_shaft_bottom = SelectorShaftBottom()
    selector_shaft_top_1_419224 = SelectorShaftTop1_419224()
    selector_knob_1_419225 = SelectorKnob1_419225()

    def render(self):
        self.selector_shaft_bottom.rotate(-35.6, (0.0, 0.0, 1.0))
        self.selector_shaft_bottom.translate((44.813599922, -37.603075167, -127.775))

class Part10220_410003_1_419227(AssemblyNode):
    transmission_gear_0_6 = TransmissionGear0_6()
    pentagonal_lockout = PentagonalLockout()
    p_1_9mm_spacer = Part1_9mmSpacer()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()

    def render(self):
        self.transmission_gear_0_6.translate((38.137315415, -13.851815805, -33.6))
        self.pentagonal_lockout.translate((38.137315415, -13.851815805, -26.1))
        self.p_1_9mm_spacer.translate((38.137315415, -13.851815805, -31.8))
        self.p_1_3mm_spacer.translate((38.137315415, -13.851815805, -39.0))
        self.p_4_8mm_tens_ratchet_sleeve.translate((38.137315415, -13.851815805, -24.6))

class Part10207_1_419228(AssemblyNode):
    transmission_gear_tip = TransmissionGearTip()
    transmission_shaft = TransmissionShaft()

    def render(self):
        self.transmission_gear_tip.translate((38.137315415, -13.851815805, 22.05))
        self.transmission_shaft.translate((38.137315415, -13.851815805, -140.1))

class Part10230_410008_1_419229(AssemblyNode):
    p_1_6mm_spacer = Part1_6mmSpacer()
    transmission_gear_0_5 = TransmissionGear0_5()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()

    def render(self):
        self.p_1_6mm_spacer.translate((38.137315415, -13.851815805, -70.92499975))
        self.transmission_gear_0_5.translate((38.137315415, -13.851815805, -64.92499975))
        self.p_2_5mm_lockout_sleeve.translate((38.137315415, -13.851815805, -63.42499975))

class Part10236_1(AssemblyNode):
    p_10220_410003_1_419227 = Part10220_410003_1_419227()
    p_10207_1_419228 = Part10207_1_419228()
    p_10230_410008_1_419229 = Part10230_410008_1_419229()

class DecimalMarker1(AssemblyNode):
    p_3mm_ball = Part3mmBall()
    decimal_marker_spring = DecimalMarkerSpring()
    position_marker = PositionMarker()

    def render(self):
        self.p_3mm_ball.rotate(152.582314946, (0.380724916, -0.10104211, 0.919151255))
        self.p_3mm_ball.translate((63.423835516, -35.701907063, -143.609910838))
        self.decimal_marker_spring.rotate(-136.583685305, (0.255078254, 0.961130433, 0.105656872))
        self.decimal_marker_spring.translate((66.279178679, -37.332325849, -140.321864305))
        self.position_marker.rotate(152.582314946, (0.380724916, -0.10104211, 0.919151255))
        self.position_marker.translate((62.963296296, -35.43893629, -144.140240924))

class Part10230_410008_1_419232(AssemblyNode):
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()
    transmission_gear_0_5 = TransmissionGear0_5()
    p_1_6mm_spacer = Part1_6mmSpacer()

    def render(self):
        self.p_2_5mm_lockout_sleeve.translate((20.25, -35.074028853, -63.42499975))
        self.transmission_gear_0_5.translate((20.25, -35.074028853, -64.92499975))
        self.p_1_6mm_spacer.translate((20.25, -35.074028853, -70.92499975))

class Part10207_1_419233(AssemblyNode):
    transmission_shaft = TransmissionShaft()
    transmission_gear_tip = TransmissionGearTip()

    def render(self):
        self.transmission_shaft.translate((20.25, -35.074028853, -140.1))
        self.transmission_gear_tip.translate((20.25, -35.074028853, 22.05))

class Part10220_410003_1_419234(AssemblyNode):
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()
    transmission_gear_0_6 = TransmissionGear0_6()
    pentagonal_lockout = PentagonalLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()
    p_1_9mm_spacer = Part1_9mmSpacer()

    def render(self):
        self.p_4_8mm_tens_ratchet_sleeve.translate((20.25, -35.074028853, -20.4))
        self.transmission_gear_0_6.translate((20.25, -35.074028853, -29.4))
        self.pentagonal_lockout.translate((20.25, -35.074028853, -21.9))
        self.p_1_3mm_spacer.translate((20.25, -35.074028853, -34.8))
        self.p_1_9mm_spacer.translate((20.25, -35.074028853, -27.6))

class Part10236_3(AssemblyNode):
    p_10230_410008_1_419232 = Part10230_410008_1_419232()
    p_10207_1_419233 = Part10207_1_419233()
    p_10220_410003_1_419234 = Part10220_410003_1_419234()

class Part10207_1_419236(AssemblyNode):
    transmission_shaft = TransmissionShaft()
    transmission_gear_tip = TransmissionGearTip()

    def render(self):
        self.transmission_shaft.translate((35.074028853, 20.25, -140.1))
        self.transmission_gear_tip.translate((35.074028853, 20.25, 22.05))

class Part10230_410008_1_419237(AssemblyNode):
    p_1_6mm_spacer = Part1_6mmSpacer()
    transmission_gear_0_5 = TransmissionGear0_5()
    p_2_5mm_lockout_sleeve = Part2_5mmLockoutSleeve()

    def render(self):
        self.p_1_6mm_spacer.translate((35.074028853, 20.25, -50.85))
        self.transmission_gear_0_5.translate((35.074028853, 20.25, -44.85))
        self.p_2_5mm_lockout_sleeve.translate((35.074028853, 20.25, -43.35))

class Part10220_410003_1_419238(AssemblyNode):
    p_1_9mm_spacer = Part1_9mmSpacer()
    pentagonal_lockout = PentagonalLockout()
    p_1_3mm_spacer = Part1_3mmSpacer()
    transmission_gear_0_6 = TransmissionGear0_6()
    p_4_8mm_tens_ratchet_sleeve = Part4_8mmTensRatchetSleeve()

    def render(self):
        self.p_1_9mm_spacer.translate((35.074028853, 20.25, -14.7))
        self.pentagonal_lockout.translate((35.074028853, 20.25, -9.0))
        self.p_1_3mm_spacer.translate((35.074028853, 20.25, -21.9))
        self.transmission_gear_0_6.translate((35.074028853, 20.25, -16.5))
        self.p_4_8mm_tens_ratchet_sleeve.translate((35.074028853, 20.25, -7.5))

class Part10236_12(AssemblyNode):
    p_10207_1_419236 = Part10207_1_419236()
    p_10230_410008_1_419237 = Part10230_410008_1_419237()
    p_10220_410003_1_419238 = Part10220_410003_1_419238()

class DecimalMarker8(AssemblyNode):
    position_marker = PositionMarker()
    p_3mm_ball = Part3mmBall()
    decimal_marker_spring = DecimalMarkerSpring()

    def render(self):
        self.position_marker.rotate(151.766652726, (0.380601389, -0.10417141, 0.918853035))
        self.position_marker.translate((47.366368705, -27.827927155, 49.038982694))
        self.p_3mm_ball.rotate(151.766652726, (0.380601389, -0.10417141, 0.918853035))
        self.p_3mm_ball.translate((47.822779234, -28.098000162, 49.56931278))
        self.decimal_marker_spring.rotate(-136.67881293, (0.262428175, 0.958809407, 0.108701309))
        self.decimal_marker_spring.translate((50.652524514, -29.772452803, 52.857359313))

class Part10204_3(AssemblyNode):
    number_roll_carry_pin_full = NumberRollCarryPinFull()
    results_dial_type_2 = ResultsDialType2()

    def render(self):
        self.number_roll_carry_pin_full.rotate(-90.0, (0.870784372, -0.491665107, 0.0))
        self.number_roll_carry_pin_full.translate((-35.976366118, -56.908002337, 27.107881898))
        self.results_dial_type_2.rotate(-90.0, (0.870784372, -0.491665107, 0.0))
        self.results_dial_type_2.translate((-34.603579072, -62.276669529, 33.9))

class Part10205_4(AssemblyNode):
    results_dial_type_2 = ResultsDialType2()
    number_roll_carry_pin_half = NumberRollCarryPinHalf()

    def render(self):
        self.results_dial_type_2.rotate(90.0, (0.942931951, -0.33298549, 0.0))
        self.results_dial_type_2.translate((24.337545072, 67.35699514, 33.9))
        self.number_roll_carry_pin_half.rotate(93.123980698, (0.817173473, -0.529667053, 0.227333079))
        self.number_roll_carry_pin_half.translate((20.556538384, 64.450126162, 41.254869215))

class Part10205_1(AssemblyNode):
    results_dial_type_2 = ResultsDialType2()
    number_roll_carry_pin_half = NumberRollCarryPinHalf()

    def render(self):
        self.results_dial_type_2.rotate(-90.0, (0.635405729, 0.772178451, 0.0))
        self.results_dial_type_2.translate((55.72844801, -45.453202839, 33.9))
        self.number_roll_carry_pin_half.rotate(-93.123980698, (0.777214009, 0.586735081, -0.227333079))
        self.number_roll_carry_pin_half.translate((56.466777773, -38.260755356, 28.943835317))

class Part10204_6(AssemblyNode):
    results_dial_type_2 = ResultsDialType2()
    number_roll_carry_pin_full = NumberRollCarryPinFull()

    def render(self):
        self.results_dial_type_2.rotate(90.0, (-0.009597713, 0.999953941, 0.0))
        self.results_dial_type_2.translate((-70.933044396, -0.724164791, 33.9))
        self.number_roll_carry_pin_full.rotate(90.0, (-0.009597713, 0.999953941, 0.0))
        self.number_roll_carry_pin_full.translate((-67.008087348, 7.113507556, 33.825137837))

class Part10203_3(AssemblyNode):
    number_roll_carry_pin_half = NumberRollCarryPinHalf()
    results_dial_type_1 = ResultsDialType1()

    def render(self):
        self.number_roll_carry_pin_half.rotate(112.563116284, (0.849447328, 0.033745479, 0.526593278))
        self.number_roll_carry_pin_half.translate((-43.327857244, 51.231301676, 41.7))
        self.results_dial_type_1.rotate(96.896723418, (0.886333255, 0.327424313, 0.327424313))
        self.results_dial_type_1.translate((-45.928298358, 54.270661151, 33.9))

class Part10203_4(AssemblyNode):
    number_roll_carry_pin_half = NumberRollCarryPinHalf()
    results_dial_type_1 = ResultsDialType1()

    def render(self):
        self.number_roll_carry_pin_half.rotate(102.967296238, (0.895529378, -0.121478899, 0.428100468))
        self.number_roll_carry_pin_half.translate((-23.147244639, 63.142285136, 41.7))
        self.results_dial_type_1.rotate(91.823266661, (0.968673782, 0.175600548, 0.175600548))
        self.results_dial_type_1.translate((-24.5513378, 66.887752049, 33.9))

class Part10204_1(AssemblyNode):
    results_dial_type_2 = ResultsDialType2()
    number_roll_carry_pin_full = NumberRollCarryPinFull()

    def render(self):
        self.results_dial_type_2.rotate(-90.0, (0.983095768, 0.183092082, 0.0))
        self.results_dial_type_2.translate((13.624055025, -70.304020713, 33.9))
        self.number_roll_carry_pin_full.rotate(-90.0, (0.983095768, 0.183092082, 0.0))
        self.number_roll_carry_pin_full.translate((14.295663695, -66.110160498, 26.231853008))

class Part10205_2(AssemblyNode):
    results_dial_type_2 = ResultsDialType2()
    number_roll_carry_pin_half = NumberRollCarryPinHalf()

    def render(self):
        self.results_dial_type_2.rotate(-90.0, (0.861186659, 0.508288834, 0.0))
        self.results_dial_type_2.translate((36.867186359, -61.590682021, 33.9))
        self.number_roll_carry_pin_half.rotate(-93.123980698, (0.931017486, 0.285527779, -0.227333079))
        self.number_roll_carry_pin_half.translate((38.248337212, -56.130746584, 27.182744061))

class Part10204_2(AssemblyNode):
    results_dial_type_2 = ResultsDialType2()
    number_roll_carry_pin_full = NumberRollCarryPinFull()

    def render(self):
        self.results_dial_type_2.rotate(-90.0, (0.986429019, -0.164188277, 0.0))
        self.results_dial_type_2.translate((-11.197481322, -70.542261674, 33.9))
        self.number_roll_carry_pin_full.rotate(-90.0, (0.986429019, -0.164188277, 0.0))
        self.number_roll_carry_pin_full.translate((-11.804016847, -66.386274833, 26.205853651))

class Part10204_4(AssemblyNode):
    number_roll_carry_pin_full = NumberRollCarryPinFull()
    results_dial_type_2 = ResultsDialType2()

    def render(self):
        self.number_roll_carry_pin_full.rotate(90.0, (-0.650110278, 0.759839869, 0.0))
        self.number_roll_carry_pin_full.translate((-54.584799651, -39.40037388, 28.829139829))
        self.results_dial_type_2.rotate(90.0, (-0.650110278, 0.759839869, 0.0))
        self.results_dial_type_2.translate((-53.771117399, -46.504196676, 33.9))

class Part10203_1(AssemblyNode):
    number_roll_carry_pin_half = NumberRollCarryPinHalf()
    results_dial_type_1 = ResultsDialType1()

    def render(self):
        self.number_roll_carry_pin_half.rotate(-101.667894174, (-0.41794362, 0.810620014, 0.410144271))
        self.number_roll_carry_pin_half.translate((68.008670778, 0.609419372, 41.7))
        self.results_dial_type_1.rotate(119.683014833, (0.581044468, -0.575494277, -0.575494277))
        self.results_dial_type_1.translate((72.008486542, 0.647810225, 33.9))

class Part10204_7(AssemblyNode):
    results_dial_type_2 = ResultsDialType2()
    number_roll_carry_pin_full = NumberRollCarryPinFull()

    def render(self):
        self.results_dial_type_2.rotate(90.0, (0.772178451, -0.635405729, 0.0))
        self.results_dial_type_2.translate((45.952746591, 55.152549691, 33.9))
        self.number_roll_carry_pin_full.rotate(90.0, (0.772178451, -0.635405729, 0.0))
        self.number_roll_carry_pin_full.translate((39.584080109, 55.213011319, 39.922991917))

class Part10204_5(AssemblyNode):
    number_roll_carry_pin_full = NumberRollCarryPinFull()
    results_dial_type_2 = ResultsDialType2()

    def render(self):
        self.number_roll_carry_pin_full.rotate(90.0, (-0.35102329, 0.936366728, 0.0))
        self.number_roll_carry_pin_full.translate((-65.206496319, -16.88423829, 31.162018334))
        self.results_dial_type_2.rotate(90.0, (-0.35102329, 0.936366728, 0.0))
        self.results_dial_type_2.translate((-66.388208297, -25.127236119, 33.9))

class Part10203_2(AssemblyNode):
    results_dial_type_1 = ResultsDialType1()
    number_roll_carry_pin_half = NumberRollCarryPinHalf()

    def render(self):
        self.results_dial_type_1.rotate(-91.635101119, (0.166560565, 0.971861696, 0.166560565))
        self.results_dial_type_1.translate((67.932893459, -23.838001321, 33.9))
        self.number_roll_carry_pin_half.rotate(-91.186911591, (0.460484172, 0.876162461, -0.142455852))
        self.number_roll_carry_pin_half.translate((66.758452477, -15.151190146, 33.9))

class UpperCarriageBody1(AssemblyNode):
    digits_axle_1 = DigitsAxle()
    digits_axle_2 = DigitsAxle()
    digits_axle_3 = DigitsAxle()
    digits_axle_4 = DigitsAxle()
    counter_body_pin_1 = CounterBodyPin()
    digits_axle_5 = DigitsAxle()
    clearing_pin = ClearingPin()
    counter_body_stop_pin = CounterBodyStopPin()
    counter_body_pin_2 = CounterBodyPin()
    digits_axle_6 = DigitsAxle()
    digits_axle_7 = DigitsAxle()
    digits_axle_8 = DigitsAxle()
    digits_axle_9 = DigitsAxle()
    digits_axle_10 = DigitsAxle()
    digits_axle_11 = DigitsAxle()
    digits_axle_12 = DigitsAxle()
    digits_axle_13 = DigitsAxle()
    digits_axle_14 = DigitsAxle()
    counter_body = CounterBody()
    digits_axle_15 = DigitsAxle()
    clearing_stop_pin_sleeve = ClearingStopPinSleeve()
    digits_axle_16 = DigitsAxle()
    clearing_pin_spring = ClearingPinSpring()
    digits_axle_17 = DigitsAxle()

    def render(self):
        self.digits_axle_1.rotate(100.075449365, (0.385870743, 0.837978245, -0.385870743))
        self.digits_axle_1.translate((-47.293529942, 55.866324875, 33.9))
        self.digits_axle_2.rotate(-152.385861218, (0.685421323, -0.24575439, -0.685421323))
        self.digits_axle_2.translate((57.350022757, -46.787554869, 33.9))
        self.digits_axle_3.rotate(119.683014833, (0.575494277, 0.581044468, -0.575494277))
        self.digits_axle_3.translate((-0.168421671, 73.532491424, 33.9))
        self.digits_axle_4.rotate(-131.796946865, (-0.632406026, -0.447353592, 0.632406026))
        self.digits_axle_4.translate((25.036814601, 69.337152237, 33.9))
        self.counter_body_pin_1.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.counter_body_pin_1.translate((-20.461311724, -0.239729261, 49.5))
        self.digits_axle_5.rotate(90.001319496, (-0.004798857, 0.999976971, 0.004798857))
        self.digits_axle_5.translate((-73.032947672, -0.744319989, 33.9))
        self.clearing_pin.rotate(-179.450083095, (0.0, 0.0, 1.0))
        self.clearing_pin.translate((29.439639004, 8.004156813, 21.6))
        self.counter_body_stop_pin.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.counter_body_stop_pin.translate((-23.260793032, 16.287579306, 35.544410518))
        self.counter_body_pin_2.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.counter_body_pin_2.translate((21.536753794, 0.163374695, 49.5))
        self.digits_axle_6.rotate(-166.279900138, (0.701970973, -0.120305885, -0.701970973))
        self.digits_axle_6.translate((69.913050555, -24.537270849, 33.9))
        self.digits_axle_7.rotate(91.823266661, (-0.175600548, 0.968673782, 0.175600548))
        self.digits_axle_7.translate((-68.354578426, -25.864385029, 33.9))
        self.digits_axle_8.rotate(96.896723418, (-0.327424313, 0.886333255, 0.327424313))
        self.digits_axle_8.translate((-55.366781123, -47.86942826, 33.9))
        self.digits_axle_9.rotate(144.855498385, (0.670712366, 0.316685717, -0.670712366))
        self.digits_axle_9.translate((47.287098621, 56.774124438, 33.9))
        self.digits_axle_10.rotate(-126.266796884, (0.609655748, -0.506596228, -0.609655748))
        self.digits_axle_10.translate((14.008548397, -72.368521826, 33.9))
        self.digits_axle_11.rotate(104.724258057, (-0.450175858, 0.771157178, 0.450175858))
        self.digits_axle_11.translate((-35.636075797, -64.10531671, 33.9))
        self.digits_axle_12.rotate(91.635101119, (0.166560565, 0.971861696, -0.166560565))
        self.digits_axle_12.translate((-68.837608485, 24.460916283, 33.9))
        self.digits_axle_13.rotate(-138.950666871, (0.655684002, -0.374375453, -0.655684002))
        self.digits_axle_13.translate((37.93459291, -63.399174004, 33.9))
        self.digits_axle_14.rotate(114.702446195, (-0.542894613, 0.640726836, 0.542894613))
        self.digits_axle_14.translate((-11.542276705, -72.613762614, 33.9))
        self.counter_body.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.counter_body.translate((0.537721035, -0.038177283, 45.0))
        self.digits_axle_15.rotate(158.527493838, (0.69427986, 0.189607366, -0.69427986))
        self.digits_axle_15.translate((63.898717756, 37.358694592, 33.9))
        self.clearing_stop_pin_sleeve.rotate(-179.450083095, (0.0, 0.0, 1.0))
        self.clearing_stop_pin_sleeve.translate((29.439639004, 8.004156813, 25.5))
        self.digits_axle_16.rotate(179.611150774, (0.70710271, 0.003393363, -0.70710271))
        self.digits_axle_16.translate((74.108389818, 0.667965423, 33.9))
        self.clearing_pin_spring.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.clearing_pin_spring.translate((29.439639004, 8.004156813, 48.0))
        self.digits_axle_17.rotate(108.934580006, (0.494966135, 0.714154781, -0.494966135))
        self.digits_axle_17.translate((-25.288486711, 68.854122178, 33.9))

class Part10205_3(AssemblyNode):
    results_dial_type_2 = ResultsDialType2()
    number_roll_carry_pin_half = NumberRollCarryPinHalf()

    def render(self):
        self.results_dial_type_2.rotate(90.0, (0.999953941, 0.009597713, 0.0))
        self.results_dial_type_2.translate((-0.148266473, 71.432588148, 33.9))
        self.number_roll_carry_pin_half.rotate(93.123980698, (0.949048683, -0.218234433, 0.227333079))
        self.number_roll_carry_pin_half.translate((-0.035016905, 67.43349089, 41.699640739))

class Carriage1(AssemblyNode):
    p_6mm_ball_419241_1 = Part6mmBall419241()
    crank_collar_washer = CrankCollarWasher()
    p_10204_3 = Part10204_3()
    p_10205_4 = Part10205_4()
    p_6mm_ball_419241_2 = Part6mmBall419241()
    p_6mm_ball_419241_3 = Part6mmBall419241()
    crank_collar_nut = CrankCollarNut()
    p_6mm_ball_419241_4 = Part6mmBall419241()
    results_dial_type_2_1 = ResultsDialType2()
    p_6mm_ball_419241_5 = Part6mmBall419241()
    clearing_ring_rivet_1 = ClearingRingRivet()
    p_10205_1 = Part10205_1()
    p_6mm_ball_419241_6 = Part6mmBall419241()
    p_6mm_ball_419241_7 = Part6mmBall419241()
    p_6mm_ball_419241_8 = Part6mmBall419241()
    results_dial_type_2_2 = ResultsDialType2()
    p_10204_6 = Part10204_6()
    p_10203_3 = Part10203_3()
    p_10203_4 = Part10203_4()
    p_10204_1 = Part10204_1()
    digits_cover = DigitsCover()
    p_6mm_ball_419241_9 = Part6mmBall419241()
    p_6mm_ball_419241_10 = Part6mmBall419241()
    p_6mm_ball_419241_11 = Part6mmBall419241()
    upper_housing = UpperHousing()
    p_6mm_ball_419241_12 = Part6mmBall419241()
    clearing_ring_rivet_2 = ClearingRingRivet()
    p_6mm_ball_419241_13 = Part6mmBall419241()
    crank_collar = CrankCollar()
    p_6mm_ball_419241_14 = Part6mmBall419241()
    p_10205_2 = Part10205_2()
    p_10204_2 = Part10204_2()
    p_6mm_ball_419241_15 = Part6mmBall419241()
    p_10204_4 = Part10204_4()
    p_10203_1 = Part10203_1()
    p_10204_7 = Part10204_7()
    p_6mm_ball_419241_16 = Part6mmBall419241()
    p_10204_5 = Part10204_5()
    p_10203_2 = Part10203_2()
    clearing_cover = ClearingCover()
    spider_spring = SpiderSpring()
    upper_carriage_body_1 = UpperCarriageBody1()
    p_6mm_ball_419241_17 = Part6mmBall419241()
    p_10205_3 = Part10205_3()
    clearing_ring = ClearingRing()

    def render(self):
        self.p_6mm_ball_419241_1.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_1.translate((41.611836805, -14.543025222, 43.35))
        self.crank_collar_washer.rotate(180.0, (0.797150916, -0.603780106, 0.0))
        self.crank_collar_washer.translate((0.0, 0.0, 60.3))
        self.p_6mm_ball_419241_2.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_2.translate((-27.78108269, 33.060447395, 43.35))
        self.p_6mm_ball_419241_3.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_3.translate((-6.614320319, -43.007025353, 43.35))
        self.crank_collar_nut.rotate(-54.282220532, (0.0, 0.0, 1.0))
        self.crank_collar_nut.translate((0.0, 0.0, 12.3))
        self.p_6mm_ball_419241_4.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_4.translate((-32.560903643, -28.356981008, 43.35))
        self.results_dial_type_2_1.rotate(109.481790438, (0.706968432, 0.500097809, 0.500097809))
        self.results_dial_type_2_1.translate((-66.857451389, 23.761646754, 33.9))
        self.p_6mm_ball_419241_5.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_5.translate((-40.536394735, 14.466670656, 43.35))
        self.clearing_ring_rivet_1.rotate(-74.282220532, (0.0, 0.0, 1.0))
        self.clearing_ring_rivet_1.translate((39.372124643, 10.943003894, 50.5))
        self.p_6mm_ball_419241_6.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_6.translate((28.215994571, 33.59791604, 43.35))
        self.p_6mm_ball_419241_7.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_7.translate((-20.879211024, -37.969544529, 43.35))
        self.p_6mm_ball_419241_8.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_8.translate((-43.02027263, -0.456253672, 43.35))
        self.results_dial_type_2_2.rotate(104.232401654, (0.778024743, -0.444228263, -0.444228263))
        self.results_dial_type_2_2.translate((62.090225773, 36.291288041, 33.9))
        self.digits_cover.rotate(-180.0, (0.168920173, 0.985629735, 0.0))
        self.digits_cover.translate((0.386511579, -0.028412332, 31.6))
        self.p_6mm_ball_419241_9.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_9.translate((0.119644646, 43.519816382, 43.35))
        self.p_6mm_ball_419241_10.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_10.translate((15.042568974, 41.035938487, 43.35))
        self.p_6mm_ball_419241_11.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_11.translate((8.513212127, -42.861828947, 43.35))
        self.upper_housing.rotate(160.549916905, (0.0, 0.0, 1.0))
        self.upper_housing.translate((0.386511579, -0.028412332, -4.4))
        self.p_6mm_ball_419241_12.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_12.translate((44.0957147, 0.379899106, 43.35))
        self.clearing_ring_rivet_2.rotate(-74.282220532, (0.0, 0.0, 1.0))
        self.clearing_ring_rivet_2.translate((37.348717788, -16.582726336, 50.5))
        self.p_6mm_ball_419241_13.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_13.translate((34.173814358, -27.716450819, 43.35))
        self.crank_collar.rotate(-144.282220532, (0.0, 0.0, 1.0))
        self.crank_collar.translate((0.0, 0.0, 7.8))
        self.p_6mm_ball_419241_14.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_14.translate((-14.752853499, 40.749957394, 43.35))
        self.p_6mm_ball_419241_15.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_15.translate((38.051011892, 22.102884323, 43.35))
        self.p_6mm_ball_419241_16.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_16.translate((22.678782641, -37.551468141, 43.35))
        self.clearing_cover.rotate(180.0, (0.797150916, -0.603780106, 0.0))
        self.clearing_cover.translate((0.386511579, -0.028412332, 57.1))
        self.spider_spring.rotate(0.549916905, (0.0, 0.0, 1.0))
        self.spider_spring.translate((0.537721035, -0.038177283, 45.2))
        self.p_6mm_ball_419241_17.rotate(-180.0, (-0.004798912, 0.999988485, 0.0))
        self.p_6mm_ball_419241_17.translate((-40.250413642, -15.328751817, 43.35))
        self.clearing_ring.rotate(180.0, (0.603780106, 0.797150916, 0.0))
        self.clearing_ring.translate((50.343540869, -28.04260917, 62.56))

class CurtaAssembly(AssemblyNode):
    m4_nut_1 = M4Nut()
    cover_ring = CoverRing()
    m3x10_pan_1 = M3x10Pan()
    m4x16_hex_1 = M4x16Hex()
    thrust_ring = ThrustRing()
    m4x16_hex_2 = M4x16Hex()
    carriage_spring_sleeve = CarriageSpringSleeve()
    selector_shaft_bearing_1 = SelectorShaftBearing()
    m4x10_419010_1 = M4x10_419010()
    m3x10_countersink_screw_1 = M3x10CountersinkScrew()
    m4x16_hex_3 = M4x16Hex()
    m4_nut_2 = M4Nut()
    m4x16_hex_4 = M4x16Hex()
    selector_shaft_bearing_2 = SelectorShaftBearing()
    spring_sleeve_c_clip = SpringSleeveCClip()
    selector_shaft_bearing_3 = SelectorShaftBearing()
    m4x16_hex_5 = M4x16Hex()
    results_tens_lever_assembly_10 = ResultsTensLeverAssembly10()
    upper_outer_sleeve = UpperOuterSleeve()
    carriage_spring = CarriageSpring()
    crank_handle_1 = CrankHandle1()
    m5x30_countersunk_1 = M5x30Countersunk()
    results_tens_lever_assembly_8 = ResultsTensLeverAssembly8()
    m3x10_pan_2 = M3x10Pan()
    results_tens_lever_assembly_5 = ResultsTensLeverAssembly5()
    decimal_marker_7 = DecimalMarker7()
    results_tens_lever_assembly_2 = ResultsTensLeverAssembly2()
    p_10236_6 = Part10236_6()
    turns_tens_lever_assembly_5 = TurnsTensLeverAssembly5()
    turns_tens_lever_assembly_3 = TurnsTensLeverAssembly3()
    results_tens_lever_assembly_4 = ResultsTensLeverAssembly4()
    selector_shaft_bearing_4 = SelectorShaftBearing()
    crank_handle_pin = CrankHandlePin()
    selector_shaft_bearing_5 = SelectorShaftBearing()
    m3x10_countersink_screw_2 = M3x10CountersinkScrew()
    turns_tens_lever_assembly_2 = TurnsTensLeverAssembly2()
    decimal_marker_10 = DecimalMarker10()
    digit_selector_axle_1 = DigitSelectorAxle1()
    m4x16_hex_6 = M4x16Hex()
    decimal_marker_2 = DecimalMarker2()
    m4x16_hex_7 = M4x16Hex()
    m4x10_419010_2 = M4x10_419010()
    m4x16_hex_8 = M4x16Hex()
    m4x16_hex_9 = M4x16Hex()
    p_10236_5 = Part10236_5()
    m4x10_419010_3 = M4x10_419010()
    p_10236_9 = Part10236_9()
    m4x10_419010_4 = M4x10_419010()
    m4x16_hex_10 = M4x16Hex()
    m4x10_419010_5 = M4x10_419010()
    decimal_marker_9 = DecimalMarker9()
    selector_shaft_bearing_6 = SelectorShaftBearing()
    results_tens_lever_assembly_6 = ResultsTensLeverAssembly6()
    p_10236_7 = Part10236_7()
    decimal_marker_4 = DecimalMarker4()
    p_10236_8 = Part10236_8()
    digit_selector_axle_4 = DigitSelectorAxle4()
    p_10236_2 = Part10236_2()
    setting_axle_holding_plate_1 = SettingAxleHoldingPlate()
    m4x16_hex_11 = M4x16Hex()
    m4x10_419010_6 = M4x10_419010()
    p_10236_4 = Part10236_4()
    m4x16_hex_12 = M4x16Hex()
    p_6mm_ball_419094 = Part6mmBall419094()
    lower_housing_1 = LowerHousing1()
    turns_tens_lever_assembly_4 = TurnsTensLeverAssembly4()
    m4x16_hex_13 = M4x16Hex()
    decimal_marker_6 = DecimalMarker6()
    turns_tens_lever_assembly_1 = TurnsTensLeverAssembly1()
    m4x16_hex_14 = M4x16Hex()
    m3x10_pan_3 = M3x10Pan()
    digit_selector_axle_7 = DigitSelectorAxle7()
    m4x16_hex_15 = M4x16Hex()
    p_10236_11 = Part10236_11()
    m4_nut_3 = M4Nut()
    selector_shaft_bearing_7 = SelectorShaftBearing()
    results_tens_lever_assembly_3 = ResultsTensLeverAssembly3()
    p_10238_3 = Part10238_3()
    p_10238_2 = Part10238_2()
    m5x30_countersunk_2 = M5x30Countersunk()
    results_tens_lever_assembly_9 = ResultsTensLeverAssembly9()
    p_10239_1 = Part10239_1()
    p_10237_1 = Part10237_1()
    p_10238_1 = Part10238_1()
    digit_selector_axle_6 = DigitSelectorAxle6()
    reversing_lever_1 = ReversingLever1()
    selector_shaft_bearing_8 = SelectorShaftBearing()
    m3x10_countersink_screw_3 = M3x10CountersinkScrew()
    results_tens_lever_assembly_7 = ResultsTensLeverAssembly7()
    m4_nut_4 = M4Nut()
    digit_selector_axle_2 = DigitSelectorAxle2()
    digit_selector_axle_8 = DigitSelectorAxle8()
    decimal_marker_5 = DecimalMarker5()
    upper_frame_1 = UpperFrame1()
    digit_selector_axle_5 = DigitSelectorAxle5()
    p_10236_10 = Part10236_10()
    setting_axle_holding_plate_2 = SettingAxleHoldingPlate()
    lower_frame_1 = LowerFrame1()
    decimal_marker_3 = DecimalMarker3()
    base_plate = BasePlate()
    results_tens_lever_assembly_1 = ResultsTensLeverAssembly1()
    digit_selector_axle_3 = DigitSelectorAxle3()
    p_10236_1 = Part10236_1()
    decimal_marker_1 = DecimalMarker1()
    p_10236_3 = Part10236_3()
    p_10236_12 = Part10236_12()
    decimal_marker_8 = DecimalMarker8()
    carriage_1 = Carriage1()

    def render(self):
        self.m4_nut_1.translate((-52.84947971, -21.352575825, -142.05))
        self.cover_ring.translate((0.0, 0.0, 22.2))
        self.m3x10_pan_1.translate((47.523550653, 12.733897019, 15.0))
        self.m4x16_hex_1.rotate(100.288585137, (0.834817129, 0.389281621, 0.389281621))
        self.m4x16_hex_1.translate((25.787362927, -39.77027397, 4.8))
        self.thrust_ring.rotate(35.717779468, (0.0, 0.0, 1.0))
        self.thrust_ring.translate((0.0, 0.0, 25.5225))
        self.m4x16_hex_2.rotate(-91.727941072, (0.970287525, -0.17108787, 0.17108787))
        self.m4x16_hex_2.translate((28.552035412, 37.834429455, 4.8))
        self.carriage_spring_sleeve.rotate(180.0, (1.0, 0.0, 0.0))
        self.carriage_spring_sleeve.translate((0.0, 0.0, 57.6))
        self.selector_shaft_bearing_1.rotate(-155.687762595, (0.0, 0.0, 1.0))
        self.selector_shaft_bearing_1.translate((-10.158418394, -57.611253551, -138.275))
        self.m4x10_419010_1.rotate(47.531056002, (-0.129842301, 0.94068028, 0.313467044))
        self.m4x10_419010_1.translate((43.908248282, 12.219569698, 45.574328291))
        self.m3x10_countersink_screw_1.rotate(165.893955739, (0.701673843, -0.12372403, 0.701673843))
        self.m3x10_countersink_screw_1.translate((55.969284246, -20.371153499, 19.8))
        self.m4x16_hex_3.rotate(100.288585137, (0.834817129, -0.389281621, -0.389281621))
        self.m4x16_hex_3.translate((-43.644002724, -18.48955934, 4.8))
        self.m4_nut_2.translate((17.613968679, 54.210221429, -15.9))
        self.m4x16_hex_4.rotate(90.435230002, (0.992432509, 0.086826594, 0.086826594))
        self.m4x16_hex_4.translate((-5.809573269, -47.041594752, 4.8))
        self.selector_shaft_bearing_2.rotate(103.351337657, (0.0, 0.0, 1.0))
        self.selector_shaft_bearing_2.translate((-29.25, -50.662486121, -138.275))
        self.spring_sleeve_c_clip.translate((0.0, 0.0, 57.6))
        self.selector_shaft_bearing_3.rotate(-57.6058828, (0.0, 0.0, 1.0))
        self.selector_shaft_bearing_3.translate((29.25, -50.662486121, -138.275))
        self.m4x16_hex_5.rotate(-91.727941072, (0.970287525, 0.17108787, -0.17108787))
        self.m4x16_hex_5.translate((-2.447374406, 47.335749037, 4.8))
        self.upper_outer_sleeve.translate((0.0, 0.0, -40.2))
        self.carriage_spring.rotate(35.717779468, (0.0, 0.0, 1.0))
        self.carriage_spring.translate((0.0, 0.0, 27.0225))
        self.m5x30_countersunk_1.rotate(-70.0, (0.0, 0.0, 1.0))
        self.m5x30_countersunk_1.translate((19.088247813, -52.816637436, -186.75))
        self.m3x10_pan_2.translate((-16.827391052, -46.232876943, 15.0))
        self.selector_shaft_bearing_4.rotate(-20.373054183, (0.0, 0.0, 1.0))
        self.selector_shaft_bearing_4.translate((-44.813599922, -37.603075167, -138.275))
        self.crank_handle_pin.rotate(90.989717347, (0.982873666, 0.130306093, 0.130306093))
        self.crank_handle_pin.translate((-5.507637771, 20.444630619, 74.85))
        self.selector_shaft_bearing_5.rotate(144.2101172, (0.0, 0.0, 1.0))
        self.selector_shaft_bearing_5.translate((44.813599922, -37.603075167, -138.275))
        self.m3x10_countersink_screw_2.rotate(92.900575802, (0.950614905, -0.219466743, -0.219466743))
        self.m3x10_countersink_screw_2.translate((-26.109941461, -53.533313281, 19.8))
        self.m4x16_hex_6.rotate(180.0, (0.707106781, 0.0, 0.707106781))
        self.m4x16_hex_6.translate((45.318105414, -13.89, 4.8))
        self.m4x16_hex_7.rotate(109.207479725, (0.710564775, -0.497542812, -0.497542812))
        self.m4x16_hex_7.translate((-47.335749037, -2.447374406, 4.8))
        self.m4x10_419010_2.rotate(180.0, (0.984807753, -0.173648178, 0.0))
        self.m4x10_419010_2.translate((-36.638893752, -43.664533258, -132.45))
        self.m4x16_hex_8.rotate(-90.0, (1.0, 0.0, 0.0))
        self.m4x16_hex_8.translate((13.89, 45.318105414, 4.8))
        self.m4x16_hex_9.rotate(-96.717713464, (0.889126491, 0.323615577, -0.323615577))
        self.m4x16_hex_9.translate((-18.48955934, 43.644002724, 4.8))
        self.m4x10_419010_3.rotate(180.0, (0.965925826, -0.258819045, 0.0))
        self.m4x10_419010_3.translate((36.638893752, -43.664533258, -132.45))
        self.m4x10_419010_4.rotate(180.0, (0.984807753, -0.173648178, 0.0))
        self.m4x10_419010_4.translate((0.009118459, -57.003318847, -132.45))
        self.m4x16_hex_10.rotate(120.0, (0.577350269, -0.577350269, -0.577350269))
        self.m4x16_hex_10.translate((-45.318105414, 13.89, 4.8))
        self.m4x10_419010_5.rotate(180.0, (0.965925826, -0.258819045, 0.0))
        self.m4x10_419010_5.translate((56.138893752, -9.88954251, -132.45))
        self.selector_shaft_bearing_6.rotate(-177.191062484, (0.0, 0.0, 1.0))
        self.selector_shaft_bearing_6.translate((58.5, 0.0, -138.275))
        self.setting_axle_holding_plate_1.rotate(60.0, (0.0, 0.0, 1.0))
        self.setting_axle_holding_plate_1.translate((0.003955464, 0.003318723, -141.45))
        self.m4x16_hex_11.rotate(90.435230002, (0.992432509, -0.086826594, -0.086826594))
        self.m4x16_hex_11.translate((-21.54838611, -42.217648376, 4.8))
        self.m4x10_419010_6.rotate(83.262779635, (-0.33858732, 0.466025466, 0.817422101))
        self.m4x10_419010_6.translate((20.729374904, 65.796608357, -152.594722215))
        self.m4x16_hex_12.rotate(93.840965716, (0.935113127, 0.250562807, 0.250562807))
        self.m4x16_hex_12.translate((10.629959849, -46.19163054, 4.8))
        self.p_6mm_ball_419094.rotate(-180.0, (0.707106781, 0.0, -0.707106781))
        self.p_6mm_ball_419094.translate((9.627860318, 0.0, 30.0))
        self.m4x16_hex_13.rotate(109.207479725, (0.710564775, 0.497542812, 0.497542812))
        self.m4x16_hex_13.translate((37.834429455, -28.552035412, 4.8))
        self.m4x16_hex_14.rotate(-96.717713464, (0.889126491, -0.323615577, 0.323615577))
        self.m4x16_hex_14.translate((39.77027397, 25.787362927, 4.8))
        self.m3x10_pan_3.translate((-40.302280579, 28.219960668, 15.0))
        self.m4x16_hex_15.rotate(93.840965716, (0.935113127, -0.250562807, -0.250562807))
        self.m4x16_hex_15.translate((-34.688145566, -32.30163054, 4.8))
        self.m4_nut_3.translate((-38.140444562, 42.359255052, -142.05))
        self.selector_shaft_bearing_7.rotate(30.0541172, (0.0, 0.0, 1.0))
        self.selector_shaft_bearing_7.translate((54.972018316, -20.008178385, -138.275))
        self.m5x30_countersunk_2.rotate(-70.0, (0.0, 0.0, 1.0))
        self.m5x30_countersunk_2.translate((-19.902048526, 54.308321334, -186.75))
        self.selector_shaft_bearing_8.rotate(58.176118702, (0.0, 0.0, 1.0))
        self.selector_shaft_bearing_8.translate((10.158418394, -57.611253551, -138.275))
        self.m3x10_countersink_screw_3.rotate(-165.893955739, (0.701673843, -0.12372403, -0.701673843))
        self.m3x10_countersink_screw_3.translate((-55.969284246, 20.371153499, 19.8))
        self.m4_nut_4.translate((52.84947971, 21.352575825, -142.05))
        self.setting_axle_holding_plate_2.rotate(-20.0, (0.0, 0.0, 1.0))
        self.setting_axle_holding_plate_2.translate((0.003955163, -0.003319081, -141.45))
        self.base_plate.rotate(180.0, (-0.173648178, 0.984807753, 0.0))
        self.base_plate.translate((-0.406900356, 0.745841949, -180.75))
