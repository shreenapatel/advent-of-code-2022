def part1(data):

    rounds = [tuple(x.split(" ")) for x in data.rstrip("\n").split("\n")]

    win_combos = [("A", "Y"), ("B", "Z"), ("C", "X")]
    draw_combos = [("A", "X"), ("B", "Y"), ("C", "Z")]

    draws = [r for r in rounds if r in draw_combos]
    wins = [r for r in rounds if r in win_combos]

    moves = [r[1] for r in rounds]

    score = (
        moves.count("X")
        + 2 * moves.count("Y")
        + 3 * moves.count("Z")
        + 3 * len(draws)
        + 6 * len(wins)
    )

    return score


def part2(data):

    rounds = [tuple(x.split(" ")) for x in data.rstrip("\n").split("\n")]

    rock_pairs = [("A", "Y"), ("B", "X"), ("C", "Z")]
    paper_pairs = [("A", "Z"), ("B", "Y"), ("C", "X")]
    scissor_pairs = [("A", "X"), ("B", "Z"), ("C", "Y")]

    rock_moves = [r for r in rounds if r in rock_pairs]
    paper_moves = [r for r in rounds if r in paper_pairs]
    scissor_moves = [r for r in rounds if r in scissor_pairs]

    outcomes = [r[1] for r in rounds]

    score = (
        len(rock_moves)
        + 2 * len(paper_moves)
        + 3 * len(scissor_moves)
        + 3 * outcomes.count("Y")
        + 6 * outcomes.count("Z")
    )

    return score
