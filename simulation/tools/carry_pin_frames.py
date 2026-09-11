"""Compare the fifteen source pin mountings in one dial-station frame."""

import json
from simulation.carry_contact import CarryContactBench
from simulation.tools.interference import world_solids, rigid_leaves
from simulation.standard.parts import NumberRollCarryPinHalf, NumberRollCarryPinFull


def probe():
    model = CarryContactBench()
    model.set_state(crank_turns=0, enabled=0)
    model.assemble()
    paths = {path for path, part in rigid_leaves(model)
             if isinstance(part, (NumberRollCarryPinHalf, NumberRollCarryPinFull))}
    shapes = world_solids(model, selected=paths)
    banks = (
        ('result', model.results_dials, 0,
         ('p_10203_1', 'p_10203_2', 'p_10205_1', 'p_10205_2', 'p_10204_1',
          'p_10204_2', 'p_10204_3', 'p_10204_4', 'p_10204_5', 'p_10204_6')),
        ('counter', model.turns_dials, 130,
         ('p_10203_3', 'p_10203_4', 'p_10205_3', 'p_10205_4', 'p_10204_7')),
    )
    for bank, register, origin, names in banks:
        for place, name in enumerate(names):
            dial = getattr(register, name)
            for part in dial.children:
                path = f'Curta.{register.name}.{dial.name}.{part.name}'
                if path not in shapes:
                    continue
                shape = shapes[path].rotate((0, 0, 0), (0, 0, 1), -origin+20*place)
                bounds = shape.BoundingBox()
                planes = sorted((face for face in shape.Faces() if face.geomType() == 'PLANE'),
                                key=lambda face: face.Area(), reverse=True)
                print(json.dumps(dict(bank=bank, place=place, dial=name, part=part.name,
                    center=shape.Center().toTuple(), volume=shape.Volume(),
                    bounds=[bounds.xmin, bounds.xmax, bounds.ymin, bounds.ymax, bounds.zmin, bounds.zmax],
                    faces=[dict(area=face.Area(), center=face.Center().toTuple(),
                                normal=face.normalAt().toTuple()) for face in planes[:2]])), flush=True)


if __name__ == '__main__':
    probe()
