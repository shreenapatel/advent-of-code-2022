from aoc.runner import load_data
from aoc.solutions.day04 import part1, part2


def test_part1_solution_is_correct():
    """Check output against known solution"""

    data = load_data(4)

    output = part1(data)

    assert output == 524


def test_part2_solution_is_correct():
    """Check output against known solution"""

    data = load_data(4)

    output = part2(data)

    assert output == 798
