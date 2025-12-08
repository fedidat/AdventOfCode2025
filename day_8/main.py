import logging
import math

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self.get_input()

    def part1(self, cycles):
        result = self._iterate(cycles)
        return result

    def part2(self, cycles):
        a, b = self._iterate(cycles)
        return a[0] * b[0]

    def _iterate(self, cycles):
        distances = {}
        for a in self.data:
            for b in self.data:
                if a == b or (tuple(b), tuple(a)) in distances:
                    continue
                distances[(tuple(a), tuple(b))] = (
                    (a[0] - b[0]) ** 2+ (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
                )
        sorted_dist = sorted(distances.items(), key=lambda x: x[1])
        circuits = {tuple(a): {tuple(a)} for a in self.data}
        for i in range(cycles):
            (a, b), _ = sorted_dist[i]
            if len(circuits[a].union(circuits[b])) == len(self.data):
                return (a, b)
            for c in circuits[b]:
                circuits[a].add(c)
                circuits[c] = circuits[a]
            for c in circuits[a]:
                circuits[c] = circuits[a]
        circuit_set = set()
        for c in circuits.values():
            circuit_set.add(frozenset(c))
        circuit_sizes = sorted([len(c) for c in circuit_set])
        top3 = circuit_sizes[-3:]
        return math.prod(top3)

    def get_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = f.readlines()
        data = [[int(val) for val in line.split(',')] for line in lines]
        logging.info(data[:5])
        return data
