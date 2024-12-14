import os, sys, re, math, itertools, functools, collections, operator

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.read().strip().split("\n\n")
    rules = [[int(n) for n in line.strip().split("|")] for line in lines[0].split("\n")]
    reports = [
        [int(n) for n in line.strip().split(",")] for line in lines[1].split("\n")
    ]


def part_1() -> str | int:
    total = 0

    for report in reports:
        valid = True
        for i in range(len(report) - 1):
            for j in range(i + 1, len(report)):
                if [report[j], report[i]] in rules:
                    valid = False
                    break
                
        if valid:
            total += report[len(report) // 2]

    return total


def part_2() -> str | int:
    total = 0

    for report in reports:
        updated = False
        for i in range(len(report) - 1):
            for j in range(i + 1, len(report)):
                if [report[j], report[i]] in rules:
                    report[j], report[i] = report[i], report[j]
                    updated = True

        if updated:
            total += report[len(report) // 2]

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
