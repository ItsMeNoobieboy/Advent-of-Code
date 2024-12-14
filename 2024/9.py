import os, sys, re, math, itertools, functools, collections, copy, fractions

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    disk_map = f.read().strip()


def part_1() -> str | int:
    total = 0

    id_num = 0
    space = False
    blocks = []
    for c in disk_map:
        if space:
            blocks += ["."] * int(c)
        else:
            blocks += [id_num] * int(c)
            id_num += 1
        space = not space

    while "." in blocks:
        last = blocks.pop()
        if last == ".":
            continue
        blocks[blocks.index(".")] = last

    for i, val in enumerate(blocks):
        total += i * val

    return total


def part_2() -> str | int:
    total = 0

    id_num = 0
    space = False
    blocks = []
    for c in disk_map:
        if space:
            blocks.append([".", int(c)])
        else:
            blocks.append([id_num, int(c)])
            id_num += 1
        space = not space

    i = len(blocks) - 1
    while i >= 0:
        if blocks[i][0] == ".":
            i -= 1
            continue

        for j in range(i):
            if blocks[j][0] != ".":
                continue
            if blocks[j][1] > blocks[i][1]:
                blocks[j][1] -= blocks[i][1]
                blocks.insert(j, list(blocks[i]))
                i += 1
                blocks[i][0] = "."
                break
            elif blocks[j][1] == blocks[i][1]:
                blocks[i], blocks[j] = blocks[j], blocks[i]
                break

        i -= 1

    counter = 0
    for i in range(len(blocks)):
        if blocks[i][0] == ".":
            counter += blocks[i][1]
            continue
        total += (2 * counter + blocks[i][1] - 1) / 2 * blocks[i][1] * blocks[i][0]
        counter += blocks[i][1]

    if total % 1 != 0:
        raise Exception("Something went wrong")

    return int(total)


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
