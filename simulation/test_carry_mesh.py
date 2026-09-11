"""Both a carried digit and a blank digit must clear the complete bell."""

from solid_node.test import TestCase
from simulation.carry_mesh import CarryMesh


class CarryMeshTest(TestCase):
    node = CarryMesh

    def check_channel(self, part):
        for enabled in (0, 1):
            for angle in range(0, 361, 3):
                self.node.set_state(crank_turns=angle / 360, enabled=enabled)
                try:
                    self.assertNotIntersecting(self.node.bell, part)
                except AssertionError as error:
                    raise AssertionError(f'carry={enabled}, crank={angle}: {error}') from error

    def test_result_carry_and_reset(self):
        self.check_channel(self.node.result.p_10220_410003_1_419227)

    def test_turns_carry_and_reset(self):
        self.check_channel(self.node.counter.p_10220_410003_1_419081)

    def test_active_teeth_and_inactive_lockouts_really_constrain_the_shafts(self):
        for angle, group in [(152, self.node.result.p_10220_410003_1_419227),
                             (204, self.node.counter.p_10220_410003_1_419081)]:
            self.node.set_state(crank_turns=0, enabled=0)
            lockout = group.pentagonal_lockout
            self.assertFreeWithin(lockout, .1, against=self.node.bell)
            self.assertBlockedBeyond(lockout, 12, against=self.node.bell)
            self.node.set_state(crank_turns=angle/360, enabled=1)
            tooth = group.transmission_gear_0_6
            self.assertFreeWithin(tooth, .1, against=self.node.bell)
            self.assertBlockedBeyond(tooth, 12, against=self.node.bell)
