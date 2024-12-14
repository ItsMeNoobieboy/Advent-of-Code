import os, sys, re, math, itertools, functools, collections, operator

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.read()


def find_next(index):
    a, b, c = (
        lines.find("mul(", index),
        lines.find("do()", index),
        lines.find("don't()", index),
    )
    if a == -1:
        a = float("inf")
    if b == -1:
        b = float("inf")
    if c == -1:
        c = float("inf")
    if a == b == c == float("inf"):
        return -1, -1
    start = min(a, b, c)
    return start, lines.find(")", start)


def solve():
    enabled = True
    part_1 = 0
    part_2 = 0

    start = -1
    while True:
        start, end = find_next(start + 1)

        # No more instructions
        if start == -1:
            break

        instruction = lines[start : end + 1]
        if instruction == "do()":
            enabled = True
            continue
        elif instruction == "don't()":
            enabled = False
            continue

        # is mul command
        inner = instruction[4:-1]
        # Two args
        if inner.count(",") != 1:
            continue
        a, b = inner.split(",")

        # Both nums
        if not a.isdigit() or not b.isdigit():
            continue

        # Check length
        if len(a) not in range(1, 4) or len(b) not in range(1, 4):
            continue
        a, b = int(a), int(b)

        # Tally
        part_1 += a * b
        if enabled:
            part_2 += a * b

    return part_1, part_2


if __name__ == "__main__":
    part_1, part_2 = solve()
    print("Part 1:", part_1)
    print("Part 2:", part_2)
