class Crates:
    """Class to store crate configurations with methods to move
    crates between stacks"""

    def __init__(self, positions):
        self.positions = positions

    def move_single_crate(self, stack_start, stack_end):

        crate = self.positions[stack_start].pop()

        self.positions[stack_end].append(crate)

        return

    def move_multiple_crates(self, num_crates, stack_start, stack_end):

        crates = self.positions[stack_start][-num_crates:]

        self.positions[stack_start] = self.positions[stack_start][:-num_crates]

        self.positions[stack_end].extend(crates)

        return


def part1(data):

    # Get crate positions
    crates = data.rstrip("\n").split("\n\n")[0].split("\n")
    crates.reverse()
    # Get indices for crate contents
    crate_idx = [i for i in range(len(crates[0])) if crates[0][i] != " "]
    crate_ids = [crates[0][i] for i in crate_idx]
    # Keep only the crate contents
    crates = [[row[i] for i in crate_idx] for row in crates[1:]]
    # Transpose list of lists
    crates = list(map(list, zip(*crates)))
    # Store crate contents in dict
    crate_positions = dict.fromkeys(crate_ids)
    for i, id in enumerate(crate_ids):
        crate_positions[id] = [c for c in crates[i] if c != " "]
    # Create crates object for transformation
    crates = Crates(crate_positions)

    # Format moves to store number of moves, starting crate and end crate
    moves = data.rstrip("\n").split("\n\n")[1].split("\n")
    moves = [
        m.replace("move ", "")
        .replace("from ", "")
        .replace("to ", "")
        .split(" ")  # noqa
        for m in moves
    ]

    # Perform each move in sequence
    for m in moves:
        num_moves = int(m[0])
        while num_moves > 0:
            crates.move_single_crate(m[1], m[2])
            num_moves += -1

    return "".join([v[-1] for k, v in crates.positions.items()])


def part2(data):

    # Get crate positions
    crates = data.rstrip("\n").split("\n\n")[0].split("\n")
    crates.reverse()
    # Get indices for crate contents
    crate_idx = [i for i in range(len(crates[0])) if crates[0][i] != " "]
    crate_ids = [crates[0][i] for i in crate_idx]
    # Keep only the crate contents
    crates = [[row[i] for i in crate_idx] for row in crates[1:]]
    # Transpose list of lists
    crates = list(map(list, zip(*crates)))
    # Store crate contents in dict
    crate_positions = dict.fromkeys(crate_ids)
    for i, id in enumerate(crate_ids):
        crate_positions[id] = [c for c in crates[i] if c != " "]
    # Create crates object for transformation
    crates = Crates(crate_positions)

    # Format moves to store number of moves, starting crate and end crate
    moves = data.rstrip("\n").split("\n\n")[1].split("\n")
    moves = [
        m.replace("move ", "")
        .replace("from ", "")
        .replace("to ", "")
        .split(" ")  # noqa
        for m in moves
    ]

    # Perform each move in sequence
    for m in moves:
        crates.move_multiple_crates(int(m[0]), m[1], m[2])

    return "".join([v[-1] for k, v in crates.positions.items()])
