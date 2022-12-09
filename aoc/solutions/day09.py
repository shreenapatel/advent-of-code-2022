def move_position(curr_position, direction):
    """
    Get new position after moving 1 step in provided direction
    """
    new_position = curr_position[:]

    if direction == "U":
        new_position[1] = curr_position[1] + 1
    elif direction == "D":
        new_position[1] = curr_position[1] - 1
    elif direction == "R":
        new_position[0] = curr_position[0] + 1
    else:
        new_position[0] = curr_position[0] - 1

    return new_position


def get_move_direction(x_gap, y_gap):
    """
    Find out which direction to move in based on difference
    in x and y positions
    """

    if y_gap > 1 and x_gap == 0:
        direction = ["U"]
    elif y_gap < -1 and x_gap == 0:
        direction = ["D"]
    elif x_gap > 1 and y_gap == 0:
        direction = ["R"]
    elif x_gap < -1 and y_gap == 0:
        direction = ["L"]
    elif (y_gap >= 1 and x_gap > 1) or (x_gap >= 1 and y_gap > 1):
        direction = ["U", "R"]
    elif (y_gap >= 1 and x_gap < -1) or (x_gap <= -1 and y_gap > 1):
        direction = ["U", "L"]
    elif (y_gap <= -1 and x_gap > 1) or (x_gap >= 1 and y_gap < -1):
        direction = ["D", "R"]
    elif (y_gap <= -1 and x_gap < -1) or (x_gap <= -1 and y_gap < -1):
        direction = ["D", "L"]
    else:
        direction = []

    return direction


def part1(data):

    moves = [tuple(line.split(" ")) for line in data.rstrip("\n").split("\n")]

    head = [0, 0]
    tail = [0, 0]
    tail_history = [tail]

    for m in moves:

        for _ in range(int(m[1])):

            # Move head
            head = move_position(head, m[0])

            # Move tail based on position relative to head
            y_gap = head[1] - tail[1]
            x_gap = head[0] - tail[0]

            directions = get_move_direction(x_gap, y_gap)

            for d in directions:
                tail = move_position(tail, d)

            tail_history.append(tail)

    # convert to tuple to get unique items in list of list
    return len(set([tuple(x) for x in tail_history]))


def part2(data):

    moves = [tuple(line.split(" ")) for line in data.rstrip("\n").split("\n")]

    num_knots = 10
    knots = [[0, 0]] * num_knots
    tail_history = [knots[-1]]

    for m in moves:

        for _ in range(int(m[1])):

            # Move head
            knots[0] = move_position(knots[0], m[0])

            # Update each knot position based on position of previous knot
            for knot_id in range(1, num_knots):

                y_gap = knots[knot_id - 1][1] - knots[knot_id][1]
                x_gap = knots[knot_id - 1][0] - knots[knot_id][0]

                directions = get_move_direction(x_gap, y_gap)

                for d in directions:
                    knots[knot_id] = move_position(knots[knot_id], d)

                tail_history.append(knots[-1])

    # convert to tuple to get unique items in list of list
    return len(set([tuple(x) for x in tail_history]))
