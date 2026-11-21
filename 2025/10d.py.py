import functools
import itertools
import math
from multiprocessing import Pool

cache = {}


def parse_button(button_str):
    parts = button_str[1:-1].split(",")
    return list(map(int, parts))


def get_presses(solution):
    return sum(max(element) for element in solution)


def find_desired_joltage(desired_joltage, buttons):
    def sum_solution(solution):
        joltage = [0] * len(desired_joltage)

        for element in solution:
            for i in range(len(desired_joltage)):
                joltage[i] += element[i]

        return tuple(joltage)

    def too_big(solution):
        joltage = sum_solution(solution)
        return any(x > y for x, y in zip(joltage, desired_joltage))

    def min_for_button(button):
        return min(desired_joltage[i] for i in button)

    empty_solution = frozenset()
    cache[empty_solution] = (0,) * len(desired_joltage)
    solutions = {empty_solution}

    for button in buttons:
        next_solutions = set()

        max_i = min_for_button(button)

        for i in range(max_i + 1):
            new_element = tuple(
                (i if j in button else 0 for j in range(len(desired_joltage)))
            )

            # print(new_element)

            for solution in solutions:
                new_solution = solution | {new_element}
                if not too_big(new_solution):
                    value = cache[solution]
                    cache[new_solution] = [x + y for x, y in zip(value, new_element)]
                    next_solutions.add(new_solution)

            # candidates = [solution | {new_element} for solution in solutions]
            # good_candidates = [x for x in candidates if not too_big(x)]
            # # print(candidates)

            # next_solutions.update(good_candidates)

            # print(next_solutions)
            # print()

        solutions = next_solutions

    print("calculating correct solutions")

    correct_solutions = [
        solution for solution in solutions if sum_solution(solution) == desired_joltage
    ]

    # print(f"{correct_solutions=}")

    return min(get_presses(solution) for solution in correct_solutions)


agg = 0

with open("10.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        _, *buttons, desired_joltage = line.strip().split()

        desired_joltage = tuple(int(x) for x in desired_joltage[1:-1].split(","))
        buttons = [parse_button(button) for button in buttons]

        # print(desired_joltage, buttons)
        # print("===")
        print(f"{i}")

        agg += find_desired_joltage(desired_joltage, buttons)

print()
print(agg)
