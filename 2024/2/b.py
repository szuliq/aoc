import itertools
import math

good = 0

def is_good(numbers):
    previous, rest = numbers[0], numbers[1:]
    changes = []

    while rest:
        current, rest = rest[0], rest[1:]
        changes.append(previous - current)
        previous = current

    signs = {math.signbit(x) for x in changes}
    abs_changes = {abs(x) for x in changes}

    if len(signs) == 1 and all(1 <= x <= 3 for x in abs_changes):
        return True


with open('data.txt') as fh:
    for line in fh.readlines():
        numbers = list(map(int, line.split()))

        for comb in itertools.combinations(numbers, len(numbers) - 1):
            if is_good(comb):
                good += 1
                break


print(good)
