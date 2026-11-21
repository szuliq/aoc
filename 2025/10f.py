import functools
import itertools
import math
from multiprocessing import Pool

from constraint import Problem, RecursiveBacktrackingSolver

cache = {}


def parse_button(button_str):
    parts = button_str[1:-1].split(",")
    return list(map(int, parts))


def get_presses(solution):
    return sum(max(element) for element in solution)


def find_desired_joltage(desired_joltage, buttons):
    problem = Problem(RecursiveBacktrackingSolver())

    for i, button in enumerate(buttons):
        problem.addVariable(i, list(range(min(desired_joltage[i] for i in button) + 1)))

        # val = tuple((1 if j in button else 0 for )))
        # print(val)

    for j in range(len(desired_joltage)):

        def constraint(*args, j=j):
            return (
                sum(args[i] if j in buttons[i] else 0 for i in range(len(buttons)))
                == desired_joltage[j]
            )

        problem.addConstraint(constraint, range(len(buttons)))

    solutions = problem.getSolutions()

    min_presses = math.inf
    for solution in solutions:
        min_presses = min(min_presses, sum(solution.values()))
    return min_presses


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
