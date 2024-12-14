import os, sys, re, math, itertools, functools, collections, copy, fractions

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.read().strip()
    stones = [int(n) for n in lines.split(" ")]


@functools.cache
def count(stone, n):
    if n == 0:
        return 1

    if stone == 0:
        return count(1, n - 1)

    elif math.floor(math.log10(stone)) % 2 == 1:
        d = math.pow(10, math.floor(math.log10(stone)) // 2 + 1)
        total = count(stone // d, n - 1)
        total += count(stone % d, n - 1)
        return total

    else:
        return count(stone * 2024, n - 1)


def part_1() -> str | int:
    total = 0

    for stone in stones:
        total += count(stone, 25)

    return total


def part_2() -> str | int:
    total = 0

    for stone in stones:
        total += count(stone, 75)

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
