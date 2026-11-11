from collections import defaultdict

with open("data.in") as fh:
    line = fh.readline()

disk = []
in_file = True
file_no = 0

full_blocks = []
free_blocks = defaultdict(list)


for digit in line.strip():
    if in_file:
        full_blocks.append((len(disk), int(digit)))
    else:
        free_blocks[int(digit)].append(len(disk))


    for _ in range(int(digit)):
        if in_file:
            disk.append(str(file_no))
        else:
            disk.append(".")

    if in_file:
        file_no += 1

    in_file = not in_file


# print(full_blocks)
print(free_blocks.keys())
print("".join(f"[{x}]" for x in disk))


for full_block_index, full_block_size in reversed(full_blocks):
    most_left_available_size = 0
    most_left_available_place = len(disk)

    # if full_block_index == 11:
    #     import ipdb; ipdb.set_trace()

    for free_block_size, places in free_blocks.items():
        if places and free_block_size >= full_block_size:
            place = places[0]

            if place < most_left_available_place:
                most_left_available_place = place
                most_left_available_size = free_block_size

    if most_left_available_size and most_left_available_place < full_block_index:
        # print(f"moving index {full_block_index} size {full_block_size}")
        # print(f"to {most_left_available_place} size {most_left_available_size}")

        free_blocks[most_left_available_size].pop(0)

        for diff in range(full_block_size):
            disk[most_left_available_place + diff] = disk[full_block_index + diff]
            disk[full_block_index + diff] = "."

        if (leftover_size := most_left_available_size - full_block_size) > 0:
            leftover_position = most_left_available_place + full_block_size
            free_blocks[leftover_size].append(leftover_position)
            free_blocks[leftover_size].sort()
    # else:
    #     print(f"no space for {full_block_index} size {full_block_size}")

    # print(free_blocks)
    # print("".join(disk))
    # print()


print("".join(f"[{x}]" for x in disk))
print(sum(i * int(x) for (i, x) in enumerate(disk) if x != "."))
