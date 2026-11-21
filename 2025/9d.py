import itertools

corners = []
edges = []

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
        corner = tuple(map(int, line.strip().split(",")))
        corners.append(corner)

        if previous_corner:
            mark_edge(previous_corner, corner)

        previous_corner = corner

        max_x = max(max_x, corner[0])
        max_y = max(max_y, corner[1])

    mark_edge(previous_corner, corners[0])

edge_points = horizontal_edge_points | vertical_edge_points | set(corners)


def crosses_vertical(point):
    x, y = point

    result = 0

    while x >= 0:
        if (x, y) in crosses_vertical_cache:
            result += crosses_vertical_cache[(x, y)]
            break
        elif (x, y) in vertical_edge_points:
            result += 1
            crosses_vertical_cache[(x, y)] = result

        x -= 1

    return result


def is_inside(point):
    if point in edge_points:
        return True
    else:
        x, y = point
        crossed_edges = crosses_vertical((x - 1, y))
        return crossed_edges % 2 == 1


def rectangle(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2

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


def are_other_corners_inside(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    return is_inside((x1, y2)) and is_inside((x2, y1))


def is_good(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    if not are_other_corners_inside(c1, c2):
        return False

    for x in range(min(x1, x2) + 1, max(x1, x2)):
        ys = x_to_y[x]

        if any(min(y1, y2) < y < max(y1, y2) for y in ys):
            return False

    return True


rectangles = []

for c1, c2 in itertools.combinations(corners, 2):
    size = rectangle(c1, c2)
    rectangles.append((size, (c1, c2)))

for size, (c1, c2) in sorted(rectangles, reverse=True):
    print(size, c1, c2)
    if is_good(c1, c2):
        print(size)
        break

# print(is_good((94543, 50265), (5459, 67484)))

# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         if is_inside((x, y)):
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

# import pdb

# pdb.set_trace()
