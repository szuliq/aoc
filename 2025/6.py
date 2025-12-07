import functools
import operator

sum = 0

lines = []

OPERATIONS = {"+": (operator.add, 0), "*": (operator.mul, 1)}

with open("6.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.split())


for *numbers, operation in zip(*lines):
    op, start = OPERATIONS[operation]
    sum += functools.reduce(op, map(int, numbers), start)

print(sum)
