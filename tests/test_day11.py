from aoc.runner import load_data
from aoc.solutions.day11 import part1, part2


def test_part1_solution_is_correct():
    """Check output against known solution"""

    data = load_data(11)

    output = part1(data)

    assert output == 117624


def test_part2_solution_is_correct():
    """Check output against known solution"""

    data = load_data(11)

    output = part2(data)

    assert output == 16792940265
