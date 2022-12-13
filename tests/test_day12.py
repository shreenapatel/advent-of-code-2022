from aoc.runner import load_data
from aoc.solutions.day12 import part1, part2  # noqa


def test_part1_solution_is_correct():
    """Check output against known solution"""

    data = load_data(12)

    output = part1(data)

    assert output == 437


def test_part2_solution_is_correct():
    """Check output against known solution"""

    data = load_data(12)

    output = part2(data)

    assert output == 430
