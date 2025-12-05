sum = 0
fresh = []


def unify():
    fresh.sort()

    for i, (start, end) in enumerate(fresh):
        try:
            next_start, next_end = fresh[i + 1]
        except IndexError:
            return False

        if next_start <= end <= next_end:
            fresh.remove((start, end))
            fresh.remove((next_start, next_end))
            fresh.append((start, next_end))
            return True
        elif next_end <= end:
            fresh.remove((next_start, next_end))
            return True


with open("5.txt", "r") as file:
    for line in file.readlines():
        if line.strip() == "":
            break

        start, end = line.strip().split("-")
        fresh.append((int(start), int(end)))

while True:
    change = unify()
    if not change:
        break

for start, end in fresh:
    sum += end - start + 1

print(sum)
