from aoc.runner import load_data
from aoc.solutions.day{{day_str}} import part1, part2 # noqa


def test_part1_solution_is_correct():
    """Check output against known solution"""

    data = load_data({{day}})

    output = part1(data)

    assert output == None


def test_part2_solution_is_correct():
    """Check output against known solution"""

    data = load_data({{day}})

    output = part2(data)

    assert output == None
