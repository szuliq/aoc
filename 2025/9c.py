import itertools
from collections import defaultdict

corners = []
x_to_y = defaultdict(list)
corners = []
max_x = 0
max_y = 0
previous_corner = None

horizontal_edge_points = set()
vertical_edge_points = set()

crosses_vertical_cache = {}


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


with open("9.txt", "r") as file:
    for line in file.readlines():
        x, y = tuple(map(int, line.strip().split(",")))
        corners.append((x, y))
        x_to_y[x].append(y)

        if previous_corner:
            mark_edge(previous_corner, (x, y))

        previous_corner = (x, y)

        max_x = max(max_x, x)
        max_y = max(max_y, y)

    mark_edge(previous_corner, corners[0])

edge_points = horizontal_edge_points | vertical_edge_points | set(corners)


def rectangle(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def crosses_vertical(point):
    if result := crosses_vertical_cache.get(point):
        return result

    x, y = point

    if x > max_x:
        return 0
    else:
        result = 0

        for i in range(x, max_x + 1):
            if (i, y) in crosses_vertical_cache:
                result += crosses_vertical_cache[(i, y)]
                break
            elif (i, y) in vertical_edge_points:
                result += 1

            crosses_vertical_cache[(i, y)] = result

        crosses_vertical_cache[point] = result

        return result


def is_inside(point):
    if point in edge_points:
        return True
    else:
        x, y = point
        crossed_edges = crosses_vertical((x + 1, y))
        return crossed_edges % 2 == 1


def are_other_corners_inside(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    return is_inside((x1, y2)) and is_inside((x2, y1))


def no_other_corner_inside(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    for x in range(min(x1, x2) + 1, max(x1, x2)):
        ys = x_to_y[x]

        if any(min(y1, y2) < y < max(y1, y2) for y in ys):
            return False

    return True


rectangles = []

for c1, c2 in itertools.combinations(corners, 2):
    size = rectangle(c1, c2)
    if are_other_corners_inside(c1, c2):
        rectangles.append((size, (c1, c2)))

for size, (c1, c2) in sorted(rectangles, reverse=True):
    print(size, c1, c2)
    if no_other_corner_inside(c1, c2):
        print(size)
        break

print(no_other_corner_inside((94543, 50265), (5459, 67484)))


# import pdb

# pdb.set_trace()
