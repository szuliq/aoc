from collections import defaultdict

forward = defaultdict(list)
backwards = defaultdict(list)
ways = defaultdict(lambda: [0, 0, 0])

with open("11.txt", "r") as file:
    for line in file.readlines():
        start, ends = line.strip().split(":")
        ends = ends.strip().split()

        for end in ends:
            forward[start].append(end)
            backwards[end].append(start)

ways["out"] = (1, 0, 0)


# def find_paths(current, path=set()):
#     for next in backwards[current]:
#         if next == "you":
#             print("increasing me", current)
#         ways[next] += ways[current]

#     print(current, path, ways["bbb"], ways["ccc"])

#     for next in backwards[current]:
#         if next != "you":
#             find_paths(next, path | {next})

queue = ["out"]
seen = set()

while queue:
    current = queue.pop(0)

    # print(current, queue, dict(ways))

    if any(children in queue for children in forward[current]):
        queue.append(current)
        continue

    seen.add(current)

    normal, dac, fft = ways[current]

    for next in backwards[current]:
        if next == "dac":
            ways[next][0] = 0
            ways[next][1] += normal
            ways[next][2] += fft
        elif next == "fft":
            ways[next][0] = 0
            ways[next][1] += dac
            ways[next][2] += normal
        else:
            ways[next][0] += normal
            ways[next][1] += dac
            ways[next][2] += fft

        if next in seen:
            continue

        if next not in queue:
            queue.append(next)

# def find_paths():
#     current_layer = {"out"}
#     next_layer = set()
#     seen = set()

#     while current_layer:
#         print(current_layer, ways)
#         for edge in current_layer:

#             # if edge == "you":
#             #     return ways["you"]

#             # if edge in seen:
#             #     continue

#             # seen.add(edge)

#             for next in backwards[edge]:
#                 ways[next] += ways[edge]
#                 next_layer.add(next)

#         current_layer, next_layer = next_layer, set()


# # find_paths("out")
# find_paths()
_, dac, fft = ways["svr"]

print(min(dac, fft))
