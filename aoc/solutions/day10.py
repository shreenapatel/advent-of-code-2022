def part1(data):

    program = [
        tuple(x.split(" "))
        for x in data.replace("noop\n", "noop 0\n").rstrip("\n").split("\n")
    ]
    program = [(int(cycle == "addx") + 1, int(signal)) for cycle, signal in program]

    cycle_hist = []
    register = []
    cycle, X = 0, 1
    for num_cycles, signal in program:
        cycle += num_cycles
        X += signal
        register.append(X)
        cycle_hist.append(cycle)

    check_points = [20, 60, 100, 140, 180, 220]
    total_signal_strength = 0

    for chk in check_points:

        id = next((k - 1 for k, v in enumerate(cycle_hist) if v > chk))

        if cycle_hist[id] == chk:
            id += -1

        total_signal_strength += chk * register[id]

    return total_signal_strength


def part2(data):

    program = [
        tuple(x.split(" "))
        for x in data.replace("noop\n", "noop 0\n").rstrip("\n").split("\n")
    ]
    program = [(int(cycle == "addx") + 1, int(signal)) for cycle, signal in program]

    screen_width = 40
    cycle = 0
    sprite = [0, 1, 2]
    output = ""

    for num_cycles, signal in program:
        for _ in range(num_cycles):
            cycle += 1
            cursor = (cycle - 1) % screen_width

            if cursor in sprite:
                output += "#"
            else:
                output += "."
            if cursor == (screen_width - 1):
                output += "\n"

        sprite = [x + signal for x in sprite]

    return output
