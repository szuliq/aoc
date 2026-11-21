import itertools

sum = 0


def parse_button(button_str):
    parts = button_str[1:-1].split(",")
    return list(map(int, parts))


def flip(button, state):
    return tuple(not x if i in button else x for i, x in enumerate(state))


def find_desired_state(desired_state, buttons):
    # import pdb

    # pdb.set_trace()

    for i in range(1, 100):
        for combination in itertools.product(buttons, repeat=i):
            state = (False,) * len(desired_state)

            # seen_states = {state}

            combination = list(combination)

            for button in combination:
                state = flip(button, state)

            # if state in seen_states:
            #     continue

            # print(combination, state)

            if state == desired_state:
                return i

            # seen_states.add(state)


with open("10.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        print(f"Line {i+1}")

        desired_state, *buttons, _ = line.strip().split()

        desired_state = tuple(x == "#" for x in desired_state[1:-1])
        buttons = [parse_button(button) for button in buttons]

        sum += find_desired_state(desired_state, buttons)


print(sum)
