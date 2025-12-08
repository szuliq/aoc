import itertools
import math

points = {}
distances = []


def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


with open("8.txt", "r") as file:
    for line in file.readlines():
        point = tuple(map(int, line.strip().split(",")))
        points[point] = frozenset([point])

for p1, p2 in itertools.combinations(points.keys(), 2):
    distances.append((dist(p1, p2), p1, p2))


for _, p1, p2 in sorted(distances):
    s1 = points[p1]
    s2 = points[p2]
    union = frozenset(s1 | s2)
    for p in union:
        points[p] = union

    groups = set(points.values())

    if len(groups) == 1:
        print(p1[0] * p2[0])
        break
