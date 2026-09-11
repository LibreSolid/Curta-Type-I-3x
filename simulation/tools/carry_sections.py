"""Native contact regions and sections of the first carry's fork and reset shoe."""

import json
import cadquery as cq
import matplotlib.pyplot as plt
from simulation.carry_contact import CarryContactBench
from simulation.tools.interference import world_solids


def probe():
    model = CarryContactBench()
    model.set_state(crank_turns=0, enabled=0)
    model.assemble()
    paths = {
        'slider': 'Curta.results_lever.tens_slider_for_results',
        'flange': 'Curta.result.p_10220_410003_1_419227',
        'bell': 'Curta.bell',
        'pin': 'Curta.results_dials.p_10203_1.number_roll_carry_pin_half',
    }
    solids = world_solids(model, selected=set(paths.values()))
    shapes = {name: solids[path] for name, path in paths.items()}
    for kind in ('flange', 'bell', 'pin'):
        overlap = shapes['slider'].intersect(shapes[kind])
        print(json.dumps({'kind': kind, 'native_mm3': overlap.Volume(),
                         'regions': [{'mm3': region.Volume(), 'center': region.Center().toTuple()}
                                     for region in overlap.Solids()]}), flush=True)
    figure, axes = plt.subplots(1, 2, figsize=(13, 7))
    # X/Z side sections across the 1.47 mm slider thickness, and Y/Z across pin.
    sections = (cq.Plane((0, -7.15, 0), (1, 0, 0), (0, -1, 0)),
                cq.Plane((57.5, 0, 0), (0, 1, 0), (1, 0, 0)))
    for ax, plane in zip(axes, sections):
        for name, shape in shapes.items():
            sliced = cq.Workplane(plane).add(shape).section().val()
            first = True
            for edge in sliced.Edges():
                points, _ = edge.sample(80)
                points = [plane.toLocalCoords(point) for point in points]
                ax.plot([p.x for p in points], [p.y for p in points],
                        label=name if first else None)
                first = False
        ax.set_aspect('equal')
        ax.grid()
        ax.legend()
    axes[0].set(xlim=(24, 45), ylim=(-37, -15), xlabel='world X', ylabel='world Z')
    axes[1].set(xlim=(-15, 5), ylim=(23, 44), xlabel='world Y', ylabel='world Z')
    figure.tight_layout()
    figure.savefig('_build_evidence/carry-sections.png', dpi=160)


if __name__ == '__main__':
    probe()
