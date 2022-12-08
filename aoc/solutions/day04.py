def part1(data):

    pairs = [tuple(p.split(",")) for p in data.rstrip("\n").split("\n")]

    sections = [
        [
            set(range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1)),
            set(range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1)),
        ]
        for elf1, elf2 in pairs
    ]

    # count how many pairs have full overlap
    full_overlap = [
        any([elf1.issubset(elf2), elf2.issubset(elf1)]) for elf1, elf2 in sections
    ]
    num_with_full_overlap = sum(full_overlap)

    return num_with_full_overlap


def part2(data):

    pairs = [tuple(p.split(",")) for p in data.rstrip("\n").split("\n")]

    sections = [
        [
            set(range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1)),
            set(range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1)),
        ]
        for elf1, elf2 in pairs
    ]

    # count how many pairs have some overlap
    overlap = [len(set.intersection(elf1, elf2)) for elf1, elf2 in sections]
    num_with_overlap = len(overlap) - overlap.count(0)

    return num_with_overlap
