import logging

def generate_identical_distributions(n, k):
    if k == 1:
        yield (n,)
    else:
        for i in range(n + 1):
            for tail in generate_identical_distributions(n - i, k - 1):
                yield (i,) + tail

class Main:
    def __init__(self, file):
        self.file = file
        self.data = self.get_input()

    def part1(self):
        result = 0
        for machine in self.data:
            result += self._solve_machine(machine)
        return result

    def _solve_machine(self, machine):
        _, goal, switches, _ = machine
        switches = set(tuple(s) for s in switches)
        depth = 10
        combos = set()
        for i in range(depth):
            combos = self._combinations(combos, switches, i)
            for combo in combos:
                cur = set()
                for switch in combo:
                    for toggle in switch:
                        cur ^= {toggle}
                if cur == goal:
                    return i
        raise ValueError("No solution found")

    def _combinations(self, base, switches, i):
        if i == 0:
            return base
        next_combos = set()
        for combo in (base or {()}):
            for switch in switches:
                new_combo = tuple(sorted(combo + (switch,)))
                next_combos.add(new_combo)
        return next_combos

    def part2(self):
        result = 0
        for i, machine in enumerate(self.data):
            result += self._solve_machine_p22(machine)
        return result

    def _solve_machine_p22(self, machine):
        _, _, switches, goal = machine
        max_depth = 100
        for depth in range(max_depth):
            combos = list(generate_identical_distributions(depth, len(switches)))
            for dist in combos:
                cur = [0] * len(goal)
                for i, num in enumerate(dist):
                    for pos in switches[i]:
                        cur[pos] += num
                if cur == goal:
                    return depth
        raise ValueError("No solution found")

    # def _solve_machine_p21(self, machine):
    #     _, _, switches, goal = machine
    #     switches = set(tuple(s) for s in switches)
    #     depth = 1000
    #     cache = {tuple([0] * len(goal))}
    #     for i in range(depth):
    #         next_cache = set()
    #         for entry in cache:
    #             for switch in switches:
    #                 cur = list(entry)
    #                 for pos in switch:
    #                     cur[pos] += 1
    #                 if cur == goal:
    #                     return i + 1
    #                 if all(cur[i] <= goal[i] for i in range(len(cur))):
    #                     next_cache.add(tuple(cur))
    #         cache = next_cache
    #     raise ValueError("No solution found")

    # def _solve_machine_p2(self, machine):
    #     _, _, switches, goal = machine
    #     switches = set(tuple(s) for s in switches)
    #     depth = 40
    #     combos = set()
    #     for i in range(depth):
    #         combos = self._combinations(combos, switches, i)
    #         next_combos = set()
    #         for combo in combos:
    #             cur = [0] * len(goal)
    #             for switch in combo:
    #                 for toggle in switch:
    #                     cur[toggle] += 1
    #             if cur == goal:
    #                 return i
    #             if all(cur[i] <= goal[i] for i in range(len(cur))):
    #                 next_combos.add(combo)
    #         combos = next_combos
    #     raise ValueError("No solution found")

    def get_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = f.readlines()
        raw = [line.strip().split(' ') for line in lines]
        data = []
        for r in raw:
            num_switches = len(r[0][1:-1])
            goal = {i for i, c in enumerate(r[0][1:-1]) if c == '#'}
            switches = []
            for raw_switch in r[1:-1]:
                switches.append(set(int(n) for n in raw_switch[1:-1].split(',')))
            joltage = [int(n) for n in r[-1][1:-1].split(',')]
            data.append((num_switches, goal, switches, joltage))
        logging.info(data[:5])
        return data
