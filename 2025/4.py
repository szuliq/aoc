from collections import defaultdict

sum = 0
orig = []


with open("4.txt", "r") as file:
    for line in file.readlines():
        orig.append(list(char == "@" for char in line.strip()))


while True:
    change = 0

    roll_counts = defaultdict(lambda: defaultdict(int))

    for i, row in enumerate(orig):
        for j, val in enumerate(row):
            if val:
                roll_counts[i - 1][j - 1] += 1
                roll_counts[i - 1][j] += 1
                roll_counts[i - 1][j + 1] += 1
                roll_counts[i][j - 1] += 1
                roll_counts[i][j + 1] += 1
                roll_counts[i + 1][j - 1] += 1
                roll_counts[i + 1][j] += 1
                roll_counts[i + 1][j + 1] += 1

    for i, row in enumerate(orig):
        for j, val in enumerate(row):
            if val and roll_counts[i][j] < 4:
                change += 1
                orig[i][j] = False
                # print("x", end="")
            # elif val:
            #     print("@", end="")
            # else:
            #     print(".", end="")
        # print()
        # print()

    if change:
        sum += change
    else:
        break


print(sum)
