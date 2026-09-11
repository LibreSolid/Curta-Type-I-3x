"""Native continuity and source fidelity of all seventeen flexible fingers."""

from solid_node.node import AssemblyNode
from solid_node.simulation import Driver
from simulation.spider import FlexibleSpider


class SpiderBankBench(AssemblyNode):
    rise = Driver(default=0, range=(0, 3), unit='mm')
    spider = FlexibleSpider()
    rise.drives(spider.result_1.rise)
    rise.drives(spider.result_2.rise)
    rise.drives(spider.result_3.rise)
    rise.drives(spider.result_4.rise)
    rise.drives(spider.result_5.rise)
    rise.drives(spider.result_6.rise)
    rise.drives(spider.result_7.rise)
    rise.drives(spider.result_8.rise)
    rise.drives(spider.result_9.rise)
    rise.drives(spider.result_10.rise)
    rise.drives(spider.result_11.rise)
    rise.drives(spider.turns_1.rise)
    rise.drives(spider.turns_2.rise)
    rise.drives(spider.turns_3.rise)
    rise.drives(spider.turns_4.rise)
    rise.drives(spider.turns_5.rise)
    rise.drives(spider.turns_6.rise)
