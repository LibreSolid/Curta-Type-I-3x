"""Material connectivity distinguishes an enclosed void from a detached body."""

import numpy as np


def assert_connected_material(mesh):
    """One outward material shell, with only enclosed inward cavity shells.

    This does not merge vertices, ignore components or set a volume epsilon.
    A second positive-volume shell is a detached body; an open, zero-volume
    or external negative shell is invalid. Native one-solid checks complement
    this faceted check wherever the source provides an exact shape.
    """
    shells = mesh.split(only_watertight=False)
    assert all(shell.is_watertight for shell in shells), 'open mesh shell'
    material = [shell for shell in shells if shell.volume > 0]
    cavities = [shell for shell in shells if shell.volume < 0]
    assert len(material) == 1, f'{len(material)} detached material bodies'
    assert len(material) + len(cavities) == len(shells), 'zero-volume shell'
    for cavity in cavities:
        assert np.all(material[0].contains(cavity.vertices)), 'cavity is not enclosed by material'
    assert mesh.volume > 0, 'nonpositive material volume'
