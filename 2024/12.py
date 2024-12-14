import os, sys, re, math, itertools, functools, collections, copy, fractions

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.read().splitlines()
    # For parsing lines of integers
    # lines = [[int(n) for n in line.split(" ")] for line in lines]

l = len(lines)
w = len(lines[0])
visited = []


def dfs1(i, j, match=None):
    if i < 0 or i >= l or j < 0 or j >= w:
        return 1, 0

    if match is None:
        match = lines[i][j]

    if lines[i][j] != match:
        return 1, 0

    if visited[i][j]:
        return 0, 0

    visited[i][j] = True

    p, a = 0, 0

    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        p_, a_ = dfs1(i + x, j + y, match)
        p += p_
        a += a_

    return p, a + 1


def part_1() -> str | int:
    total = 0

    global visited
    visited = [[False for _ in range(w)] for _ in range(l)]

    for i in range(l):
        for j in range(w):
            if visited[i][j]:
                continue

            p, a = dfs1(i, j)
            total += p * a

    return total


def is_corner(i, j, match):
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= w:
        return True
    if i >= l and j < 0:
        return True
    if i >= l and j >= w:
        return True

    if i < 0:
        if 0 <= j < w and lines[0][j] != match:
            return True
    if i >= l:
        if 0 <= j < w and lines[l - 1][j] != match:
            return True
    if j < 0:
        if 0 <= i < l and lines[i][0] != match:
            return True
    if j >= w:
        if 0 <= i < l and lines[i][w - 1] != match:
            return True

    return False


def dfs2(i, j, match=None):
    if i < 0 or i >= l or j < 0 or j >= w:
        return 0, 0

    if match is None:
        match = lines[i][j]

    if lines[i][j] != match:
        return 0, 0

    if visited[i][j]:
        return 0, 0

    visited[i][j] = True

    p, a = 0, 0

    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        x, y = i + dx, j + dy
        if x < 0 or x >= l or y < 0 or y >= w:
            if is_corner(x, y, match):
                p += 1
            continue

        # Exterier corner
        if lines[i][y] != match and lines[x][j] != match:
            p += 1

        # Interior corner
        if lines[x][y] != match and lines[i][y] == lines[x][j] == match:
            p += 1

    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        p_, a_ = dfs2(i + x, j + y, match)
        p += p_
        a += a_

    return p, a + 1


def part_2() -> str | int:
    total = 0

    global visited
    visited = [[False for _ in range(w)] for _ in range(l)]

    for i in range(l):
        for j in range(w):
            if visited[i][j]:
                continue

            p, a = dfs2(i, j)
            total += p * a

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
