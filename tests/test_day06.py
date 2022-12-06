from aoc.runner import load_data
from aoc.solutions.day06 import part1, part2  # noqa


def test_part1_solution_is_correct():
    """Check output against known solution"""

    data = load_data(6)

    output = part1(data)

    assert output == 1723


def test_part2_solution_is_correct():
    """Check output against known solution"""

    data = load_data(6)

    output = part2(data)

    assert output == 3708
