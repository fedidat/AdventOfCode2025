import logging
import re

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self.get_input()

    def part1(self):
        result = 0
        for x, y, nums in self.data:
            if x//3 * y//3 >= sum(nums):
                result += 1
        return result

    def get_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = f.readlines()
        data = []
        for line in lines[30:]:
            x, y, *nums = map(int, re.findall(r'\d+', line))
            data.append((x, y, nums))
        logging.info(data[:5])
        return data
