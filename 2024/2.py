import os, sys, re, math, itertools, functools, collections, operator

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [[int(n) for n in x.split()] for x in lines]


def check_safe(line):
    increasing = all(line[i] < line[i + 1] for i in range(len(line) - 1))
    decreasing = all(line[i] > line[i + 1] for i in range(len(line) - 1))
    within_range = all(
        abs(line[i] - line[i + 1]) in range(1, 4) for i in range(len(line) - 1)
    )
    return within_range and (increasing or decreasing)


def with_damp(line):
    if check_safe(line):
        return True

    # Try removing one element
    for i in range(len(line)):
        if check_safe(line[:i] + line[i + 1 :]):
            return True
    return False


def part_1() -> str | int:
    total = 0

    for line in lines:
        if check_safe(line):
            total += 1

    return total


def part_2() -> str | int:
    total = 0

    for line in lines:
        if with_damp(line):
            total += 1

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
