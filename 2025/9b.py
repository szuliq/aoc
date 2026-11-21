import functools
import itertools

corners = []
horizontal_edge_points = set()
vertical_edge_points = set()
previous_corner = None
max_x = 0
max_y = 0
# crosses_vertical_cache = {}
inside = set()


def mark_edge(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    if x1 == x2:
        if y1 < y2:
            for y in range(y1 + 1, y2 + 1):
                vertical_edge_points.add((x1, y))
        else:
            for y in range(y2 + 1, y1 + 1):
                vertical_edge_points.add((x1, y))
    elif y1 == y2:
        if x1 < x2:
            for x in range(x1 + 1, x2 + 1):
                horizontal_edge_points.add((x, y1))
        else:
            for x in range(x2 + 1, x1 + 1):
                horizontal_edge_points.add((x, y1))


with open("9-0.txt", "r") as file:
    for line in file.readlines():
        corner = tuple(map(int, line.strip().split(",")))
        corners.append(corner)
        if previous_corner:
            mark_edge(previous_corner, corner)
        previous_corner = corner
        max_x = max(max_x, corner[0])
        max_y = max(max_y, corner[1])
    mark_edge(previous_corner, corners[0])
    corners = set(corners)


for y in range(max_y + 1):
    crossed = 0
    for x in range(max_x + 1):
        if (x, y) in vertical_edge_points:
            crossed += 1
        if crossed % 2 == 1:
            inside.add((x, y))

inside |= corners
inside |= horizontal_edge_points
inside |= vertical_edge_points


def rectangle(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def points_in_edge(edge):
    (x1, y1), (x2, y2) = edge

    points = set()

    if x1 == x2:
        if y1 < y2:
            for y in range(y1, y2 + 1):
                points.add((x1, y))
        else:
            for y in range(y2, y1 + 1):
                points.add((x1, y))
    elif y1 == y2:
        if x1 < x2:
            for x in range(x1, x2 + 1):
                points.add((x, y1))
        else:
            for x in range(x2, x1 + 1):
                points.add((x, y1))

    return points


def is_good(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    a = c1, (x1, y2)
    b = c1, (x2, y1)
    c = c2, (x1, y2)
    d = c2, (x2, y1)

    points = (
        points_in_edge(a) | points_in_edge(b) | points_in_edge(c) | points_in_edge(d)
    )

    return all(point in inside for point in points)


rectangles = []

for c1, c2 in itertools.combinations(corners, 2):
    size = rectangle(c1, c2)
    rectangles.append((size, (c1, c2)))

for size, (c1, c2) in sorted(rectangles, reverse=True):
    print(size, c1, c2)
    if is_good(c1, c2):
        print(size)
        break


for y in range(max_y + 3):
    for x in range(max_x + 3):
        if (x, y) in inside:
            print("#", end="")
        else:
            print(".", end="")
    print()

# import pdb

# pdb.set_trace()
