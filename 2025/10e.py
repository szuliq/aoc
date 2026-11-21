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
    print(desired_joltage)

    def sum_solution(solution):
        joltage = [0] * len(desired_joltage)

        for element in solution:
            for i in range(len(desired_joltage)):
                joltage[i] += element[i]

        return tuple(joltage)

    def check_combination(combination):
        solution = []
        for button, x in zip(buttons, combination):
            val = tuple((x if j in button else 0 for j in range(len(desired_joltage))))
            solution.append(val)

        return sum_solution(solution) == desired_joltage

    # Maximum possible presses needed per button
    max_presses_per_button = [max(desired_joltage) for _ in buttons]

    # Try increasing sums (total presses) until we find a solution
    for total_presses in range(sum(desired_joltage) + 1):
        for combination in itertools.product(
            *[range(m + 1) for m in max_presses_per_button]
        ):
            if sum(combination) == total_presses:
                if check_combination(combination):
                    print("found solution", combination)
                    return sum(combination)

    return 0


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
