with open("data.in") as fh:
    line = fh.readline()

disk = []
in_file = True
file_no = 0

for digit in line.strip():
    for _ in range(int(digit)):
        if in_file:
            disk.append(str(file_no))
        else:
            disk.append(".")

    if in_file:
        file_no += 1

    in_file = not in_file

index = 0
back_index = len(disk)

# print("".join(disk))

while True:
    if index == back_index:
        break

    if disk[index] == ".":
        while True:
            back_index -= 1

            if disk[back_index] != ".":
                disk[index] = disk[back_index]
                disk[back_index] = "."
                # print("".join(disk))
                break

    index += 1

print(sum(i * int(x) for (i, x) in enumerate(disk) if x != "."))
