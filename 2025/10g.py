import itertools
import math

from sympy import Eq, solve, symbols


def parse_button(button_str):
    parts = button_str[1:-1].split(",")
    return list(map(int, parts))


def get_presses(solution):
    return sum(max(element) for element in solution)


def find_desired_joltage(desired_joltage, buttons):
    def min_for_button(button):
        return min(desired_joltage[i] for i in button)

    button_symbols = symbols([f"b{i}" for i in range(len(buttons))], nonnegative=True)
    ranges = {
        button_symbol: range(min_for_button(button) + 1)
        for button_symbol, button in zip(button_symbols, buttons)
    }

    print(button_symbols)

    eqs = []

    for i, value in enumerate(desired_joltage):
        vars = []
        for j, button_symbol in enumerate(button_symbols):
            if i in buttons[j]:
                vars.append(button_symbol)
        equation = Eq(sum(vars), value)
        eqs.append(equation)

    solution = solve(eqs, button_symbols)
    print("solution:", solution)
    print("solution types:", [type(x) for x in solution.values()])

    bound_vars = set(solution.keys())
    free_vars = set(button_symbols) - bound_vars
    print("bound vars:", bound_vars)
    print("free vars:", free_vars)

    min_sum = math.inf

    for combination in itertools.product(*[ranges[var] for var in free_vars]):
        temp_values = dict(zip(free_vars, combination))

        potential_parts = list(combination)

        for var, expr in solution.items():
            if (res := expr.subs(temp_values)) in ranges[var]:
                potential_parts.append(res)
            else:
                potential_parts.append(math.inf)

        # print(f"{combination=} {potential_parts=} sum={sum(potential_parts)}")
        min_sum = min(min_sum, sum(potential_parts))

    print(min_sum)
    print()
    return min_sum


agg = 0

with open("10-0.txt", "r") as file:
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
