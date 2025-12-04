import logging

class Main:
    def __init__(self, file):
        self.file = file
        self.data = []

    def part1(self) -> int:
        self.data = self._get_input()
        return self._move_rolls()

    def part2(self) -> int:
        self.data = self._get_input()
        rolls, last = 0, -1
        while rolls != last:
            last = rolls
            rolls += self._move_rolls()
        return rolls

    def _move_rolls(self) -> int:
        grid, rolls = [list(s) for s in self.data], 0
        for y, line in enumerate(self.data):
            for x, val in enumerate(line):
                if val == '@':
                    adj = sum(
                        self.is_roll_at(x + dx, y + dy)
                        for dx in [-1, 0, 1]
                        for dy in [-1, 0, 1]
                    )
                    if adj < 5:
                        rolls += 1
                        grid[y][x] = '.'
        self.data = grid
        return rolls

    def is_roll_at(self, x, y) -> bool:
        return (
            0 <= y < len(self.data)
            and 0 <= x < len(self.data[0])
            and self.data[y][x] == '@'
        )

    def _get_input(self):
        with open(self.file, encoding='utf-8') as f:
            raw = [list(s.strip()) for s in f.readlines()]
        logging.info(raw[:5])
        return raw
