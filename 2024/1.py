import os, sys, re, math, itertools, functools, collections, operator

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.readlines()
    one = [int(x[:5]) for x in lines]
    two = [int(x[8:]) for x in lines]


def part_1() -> str | int:
    total = 0
    sone = sorted(one)
    stwo = sorted(two)

    for a, b in zip(sone, stwo):
        total += abs(a - b)

    return total


def part_2() -> str | int:
    total = 0
    for a in one:
        total += a * two.count(a)

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
