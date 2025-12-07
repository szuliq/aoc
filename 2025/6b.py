import functools
import operator

sum = 0

lines = []

OPERATIONS = {"+": (operator.add, 0), "*": (operator.mul, 1)}


def unravel(numbers):
    return list(int("".join(number)) for number in zip(*numbers))


with open("6.txt", "r") as file:
    lines = list(file.readlines())


col_lengths = []
curr = 0
for char in lines[-2]:
    if char == " ":
        curr += 1
    else:
        if curr > 0:
            col_lengths.append(curr - 1)
        curr = 1

col_lengths[-1] += 1

spaced_lines = []
for line in lines:
    new_line = []
    used = 0
    for length in col_lengths:
        new_line.append(line[used : used + length])
        used += length + 1
    spaced_lines.append(new_line)


for *numbers, operation in zip(*spaced_lines[:-1]):
    operation = operation.strip()

    if operation not in OPERATIONS:
        continue

    op, start = OPERATIONS[operation]
    sum += functools.reduce(op, unravel(numbers), start)
