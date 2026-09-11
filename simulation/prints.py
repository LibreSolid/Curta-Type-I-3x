"""The source's printed groups, separate from their individual CAD features."""

from solid_node.node import AssemblyNode
from simulation.standard.assembly import MainAxleStepDrum1
from simulation.standard.printed import MainAxleStepDrumTop1, MainAxleStepDrumBottom1, TensBell1


class PrintedDrum(MainAxleStepDrum1):
    main_axle_step_drum_top_1 = MainAxleStepDrumTop1()
    main_axle_step_drum_bottom_1 = MainAxleStepDrumBottom1()


class PrintedDrive(AssemblyNode):
    drum = PrintedDrum()
    tens_bell = TensBell1()
