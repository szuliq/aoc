import itertools
from collections import defaultdict

antenas = defaultdict(set)
field = set()
antinodes = set()
max_x, max_y = 0, 0


with open("data.in") as fh:
    for y, line in enumerate(fh.readlines()):
        max_y = max(max_y, y)

        for x, char in enumerate(line):
            max_x = max(max_x, x)

            match char:
                case ".":
                    field.add((x, y))
                case "\n":
                    pass
                case _:
                    field.add((x, y))
                    antenas[char].add((x, y))

rev_antenas = {}

for freq, points in antenas.items():
    for point in points:
        rev_antenas[point] = freq


def draw():
    for y in range(max_y):
        for x in range(max_x):
            letter = "#" if (x, y) in antinodes else "."
            letter = rev_antenas.get((x, y), letter)
            print(letter, end="")
        print()
    print()


# print(antenas)


def compute_antinodes(a, b):
    yield a
    yield b
    yield from compute_antinode_echo(a, b)
    yield from compute_antinode_echo(b, a)


def compute_antinode_echo(a, b):
    (x1, y1), (x2, y2) = a, b

    dx, dy = (x2 - x1, y2 - y1)

    mult = 1

    while True:
        antinode = x1 - mult * dx, y1 - mult * dy
        if antinode in field:
            mult += 1
            yield antinode
        else:
            break


for _, points in antenas.items():
    for a, b in itertools.combinations(points, 2):
        for antinode in compute_antinodes(a, b):
            antinodes.add(antinode)


# print(antinodes)
draw()

print(len(antinodes))
