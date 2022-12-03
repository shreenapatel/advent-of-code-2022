def part1(data):

    rsacks = data.rstrip("\n").split("\n")
    compartment_size = [int(len(r) / 2) for r in rsacks]
    items = [
        set.intersection(set(r[:i]), set(r[i:])).pop()
        for r, i in zip(rsacks, compartment_size)
    ]
    scores = [item.isupper() * 26 + ord(item.lower()) - 96 for item in items]

    return sum(scores)


def part2(data):

    rsacks = [set(r) for r in data.rstrip("\n").split("\n")]

    badges = [
        set.intersection(rsacks[i], rsacks[i + 1], rsacks[i + 2]).pop()
        for i in range(0, len(rsacks), 3)
    ]
    scores = [b.isupper() * 26 + ord(b.lower()) - 96 for b in badges]

    return sum(scores)
