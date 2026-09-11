"""The seventeen native balls lift individual fingers of one spider spring."""

from solid_node.motion.joints import Prismatic
from simulation.standard.layers import RegisterDetents as SourceDetents
from simulation.standard.parts import Part6mmBall419241
from simulation.spider import FlexibleSpider, PRELOAD, SEAT_GAP


class RegisterDetents(SourceDetents):
    p_6mm_ball_419241_1 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_2 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_3 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_4 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_5 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_6 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_7 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_8 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_9 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_10 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_11 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_12 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_13 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_14 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_15 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_16 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    p_6mm_ball_419241_17 = Part6mmBall419241(lift=Prismatic(axis=(0, 0, 1)))
    spider_spring = FlexibleSpider()

    p_6mm_ball_419241_12.lift.drives(spider_spring.result_1.rise, offset=PRELOAD)
    p_6mm_ball_419241_1.lift.drives(spider_spring.result_2.rise, offset=PRELOAD)
    p_6mm_ball_419241_13.lift.drives(spider_spring.result_3.rise, offset=PRELOAD)
    p_6mm_ball_419241_16.lift.drives(spider_spring.result_4.rise, offset=PRELOAD)
    p_6mm_ball_419241_11.lift.drives(spider_spring.result_5.rise, offset=PRELOAD)
    p_6mm_ball_419241_3.lift.drives(spider_spring.result_6.rise, offset=PRELOAD)
    p_6mm_ball_419241_7.lift.drives(spider_spring.result_7.rise, offset=PRELOAD)
    p_6mm_ball_419241_4.lift.drives(spider_spring.result_8.rise, offset=PRELOAD)
    p_6mm_ball_419241_17.lift.drives(spider_spring.result_9.rise, offset=PRELOAD)
    p_6mm_ball_419241_8.lift.drives(spider_spring.result_10.rise, offset=PRELOAD)
    p_6mm_ball_419241_5.lift.drives(spider_spring.result_11.rise, offset=PRELOAD)
    p_6mm_ball_419241_2.lift.drives(spider_spring.turns_1.rise, offset=PRELOAD)
    p_6mm_ball_419241_14.lift.drives(spider_spring.turns_2.rise, offset=PRELOAD)
    p_6mm_ball_419241_9.lift.drives(spider_spring.turns_3.rise, offset=PRELOAD)
    p_6mm_ball_419241_10.lift.drives(spider_spring.turns_4.rise, offset=PRELOAD)
    p_6mm_ball_419241_6.lift.drives(spider_spring.turns_5.rise, offset=PRELOAD)
    p_6mm_ball_419241_15.lift.drives(spider_spring.turns_6.rise, offset=PRELOAD)

    def render(self):
        super().render()
        self.spider_spring.translate((0, 0, SEAT_GAP))
