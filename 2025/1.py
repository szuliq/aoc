position = 50
on_zero = 0

with open("1.txt", "r") as file:
    for line in file.readlines():
        change = 0
        steps = int(line[1:])

        if line.startswith("L"):
            steps *= -1

            if position == 0:
                change -= 1

        new_position = position + steps
        change += abs(new_position // 100)
        new_position %= 100

        if new_position == 0 and steps % 100 != 0 and steps < 0:
            change += 1

        print(position, steps, new_position, change)

        on_zero += change
        position = new_position


print(on_zero)
