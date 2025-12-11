from functools import cache
import logging

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self.get_input()

    def part1(self):
        return self._paths('you', 'out')

    def part2(self):
        return (
            self._paths('svr', 'dac') * self._paths('dac', 'fft') * self._paths('fft', 'out')
            + self._paths('svr', 'fft') * self._paths('fft', 'dac') * self._paths('dac', 'out')
        )

    @cache
    def _paths(self, start, end):
        if start == end:
            return 1
        return sum(self._paths(adj, end) for adj in self.data.get(start, []))

    def get_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = f.readlines()
        data = dict()
        for line in lines:
            parts = line.strip().split(': ')
            data[parts[0]] = parts[1].split(' ')
        logging.info(list(data.items())[:5])
        return data
