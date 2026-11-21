import functools
import itertools
import math
from multiprocessing import Pool


def parse_button(button_str):
    parts = button_str[1:-1].split(",")
    return list(map(int, parts))


def flip(button, joltage):
    return tuple(x - 1 if i in button else x for i, x in enumerate(joltage))


def index_with_min_joltage(joltage):
    min_value = math.inf
    index = None

    for i, x in enumerate(joltage):
        if x > 0 and x < min_value:
            min_value = x
            index = i

    return index


def find_desired_joltage(desired_joltage, buttons, row, steps=0, global_min=math.inf):
    if steps == 0:
        print(f"starting row {row}")

    if steps > global_min:
        print(f"{steps=} {global_min=} stopping early")
        return math.inf

    index = index_with_min_joltage(desired_joltage)

    if index is None:
        return 0

    index_buttons = [
        button
        for button in buttons
        if index in button and not any(desired_joltage[i] == 0 for i in button)
    ]
    index_buttons = sorted(index_buttons, key=lambda b: -len(b))

    if min(jolt for jolt in desired_joltage if jolt != 0) > len(index_buttons):
        index_buttons = index_buttons[:1]

    for button in index_buttons:
        joltage = flip(button, desired_joltage)

        print("step", steps, "button:", button, "from", desired_joltage, "to", joltage)

        if any(x < 0 for x in joltage):
            # print("negative", joltage)
            continue

        solution = find_desired_joltage(
            joltage, buttons, row, steps=steps + 1, global_min=global_min
        )
        global_min = min(global_min, solution)

    return global_min + 1


agg = 0

with open("10-0.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        _, *buttons, desired_joltage = line.strip().split()

        desired_joltage = tuple(int(x) for x in desired_joltage[1:-1].split(","))
        buttons = [parse_button(button) for button in buttons]

        agg += find_desired_joltage(desired_joltage, buttons, i)

print(agg)
