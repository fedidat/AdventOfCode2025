from copy import deepcopy

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self.get_input()

    def part1(self):
        splits = 0
        data = deepcopy(self.data)
        start, end = self.data[0].index('S'), self.data[0].index('S') + 1
        for j in range(len(data) - 1):
            for i in range(start, end):
                if data[j][i] == '|' or data[j][i] == 'S':
                    if data[j + 1][i] == '^':
                        data[j + 1][i - 1] = '|'
                        data[j + 1][i + 1] = '|'
                        start = min(start, i - 1)
                        end = max(i + 2, end)
                        splits += 1
                    else:
                        data[j + 1][i] = '|'
        return splits

    def part2(self):
        ways = deepcopy(self.data)
        ways.append([1] * len(self.data[-1]))
        for j in range(len(self.data) - 2, -1, -2):
            for i in range(len(self.data[j])):
                ways[j][i] = (
                    ways[j+2][i-1] + ways[j+2][i+1]
                    if self.data[j][i] == '^'
                    else ways[j+2][i]
                )
        return ways[0][self.data[0].index('S')]

    def get_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = f.readlines()
        data = [list(line.strip()) for line in lines]
        return data
