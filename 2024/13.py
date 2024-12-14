import os, sys, re, math, itertools, functools, collections, copy
from fractions import Fraction


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


pattern = re.compile(r"[A-Za-z]+\s*[AB]*: X[+=]([0-9]+), Y[+=]([0-9]+)")

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.read().split("\n\n")
    machines = []
    for line in lines:
        line = line.split("\n")
        a = pattern.match(line[0])
        b = pattern.match(line[1])
        p = pattern.match(line[2])
        machines.append(
            [
                Point(int(a.group(1)), int(a.group(2))),
                Point(int(b.group(1)), int(b.group(2))),
                Point(int(p.group(1)), int(p.group(2))),
            ]
        )


def part_1() -> str | int:
    total = 0

    for machine in machines:
        a, b, p = machine

        da = Fraction(a.x, b.x) - Fraction(a.y, b.y)
        if da == 0:
            continue
        db = Fraction(b.x, a.x) - Fraction(b.y, a.y)

        a_ = Fraction(Fraction(p.x, b.x) - Fraction(p.y, b.y), da)
        b_ = Fraction(Fraction(p.x, a.x) - Fraction(p.y, a.y), db)

        if a_ < 0 or b_ < 0 or a_.denominator != 1 or b_.denominator != 1:
            continue

        total += a_ * 3 + b_

    return int(total)


def part_2() -> str | int:
    total = 0

    for machine in machines:
        a, b, p = machine
        p.x += 10000000000000
        p.y += 10000000000000

        da = Fraction(a.x, b.x) - Fraction(a.y, b.y)
        if da == 0:
            continue
        db = Fraction(b.x, a.x) - Fraction(b.y, a.y)

        a_ = Fraction(Fraction(p.x, b.x) - Fraction(p.y, b.y), da)
        b_ = Fraction(Fraction(p.x, a.x) - Fraction(p.y, a.y), db)

        if a_ < 0 or b_ < 0 or a_.denominator != 1 or b_.denominator != 1:
            continue

        total += a_ * 3 + b_

    return int(total)


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
