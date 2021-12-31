import dataclasses
from typing import Tuple

import aocd
import numpy as np


def main():
    data = aocd.get_data(year=2021, day=5).split("\n")

    entries = [Entry.from_line(line) for line in data]

    x_max, y_max = 0, 0

    for entry in entries:
        x_max = max(x_max, entry.start[0], entry.end[0])
        y_max = max(y_max, entry.start[1], entry.end[1])

    grid = np.zeros([x_max + 1, y_max + 1])
    for entry in entries:

        for x, y in entry.vent_locations():
            grid[x, y] += 1
        print(grid)
        print()

    print(np.sum(grid >= 2))

    # grid[entry.vent_locations()] += 1
    # print(grid)


@dataclasses.dataclass
class Entry:
    start: Tuple[int, int]
    end: Tuple[int, int]

    @staticmethod
    def from_line(line: str) -> "Entry":
        start, end = line.split("->")
        x1, y1 = map(int, start.strip().split(","))
        x2, y2 = map(int, end.strip().split(","))

        return Entry((x1, y1), (x2, y2))

    @property
    def is_diagonal(self):
        return not (self.start[0] == self.end[0] or self.start[1] == self.end[1])

    def vent_locations(self):
        locations = [self.start]

        dx = self.end[0] - self.start[0]
        dy = self.end[1] - self.start[1]

        x, y = self.start
        while True:
            x += _step(dx)
            y += _step(dy)
            locations.append((x, y))

            if x == self.end[0] and y == self.end[1]:
                break

        return tuple(locations)


def _step(x):
    if x > 0:
        return 1
    if x < 0:
        return -1

    return 0


if __name__ == "__main__":
    main()
