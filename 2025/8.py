import functools
import itertools
import math
import operator

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

# print(distances)

for _, p1, p2 in sorted(distances)[:1000]:
    # print(p1, p2)
    s1 = points[p1]
    s2 = points[p2]
    union = frozenset(s1 | s2)
    for p in union:
        points[p] = union

groups = set(points.values())
lengths = (len(g) for g in groups)
print(functools.reduce(operator.mul, sorted(lengths, reverse=True)[:3], 1))
