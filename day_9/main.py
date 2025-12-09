import logging
from itertools import combinations

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self.get_input()
        perimeter, last = [], self.data[0]
        for current in self.data[1:]:
            perimeter.append((last, current))
            last = current
        perimeter.append((last, self.data[0]))
        self._perimeter = perimeter

    def part1(self):
        return self._get_largest(check=False)

    def part2(self):
        return self._get_largest(check=True)

    def _get_largest(self, check):
        largest = 0
        for (x0,y0), (x1,y1) in combinations(self.data, 2):
            x0, y0, x1, y1 = self._sort(x0, y0, x1, y1)
            area = (x1 - x0 + 1) * (y1 - y0 + 1)
            if (
                area > largest
                and (not check or self._is_inside(x0, y0, x1, y1))
            ):
                largest = area
        return largest

    def _sort(self, x0, y0, x1, y1):
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        return x0, y0, x1, y1

    def _is_inside(self, x0, y0, x1, y1):
        for (x2, y2), (x3, y3) in self._perimeter:
            x2, y2, x3, y3 = self._sort(x2, y2, x3, y3)
            if x2 < x1 and y2 < y1 and x3 > x0 and y3 > y0:
                return False
        return True

    def get_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = f.readlines()
        data = [[int(c) for c in line.split(',')] for line in lines]
        logging.info(data[:5])
        return data
