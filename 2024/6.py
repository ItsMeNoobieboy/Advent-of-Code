import os, copy

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")
    lines = [list(line) for line in lines]

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
n = len(lines)
m = len(lines[0])
start = (-1, -1)
for i in range(n):
    for j in range(m):
        if lines[i][j] == "^":
            start = (i, j)
            break
    if start != (-1, -1):
        break


def simulate(grid):
    direction = 0
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    pos = start

    while True:
        newpos = (pos[0] + DIRS[direction][0], pos[1] + DIRS[direction][1])
        if newpos[0] < 0 or newpos[0] >= n or newpos[1] < 0 or newpos[1] >= m:
            return grid, False
        if grid[newpos[0]][newpos[1]] == "#":
            direction = (direction + 1) % 4
        elif visited[newpos[0]][newpos[1]][direction]:
            return grid, True  # Loop
        else:
            pos = newpos
            grid[pos[0]][pos[1]] = "X"
            visited[pos[0]][pos[1]][direction] = True


def part_1() -> str | int:
    total = 0

    grid, _ = simulate(copy.deepcopy(lines))

    for line in grid:
        total += line.count("X") + line.count("^")

    return total


def part_2() -> str | int:
    total = 0

    for i in range(n):
        for j in range(m):
            if lines[i][j] == ".":
                grid = copy.deepcopy(lines)
                grid[i][j] = "#"

                grid, loop = simulate(grid)

                if loop:
                    total += 1

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
