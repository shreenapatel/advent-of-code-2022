from aoc.runner import load_data
from aoc.solutions.day10 import part1, part2


def test_part1_solution_is_correct():
    """Check output against known solution"""

    data = load_data(10)

    output = part1(data)

    assert output == 15680


def test_part2_solution_is_correct():
    """Check output against known solution"""

    data = load_data(10)

    output = part2(data)

    expected_output = "####.####.###..####.#..#..##..#..#.###..\n"
    expected_output += "...#.#....#..#.#....#..#.#..#.#..#.#..#.\n"
    expected_output += "..#..###..###..###..####.#....#..#.#..#.\n"
    expected_output += ".#...#....#..#.#....#..#.#.##.#..#.###..\n"
    expected_output += "#....#....#..#.#....#..#.#..#.#..#.#....\n"
    expected_output += "####.#....###..#....#..#..###..##..#....\n"
    assert output == expected_output
