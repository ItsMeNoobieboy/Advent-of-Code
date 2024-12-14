import os, sys, re, math, itertools, functools, collections, operator

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    horizontal_lines = f.readlines()


def part_1() -> str | int:
    total = 0

    vertical_lines = []
    for i in range(len(horizontal_lines[0])):
        vertical_lines.append("".join([line[i] for line in horizontal_lines]))

    diagonal_lines_1 = [""] * (len(horizontal_lines) + len(horizontal_lines[0]) - 1)
    diagonal_lines_2 = [""] * (len(horizontal_lines) + len(horizontal_lines[0]) - 1)
    for i in range(len(horizontal_lines)):
        for j in range(len(horizontal_lines[0])):
            diagonal_lines_1[i + j] += horizontal_lines[i][j]
            diagonal_lines_2[i + j] += horizontal_lines[i][~j]

    for line in horizontal_lines:
        total += line.count("XMAS") + line.count("SAMX")

    for line in vertical_lines:
        total += line.count("XMAS") + line.count("SAMX")

    for line in diagonal_lines_1 + diagonal_lines_2:
        total += line.count("XMAS") + line.count("SAMX")

    return total


def part_2() -> str | int:
    total = 0

    for i, line in enumerate(horizontal_lines):
        if i >= len(horizontal_lines) - 2:
            break

        index = -1
        while True:
            # Find next M or S (as top left corner)
            index_m = line.find("M", index + 1)
            index_s = line.find("S", index + 1)
            if index_m == -1 and index_s == -1:
                break
            if index_m == -1:
                index = index_s
            elif index_s == -1:
                index = index_m
            else:
                index = min(index_m, index_s)

            if index >= len(line) - 2:
                break

            # Check other corners
            if (
                line[index + 2] not in "MS"
                or horizontal_lines[i + 2][index] not in "MS"
                or horizontal_lines[i + 2][index + 2] not in "MS"
            ):
                continue

            # Check center
            if horizontal_lines[i + 1][index + 1] != "A":
                continue

            # Make sure diagonals are not equal
            if (
                horizontal_lines[i + 2][index] == line[index + 2]
                or horizontal_lines[i + 2][index + 2] == line[index]
            ):
                continue

            total += 1

    return total


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
