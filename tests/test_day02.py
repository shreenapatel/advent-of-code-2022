from aoc.runner import load_data
from aoc.solutions.day02 import part1, part2


def test_part1_solution_is_correct():
    """Check output against known solution"""

    data = load_data(2)

    output = part1(data)

    assert output == 15572


def test_part2_solution_is_correct():
    """Check output against known solution"""

    data = load_data(2)

    output = part2(data)

    assert output == 16098
