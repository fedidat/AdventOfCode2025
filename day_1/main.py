import logging

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self.get_input()

    def part1(self):
        pos = 50
        code = 0
        for direction, distance in self.data:
            mult = 1 if direction == "R" else -1
            pos = (pos + mult * distance) % 100
            if pos == 0:
                code += 1
        return code

    def part2(self):
        pos = 50
        code = 0
        for direction, distance in self.data:
            mult = 1 if direction == "R" else -1
            if direction == 'R':
                code += (pos + distance) // 100
            else:
                code += ((100 - pos) % 100 + distance) // 100
            pos = (pos + mult * distance) % 100
        return code

    def get_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = f.readlines()
        data = [(line[0], int(line[1:])) for line in lines]
        logging.info(data[:5])
        return data
