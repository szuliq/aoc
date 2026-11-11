from collections import defaultdict

point_to_level = {}
level_to_points = defaultdict(set)
point_rating = defaultdict(lambda: 0)

max_x, max_y = 0, 0
with open("data.in") as fh:
    for y, line in enumerate(fh.readlines()):
        max_y = max(max_y, y)

        for x, level in enumerate(line):
            max_x = max(max_x, x)

            point_to_level[(x, y)] = level
            level_to_points[level].add((x, y))

            if level == "9":
                point_rating[(x, y)] += 1


def neighbours(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


for level in map(str, range(9, 0, -1)):
    for x, y in level_to_points[level]:
        for a, b in neighbours(x, y):
            if point_to_level.get((a, b)) == str(int(level) - 1):
                point_rating[(a, b)] += point_rating[(x, y)]


def draw_scores():
    for y in range(max_y):
        for x in range(max_x):
            score = point_rating[(x, y)]
            print(score if score < 10 else ".", end="")
        print()
    print()


# draw_scores()

sum = 0
for point in level_to_points["0"]:
    sum += point_rating[point]
print(sum)
