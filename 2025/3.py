sum = 0


def biggest_joltage(row):
    head = int(row[0])
    tail = row[1:]

    if len(tail) > 2:
        x, y = biggest_joltage(tail)
        return max((head, x), (head, y), (x, y))
    else:
        return head, int(tail[0])


with open("3.txt", "r") as file:
    for line in file.readlines():
        x, y = biggest_joltage(line)
        # print(x, y)
        sum += 10 * x + y

print(sum)
