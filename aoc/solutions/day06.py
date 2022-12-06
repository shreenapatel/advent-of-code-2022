def part1(data):

    data = data.rstrip("/n")

    i = 0
    while len(set(data[i : (i + 4)])) < 4:  # noqa
        i += 1

    return i + 4


def part2(data):

    data = data.rstrip("/n")

    i = 0
    while len(set(data[i : (i + 14)])) < 14:  # noqa
        i += 1

    return i + 14
