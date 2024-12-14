import os, sys, re, math, itertools, functools, collections, copy, fractions

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.read().splitlines()

l = len(lines)
w = len(lines[0])
visited = []


def dfs(x, y, rating=False):
    if lines[x][y] == "9":
        return 1

    count = 0

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= l or ny < 0 or ny >= w:
            continue

        if visited[nx][ny]:
            continue

        if lines[nx][ny] == chr(ord(lines[x][y]) + 1):
            visited[nx][ny] = True
            count += dfs(nx, ny, rating)
            if rating:
                visited[nx][ny] = False

    return count


def calc(x, y, rating=False):
    global visited
    visited = [[False for _ in range(w)] for _ in range(l)]
    return dfs(x, y, rating)


def part_1() -> str | int:
    total = 0

    for i in range(l):
        for j in range(w):
            if lines[i][j] == "0":
                total += calc(i, j)

    return total


def part_2() -> str | int:
    total = 0

    for i in range(l):
        for j in range(w):
            if lines[i][j] == "0":
                total += calc(i, j, True)

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
