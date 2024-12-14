import os, sys, re, math, itertools, functools, collections, operator

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.readlines()
    equations = []
    for line in lines:
        a, b = line.strip().split(": ")
        equations.append([int(a), [int(n) for n in b.split(" ")]])


def attempt_pt1(target: int | float, values: list[int]):
    if len(values) == 2:
        return values[0] + values[1] == target or values[0] * values[1] == target
    else:
        return attempt_pt1(target - values[-1], values[:-1]) or attempt_pt1(
            target / values[-1], values[:-1]
        )


def part_1() -> str | int:
    total = 0

    for target, values in equations:
        if attempt_pt1(target, values):
            total += target

    return total


def attempt_pt2(target: int | float, values: list[int]):
    if len(values) == 2:
        possible = values[0] + values[1] == target or values[0] * values[1] == target
        if target % 1 == 0:
            possible |= int(str(values[0]) + str(values[1])) == target
        return possible
    else:
        possible = attempt_pt2(target - values[-1], values[:-1]) or attempt_pt2(
            target / values[-1], values[:-1]
        )
        n = len(str(values[-1]))
        if target % 1 == 0:
            str_target = str(int(target))
            if (
                str_target[-n:] == str(values[-1])
                and len(str_target) > n
                and str_target[0] != "-"
            ):
                possible |= attempt_pt2(int(str_target[:-n]), values[:-1])
        return possible


def part_2() -> str | int:
    total = 0

    for target, values in equations:
        if attempt_pt2(target, values):
            total += target

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
