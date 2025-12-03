import logging

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self._get_input()

    def part1(self):
        return self._solve(2)

    def part2(self):
        return self._solve(12)

    def _solve(self, size):
        total = 0
        for row in self.data:
            result = 0
            for digit in range(size, 0, -1):
                row, max_digit = self._find_max(row, digit - 1)
                result += max_digit * (10 ** (digit - 1))
            total += result
        return total

    def _find_max(self, row, end):
        max_index, result = 0, 0
        for index in range(0, len(row) - end):
            if row[index] > result:
                result = row[index]
                max_index = index
        return row[max_index+1:], result

    def _get_input(self):
        with open(self.file, encoding='utf-8') as f:
            raw = f.readlines()
        logging.info('input: %s, %s', raw, type(raw))
        data = [[int(num) for num in row.strip()] for row in raw]
        logging.info(data[:5])
        return data
