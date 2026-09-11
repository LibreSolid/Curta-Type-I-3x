"""Measure ball rise over one native dial-detent pitch, independently of motion."""

import json
import cadquery as cq
from simulation.curta import Curta
from simulation.tools.interference import world_solids


def probe():
    root = Curta()
    root.set_state(**root.instructions['Rest'].targets)
    root.assemble()
    prefix = 'Curta.carriage.registers.'
    stations = (
        ('type_1', 'result_register.p_10203_1.results_dial_type_1',
         'dial_detents.p_6mm_ball_419241_12', 0),
        ('type_2', 'result_register.p_10205_1.results_dial_type_2',
         'dial_detents.p_6mm_ball_419241_13', 40),
    )
    selected = {prefix + path for _, dial, ball, _ in stations for path in (dial, ball)}
    native = world_solids(root, selected=selected)
    for kind, dial_path, ball_path, clocking in stations:
        dial = native[prefix + dial_path].rotate((0, 0, 0), (0, 0, 1), clocking)
        ball = native[prefix + ball_path].rotate((0, 0, 0), (0, 0, 1), clocking)
        node = root
        for name in (prefix + ball_path).split('.')[1:]:
            node = getattr(node, name)
        ball = ball.translate((0, 0, -node.lift.value))
        centre = ball.Center().toTuple()
        for step in range(73):
            angle = step / 2
            wheel = dial.rotate((0, 0, 33.9), (1, 0, 33.9), angle)

            def blocked(height):
                # A native sphere is clear exactly when its centre is at least
                # its radius from the solid. This measures the same contact
                # without constructing an ill-conditioned, vanishing sliver.
                point = cq.Vertex.makeVertex(centre[0], centre[1], centre[2] + height)
                return point.distance(wheel) < 3

            lower, upper = 0, 5
            assert not blocked(upper), (kind, angle)
            if blocked(lower):
                for _ in range(17):
                    middle = (lower + upper)/2
                    if blocked(middle):
                        lower = middle
                    else:
                        upper = middle
            else:
                upper = 0
            print(json.dumps(dict(kind=kind, angle=angle, rise=upper + .05)), flush=True)


if __name__ == '__main__':
    probe()
