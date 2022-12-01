def part1(data):

    elf_totals = [
        sum([int(x) for x in cals.lstrip("\n").rstrip("\n").split("\n")])
        for cals in data.split("\n\n")
    ]

    return max(elf_totals)


def part2(data):

    elf_totals = [
        sum([int(x) for x in cals.lstrip("\n").rstrip("\n").split("\n")])
        for cals in data.split("\n\n")
    ]
    elf_totals.sort()

    return sum(elf_totals[-3:])
