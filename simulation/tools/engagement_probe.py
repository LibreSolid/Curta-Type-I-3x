"""Locate a full-drum contact in the original CAD ingredients of each print."""

import argparse
import json
from simulation.engagement import Engagement


def ingredients(node, ancestors=(), path=''):
    path = path + '.' + node.name
    operations = [*node.operations, *ancestors]
    if node.children:
        return [part for child in node.children for part in ingredients(child, operations, path)]
    shape = node.shape()
    for operation in operations:
        if hasattr(operation, 'angle'):
            shape = shape.rotate((0, 0, 0), operation.axis, operation.angle)
        else:
            shape = shape.translate(operation.translation)
    return [(path, shape)]


def probe(digit=0, crank=18, subtract=0):
    model = Engagement()
    model.set_state(digit=digit, crank_turns=crank/360, subtract=subtract)
    model.assemble()
    parts = ingredients(model)
    drum = [(path, shape) for path, shape in parts if '.drum.main_axle_step_drum_bottom_1.' in path]
    pinion = [(path, shape) for path, shape in parts if '.result.p_10219_410002_1.' in path]
    for a, first in drum:
        for b, second in pinion:
            overlap = first.intersect(second)
            assert overlap.isValid(), (a, b)
            volume = sum(solid.Volume() for solid in overlap.Solids())
            if volume > 0:
                box = overlap.BoundingBox()
                print(json.dumps({'drum': a, 'input': b, 'mm3': volume,
                                  'bounds': [box.xmin, box.ymin, box.zmin,
                                             box.xmax, box.ymax, box.zmax]}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digit', type=int, default=0)
    parser.add_argument('--crank', type=float, default=18)
    parser.add_argument('--subtract', type=int, default=0)
    probe(**vars(parser.parse_args()))
