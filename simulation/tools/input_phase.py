"""Calibrate the one-tooth drum engagement against its five-tooth pinion."""

from concurrent.futures import ThreadPoolExecutor
from simulation.standard.parts import OneToothStepDrumSegment, TransmissionGear0_5


def probe():
    tooth = OneToothStepDrumSegment().shape().rotate((0, 0, 0), (0, 0, 1), 170.104082802)
    tooth = tooth.translate((0, 0, -70.8))
    gear = TransmissionGear0_5().shape()

    def trial(start):
        volumes = []
        for angle in range(95, 137, 2):
            turn = 72 * min(1, max(0, (angle - start) / 11.25))
            a = tooth.rotate((0, 0, 0), (0, 0, 1), -angle)
            b = gear.rotate((0, 0, 0), (0, 0, 1), turn).translate((40.5, 0, -70.92499975))
            overlap = a.intersect(b)
            assert overlap.isValid(), (start, angle)
            volumes.append(sum(solid.Volume() for solid in overlap.Solids()))
        return start, max(volumes)

    with ThreadPoolExecutor(max_workers=4) as executor:
        for result in executor.map(trial, range(100, 117)):
            print(*result, flush=True)


if __name__ == '__main__':
    probe()
