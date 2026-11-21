import copy
import functools
import random
import string

presents = {}
reading_present = None
present = []


def rotate_90(present):
    rotated_present = [[0] * len(present) for _ in range(len(present))]

    for i in range(len(present)):
        for j in range(len(present)):
            rotated_present[j][len(present) - 1 - i] = present[i][j]

    return rotated_present


def scan_points(present):
    points = set()

    for i, line in enumerate(present):
        for j, char in enumerate(line):
            if char == "#":
                points.add((i, j))

    return frozenset(points)


def finalize_present(present):
    points = scan_points(present)
    rotations = [points]

    for i in range(3):
        present = rotate_90(present)
        points = scan_points(present)
        if points not in rotations:
            rotations.append(points)

    return rotations


def can_fit_presents(grid, requirement):
    presents_to_fit = []

    for i, val in enumerate(requirement):
        for _ in range(val):
            presents_to_fit.append(i)

    grid_x, grid_y = grid

    region = set()
    for i in range(grid_x):
        for j in range(grid_y):
            region.add((i, j))
    region = frozenset(region)

    solution = [["."] * grid_x for _ in range(grid_y)]

    result, solution = rec(grid, region, presents_to_fit, solution)

    print_solution(solution)

    return result


def rec(grid, region, presents_to_fit, solution):
    if not presents_to_fit:
        return True, solution

    current_present = presents_to_fit[0]
    rotations = presents[current_present]

    for rotation in rotations:
        new_region, new_solution = _can_fit_rotation(grid, region, rotation, solution)
        if new_region:
            # print(region)
            # print(new_region)
            # print(presents_to_fit[1:])
            print_solution(new_solution)

            result, fin = rec(grid, new_region, presents_to_fit[1:], new_solution)
            if result:
                return result, fin

    return False, solution


def _can_fit_rotation(grid, region, rotation, solution):
    x, y = grid

    for offset_x, offset_y in sorted(region):
        shape = offset_rotation(rotation, offset_x, offset_y)

        if shape <= region:
            new_solution = mark_shape_on_solution(solution, shape)
            return region - shape, new_solution

    return frozenset(), solution


# def _can_fit_rotation(grid, region, rotation, solution):
#     for subregion in generate_subregions(grid, region):
#         if shape := _can_fit_rotation_in_subregion(subregion, rotation):
#             new_solution = mark_shape_on_solution(solution, shape)
#             return region - shape, new_solution

#     return frozenset(), solution


# def generate_subregions(grid, region):
#     x, y = grid

#     for i in range(x):
#         for j in range(y):
#             yield frozenset(
#                 (x, y) for x, y in region if i <= x < i + 5 and j <= y < j + 5
#             )


# @functools.lru_cache(None)
# def _can_fit_rotation_in_subregion(subregion, rotation):
#     for offset_x, offset_y in sorted(subregion):
#         shape = offset_rotation(rotation, offset_x, offset_y)

#         if shape <= subregion:
#             return shape

#     return None


def offset_rotation(rotation, offset_x, offset_y):
    return frozenset((x + offset_x, y + offset_y) for x, y in rotation)


def mark_shape_on_solution(solution, shape):
    let = random.choice(string.ascii_uppercase)

    new_solution = copy.deepcopy(solution)

    for x, y in shape:
        row = new_solution[y]
        row[x] = let

    return new_solution


def print_solution(solution):
    for row in solution:
        print("".join(row))
    print()


agg = 0

with open("12-1.txt", "r") as file:
    for line in file:
        if reading_present is not None:
            if line.strip() == "":
                presents[reading_present] = finalize_present(present)
                present = []
                reading_present = None
            else:
                present.append(line.strip())

            continue

        parts = line.strip().split(":")

        if len(parts) == 2 and parts[1].strip() == "":
            reading_present = int(parts[0])
            continue
        elif len(parts) == 2:
            print(line)

            grid_size, requirement = parts

            grid_size = tuple(map(int, grid_size.strip().split("x")))
            requirement = list(map(int, requirement.strip().split()))

            agg += can_fit_presents(grid_size, requirement)


print(agg)
