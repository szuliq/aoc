lines = []
splits = 0


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

beams = [set(), set([lines[0].index("S")])]

for i, row in enumerate(lines[2:], start=2):
    prev_beams = beams[i - 1]
    new_beams = set()

    for beam in prev_beams:
        if row[beam] == "^":
            splits += 1
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
        else:
            new_beams.add(beam)

    print(i, prev_beams, new_beams, row)

    beams.append(new_beams)

draw(lines, beams)

print(splits)
