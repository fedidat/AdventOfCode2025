import logging

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self._get_input()

    def part1(self) -> int:
        total = 0
        ranges, available = self.data
        for item in available:
            for r in ranges:
                if r[0] <= item <= r[1]:
                    total += 1
                    break
        return total

    def part2(self) -> int:
        ranges, _ = self.data
        return sum(r[1] - r[0] + 1 for r in self._merge_ranges(ranges))

    def _merge_ranges(self, ranges):
        ranges_s = sorted(ranges, key=lambda x: x[0])
        merged, last = [], ranges_s[0]
        for cur in ranges_s[1:]:
            if last[0] <= cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                merged.append(last)
                last = cur
        merged.append(last)
        return merged

    def _get_input(self):
        with open(self.file, encoding='utf-8') as f:
            raw = f.read().split('\n\n')
        raw_ranges, raw_available = [g.splitlines() for g in raw]
        ranges = [[int(n) for n in pair.split('-')] for pair in raw_ranges]
        available = [int(n) for n in raw_available]
        logging.info("ranges: %s, available: %s", ranges[:5], available[:5])
        return ranges, available
