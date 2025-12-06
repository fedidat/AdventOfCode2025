import logging

class Main:
    def __init__(self, file):
        self.file = file

    def part1(self):
        data = self._get_p1_input()
        total = 0
        for operator, operands in data:
            total += self._apply(operator, operands)
        return total

    def part2(self):
        data = self._get_p2_input()
        total, vals = 0, []
        for operator, operand in data:
            vals.append(operand)
            if operator:
                total += self._apply(operator, vals)
                vals = []
        return total

    def _apply(self, operator, operands):
        if operator == '+':
            return sum(operands)
        # elif operator == '*':
        prod = 1
        for op in operands:
            prod *= op
        return prod

    def _get_p1_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = [line.strip().split() for line in f.readlines()]
        data = []
        for i in range(len(lines[0])):
            operator = lines[-1][i]
            operands = [int(row[i]) for row in lines[:-1]]
            data.append((operator, operands))
        logging.info(data[:5])
        return data

    def _get_p2_input(self):
        with open(self.file, encoding='utf-8') as f:
            lines = [list(line) for line in f.readlines()]
        data = []
        for i in range(len(lines[0])-2, -1, -1):
            full = ''.join(lines[j][i] for j in range(len(lines)))
            if full.strip():
                operator = full[-1].strip()
                operand = int(full[:-1]) if full[:-1] else None
                data.append((operator, operand))
        logging.info(data[:5])
        return data
