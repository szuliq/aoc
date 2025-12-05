import itertools

sum = 0


def is_invalid(number: int) -> bool:
    digits = str(number)

    for divider in range(1, (len(digits) // 2) + 1):
        if len(digits) % divider != 0:
            continue

        batches = list(itertools.batched(digits, divider))

        if all(batch == batches[0] for batch in batches):
            return True

    return False


with open("2.txt", "r") as file:
    line = file.readline()

    for value in line.split(","):
        current, end = map(int, value.split("-"))

        while current <= end:
            if is_invalid(current):
                print(current)
                sum += current

            current += 1

print(sum)
