import os, sys, re, math, itertools, functools, collections, copy, fractions


class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self, t):
        self.x += t * self.vx
        self.y += t * self.vy
        self.x %= 101
        self.y %= 103

    def get_quadrant(self):
        if self.x < 50 and self.y < 51:
            return 1
        elif self.x > 50 and self.y < 51:
            return 2
        elif self.x > 50 and self.y > 51:
            return 3
        elif self.x < 50 and self.y > 51:
            return 4
        else:
            return 0


input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.read().splitlines()
    robots = []
    for line in lines:
        x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
        robots.append(Robot(x, y, vx, vy))
    # For parsing lines of integers
    # lines = [[int(n) for n in line.split(" ")] for line in lines]


def part_1() -> str | int:
    total = 0

    for robot in robots:
        robot.move(100)

    quadrants = [0] * 5

    for robot in robots:
        quadrants[robot.get_quadrant()] += 1

    total = quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]

    return total


def print_grid(robots):
    grid = [["."] * 101 for _ in range(103)]
    for robot in robots:
        grid[robot.y][robot.x] = "#"

    for row in grid:
        print("".join(row))


def part_2() -> str | int:
    total = 0

    for robot in robots:
        robot.move(-100)

    while True:
        for robot in robots:
            robot.move(1)
        total += 1

        positions = {(robot.x, robot.y) for robot in robots}
        if len(positions) == len(robots):
            break

    print_grid(robots)

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
