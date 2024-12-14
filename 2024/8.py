import os, sys, re, math, itertools, functools, collections, copy, fractions

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = [line.strip() for line in f.readlines()]

count = [[] for _ in range(256)]
for i, line in enumerate(lines):
    line = line.strip()
    for j, ltr in enumerate(line):
        count[ord(ltr)].append((i, j))

grid = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]


def part_1() -> str | int:
    total = 0

    for char, coords in enumerate(count):
        if len(coords) < 2:
            continue
        if chr(char) == ".":
            continue

        for a, b in itertools.combinations(coords, 2):
            x1, y1 = a
            x2, y2 = b
            dis_x, dis_y = x2 - x1, y2 - y1
            nx1, ny1 = x1 - dis_x, y1 - dis_y
            nx2, ny2 = x2 + dis_x, y2 + dis_y

            if 0 <= nx1 < len(grid) and 0 <= ny1 < len(grid[0]):
                grid[nx1][ny1] = True
            if 0 <= nx2 < len(grid) and 0 <= ny2 < len(grid[0]):
                grid[nx2][ny2] = True

    for row in grid:
        total += row.count(True)

    return total


grid = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]


def part_2() -> str | int:
    total = 0

    for char, coords in enumerate(count):
        if len(coords) < 2:
            continue
        if chr(char) == ".":
            continue

        for a, b in itertools.combinations(coords, 2):
            x1, y1 = a
            x2, y2 = b
            slope = fractions.Fraction(y2 - y1, x2 - x1)

            nx, ny = x1, y1
            while 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                grid[nx][ny] = True
                nx -= slope.denominator
                ny -= slope.numerator

            nx, ny = x1, y1
            while 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                grid[nx][ny] = True
                nx += slope.denominator
                ny += slope.numerator

    for row in grid:
        total += row.count(True)

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
