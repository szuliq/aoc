from collections import defaultdict

lines = []


def draw(lines, beams):
    for i, row in enumerate(beams):
        line = lines[i]
        for beam in row:
            line[beam] = "|"

    for line in lines:
        print("".join(line))


with open("7.txt", "r") as file:
    for line in file.readlines():
        lines.append([char for char in line.strip()])

beams = [{}, {lines[0].index("S"): 1}]

for i, row in enumerate(lines[2:], start=2):
    prev_beams = beams[i - 1]
    new_beams = defaultdict(int)

    for beam, count in prev_beams.items():
        if row[beam] == "^":
            new_beams[beam - 1] += count
            new_beams[beam + 1] += count
        else:
            new_beams[beam] += count

    beams.append(new_beams)

draw(lines, beams)

print(sum(beams[-1].values()))
