import itertools

sum = 0


def digits_to_number(so_far, digits):
    so_far = so_far * 10 + digits[0]

    if len(digits) > 1:
        return digits_to_number(so_far, digits[1:])
    else:
        return so_far


def biggest_joltage(row):
    head = int(row[0])
    tail = row[1:]

    if len(tail) > 12:
        jolt = biggest_joltage(tail)

        possible_best = [jolt]
        for combination in itertools.combinations(jolt, 11):
            possible_best.append(tuple([head] + list(combination)))
        return max(possible_best)
    else:
        return tuple([head] + list(map(int, tail[:-1])))


with open("3.txt", "r") as file:
    for line in file.readlines():
        jolt = biggest_joltage(line)

        print(jolt)

        sum += digits_to_number(0, jolt)

print(sum)
