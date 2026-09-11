"""Installed X/Z section through the first digit ball and spider collar."""

import matplotlib.pyplot as plt
from simulation.curta import Curta
from simulation.standard.parts import SpiderSpring


def probe():
    root = Curta()
    root.set_state(**root.instructions['Rest'].targets)
    root.assemble()
    root.build_stls()
    carriage = root.carriage.registers
    bodies = dict(
        collar=carriage.carrier.crank_collar,
        cover=carriage.clearing_ring.clearing_cover,
        carrier=carriage.carrier.upper_carriage_body_1.counter_body,
        ball=carriage.dial_detents.p_6mm_ball_419241_12,
        dial=carriage.result_register.p_10203_1.results_dial_type_1,
    )
    source = SpiderSpring()
    source.assemble()
    source.build_stls()
    meshes = {name: body.mesh.copy() for name, body in bodies.items()}
    meshes['spider'] = source.mesh.copy()
    meshes['spider'].apply_translation((0, 0, 45.2))
    meshes['ball'].apply_translation((0, 0, -bodies['ball'].lift.value))
    figure, axis = plt.subplots(figsize=(13, 6))
    for index, (name, mesh) in enumerate(meshes.items()):
        section = mesh.section(plane_origin=(0, 0, 0), plane_normal=(0, 1, 0))
        if section is None:
            continue
        for path_index, path in enumerate(section.discrete):
            axis.plot(path[:, 0], path[:, 2], color=f'C{index}',
                      label=name if path_index == 0 else None)
    axis.set(xlim=(0, 57), ylim=(36, 51), xlabel='World X (mm)', ylabel='World Z (mm)')
    axis.set_aspect('equal')
    axis.grid()
    axis.legend()
    figure.tight_layout()
    figure.savefig('_build_evidence/spider-mount-section.png', dpi=160)


if __name__ == '__main__':
    probe()
