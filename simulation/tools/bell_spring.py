"""Measure the source forked spring against the two drum detent positions."""

import json
import cadquery as cq
import matplotlib.pyplot as plt
from simulation.bell_spring import BellLeafFitBench
from simulation.standard.parts import TensBellSpring
from simulation.tools.interference import world_solids


def probe():
    model = BellLeafFitBench()
    model.set_state(spread=0, subtract=0)
    model.assemble()
    paths = {
        'drum_top': 'Curta.drum.main_axle_step_drum_top_1',
        'drum_bottom': 'Curta.drum.main_axle_step_drum_bottom_1',
        'bell': 'Curta.bell',
    }
    figure, axes = plt.subplots(1, 2, figsize=(12, 10))
    plane = cq.Plane((0, 0, 0), (1, 0, 0), (0, -1, 0))
    colors = dict(spring='tab:blue', drum_top='tab:orange', drum_bottom='tab:red', bell='tab:green')
    for subtract, ax in enumerate(axes):
        model.set_state(subtract=subtract)
        native = world_solids(model, selected=set(paths.values()))
        shapes = {name: native[path] for name, path in paths.items()}
        shapes['spring'] = TensBellSpring().shape().translate((0, 0, -8.7))
        for name, shape in shapes.items():
            if name.startswith('drum'):
                contact = shapes['spring'].intersect(shape)
                print(json.dumps(dict(subtract=subtract, body=name, volume=contact.Volume(),
                    regions=[dict(volume=part.Volume(), center=part.Center().toTuple())
                             for part in contact.Solids()])), flush=True)
            section = cq.Workplane(plane).add(shape).section().val()
            first = True
            for edge in section.Edges():
                points, _ = edge.sample(80)
                points = [plane.toLocalCoords(point) for point in points]
                ax.plot([point.x for point in points], [point.y for point in points],
                        color=colors[name], label=name if first else None)
                first = False
        ax.set(xlim=(-24, 24), ylim=(-75, 5), xlabel='world X', ylabel='world Z',
               title='Subtraction' if subtract else 'Addition')
        ax.set_aspect('equal')
        ax.grid()
        ax.legend()
    figure.tight_layout()
    figure.savefig('_build_evidence/bell-spring-source-sections.png', dpi=150)

    figure, axes = plt.subplots(2, 4, figsize=(16, 8))
    for subtract, row in enumerate(axes):
        model.set_state(subtract=subtract)
        native = world_solids(model, selected=set(paths.values()))
        for height, ax in zip((-45, -50, -56, -60.6), row):
            plane = cq.Plane((0, 0, height), (1, 0, 0), (0, 0, 1))
            shapes = {name: native[path] for name, path in paths.items()}
            shapes['spring'] = TensBellSpring().shape().translate((0, 0, -8.7))
            for name, shape in shapes.items():
                section = cq.Workplane(plane).add(shape).section().val()
                first = True
                for edge in section.Edges():
                    points, _ = edge.sample(80)
                    ax.plot([point.x for point in points], [point.y for point in points],
                            color=colors[name], label=name if first else None)
                    first = False
            ax.set(xlim=(-22, 22), ylim=(-22, 22), xlabel='world X', ylabel='world Y',
                   title=f'{"Subtract" if subtract else "Add"}, Z {height}')
            ax.set_aspect('equal')
            ax.grid()
            ax.legend()
    figure.tight_layout()
    figure.savefig('_build_evidence/bell-spring-source-horizontal.png', dpi=150)


if __name__ == '__main__':
    probe()
