sum = 0
reading_fresh = True
fresh = []


def is_fresh(available):
    for start, end in fresh:
        if start <= available <= end:
            return True
    return False


with open("5.txt", "r") as file:
    for line in file.readlines():

        if line.strip() == "":
            reading_fresh = False
            continue

        if reading_fresh:
            start, end = line.strip().split("-")
            fresh.append((int(start), int(end)))
        else:
            available = int(line.strip())
            if is_fresh(available):
                sum += 1

print(sum)
