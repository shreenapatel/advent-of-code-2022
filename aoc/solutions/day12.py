import numpy as np
from math import floor


def grid_to_node(x, y, num_cols):
    node = x * num_cols + y % (num_cols + 1)
    return node


def node_to_xy(node, num_cols):
    y = node % num_cols
    x = floor(node / num_cols)
    return x, y


def convert_letter_to_altitude(letter):
    if letter == "S":
        altitude = 1
    elif letter == "E":
        altitude = 26
    else:
        altitude = ord(letter) - 96
    return altitude


def get_neighbours_for_node(node, heightmap):

    num_rows, num_cols = heightmap.shape

    i, j = node_to_xy(node, num_cols)

    curr_altitude = convert_letter_to_altitude(heightmap[i, j])

    neighbour_idx = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
    neighbour_idx = [
        (x, y)
        for x, y in neighbour_idx
        if x >= 0 and x <= (num_rows - 1) and y >= 0 and y <= (num_cols - 1)
    ]

    return {
        grid_to_node(x, y, num_cols)
        for x, y in neighbour_idx
        if convert_letter_to_altitude(heightmap[x, y]) <= (1 + curr_altitude)
    }


def bfs(neighbours, start_node, end_node):

    queue = [start_node]
    distances = {start_node: 0}

    while queue:

        curr_node = queue.pop(0)

        if curr_node == end_node:
            break

        unvisited_neighbours = [n for n in neighbours[curr_node] if n not in distances]
        queue.extend(unvisited_neighbours)
        distances.update({n: distances[curr_node] + 1 for n in unvisited_neighbours})

    return distances


def part1(data):

    # Load data
    heightmap = [list(row) for row in data.rstrip("\n").split("\n")]
    heightmap = np.array(heightmap)
    num_rows, num_cols = heightmap.shape
    nodes = range(num_rows * num_cols)

    # Get nodes for starting and end points
    start_x = np.where(heightmap == "S")[0][0]
    start_y = np.where(heightmap == "S")[1][0]
    start_node = grid_to_node(start_x, start_y, num_cols)
    end_x = np.where(heightmap == "E")[0][0]
    end_y = np.where(heightmap == "E")[1][0]
    end_node = grid_to_node(end_x, end_y, num_cols)

    # Find neighbours for every node
    neighbours = {node: get_neighbours_for_node(node, heightmap) for node in nodes}

    # Run BFS algorithm
    path_sizes = bfs(neighbours, start_node, end_node)

    return path_sizes[end_node]


def part2(data):

    # Load data
    heightmap = [list(row) for row in data.rstrip("\n").split("\n")]
    heightmap = np.array(heightmap)
    num_rows, num_cols = heightmap.shape
    nodes = range(num_rows * num_cols)

    # Get nodes for starting and end points
    start_x = np.where((heightmap == "S") | (heightmap == "a"))[0]
    start_y = np.where((heightmap == "S") | (heightmap == "a"))[1]
    starting_nodes = [grid_to_node(x, y, num_cols) for x, y in zip(start_x, start_y)]

    end_x = np.where(heightmap == "E")[0][0]
    end_y = np.where(heightmap == "E")[1][0]
    end_node = grid_to_node(end_x, end_y, num_cols)

    # Find neighbours for every node
    neighbours = {node: get_neighbours_for_node(node, heightmap) for node in nodes}

    # Run BFS algorithm from multiple starting points
    min_path_size = num_rows * num_cols
    for start_node in starting_nodes:

        path_sizes = bfs(neighbours, start_node, end_node)

        if end_node not in path_sizes:
            continue

        if path_sizes[end_node] < min_path_size:
            min_path_size = path_sizes[end_node]

    return min_path_size
