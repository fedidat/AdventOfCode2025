import logging

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self.get_input()

    def part1(self):
        total = 0
        for start, end in self.data:
            base = start if len(start) % 2 == 0 else str(10 ** len(start))
            cur = base[:len(base)//2]
            while int(cur * 2) <= int(end):
                cur_n = int(cur * 2)
                if cur_n >= int(start):
                    total += cur_n
                cur = str(int(cur) + 1)
        return total

    def part2(self):
        ids = set()
        for start, end in self.data:
            for repeat in range(2, len(end) + 1):
                base = start
                while len(base) % repeat != 0:
                    base = str(10 ** len(base))
                cur = base[:len(base)//repeat]
                while int(cur * repeat) <= int(end):
                    cur_n = int(cur * repeat)
                    if cur_n >= int(start):
                        ids.add(cur_n)
                    cur = str(int(cur) + 1)
        return sum(ids)

    def get_input(self):
        with open(self.file, encoding='utf-8') as f:
            raw = f.readlines()[0]
        logging.info('input: %s, %s', raw, type(raw))
        data = [line.split('-') for line in raw.split(',')]
        logging.info(data[:5])
        return data
