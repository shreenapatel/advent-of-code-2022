import numpy as np


def part1(data):

    trees = [[int(x) for x in list(line)] for line in data.rstrip("\n").split("\n")]
    trees = np.array(trees)

    N = trees.shape[0]
    num_visible = 4 * N - 4  # trees on border are always visible

    # Grid search through trees to check if they are blocked by any
    # taller trees in each of the 4 directions
    for i in range(N):

        for j in range(N):
            # ignore trees on the border as these are already counted
            if i == 0 or i == (N - 1) or j == 0 or j == (N - 1):
                continue

            curr_tree_height = trees[i, j]

            # check trees to left
            if sum(trees[i, :j] >= curr_tree_height) == 0:
                num_visible += 1
                continue

            # check trees on right
            if sum(trees[i, (j + 1) :] >= curr_tree_height) == 0:
                num_visible += 1
                continue

            # check trees above
            if sum(trees[:i, j] >= curr_tree_height) == 0:
                num_visible += 1
                continue

            # check trees below
            if sum(trees[(i + 1) :, j] >= curr_tree_height) == 0:
                num_visible += 1

    return num_visible


def count_visible_trees(current_tree, other_trees, reverse=False):

    sorted_trees = list(other_trees)

    # if checking trees to left or above, need to reverse order
    if reverse:
        sorted_trees.reverse()

    # count number of trees until we reach a tree with the same or taller
    # height, or until we reach the border
    num_visible_trees = next(
        (k + 1 for k, v in enumerate(sorted_trees) if v >= current_tree),
        len(sorted_trees),  # reach border
    )

    return num_visible_trees


def part2(data):

    trees = [[int(x) for x in list(line)] for line in data.rstrip("\n").split("\n")]
    trees = np.array(trees)

    N = trees.shape[0]
    max_score = 0

    # Grid search to calculate each tree's scenic_score (product of the number of
    # visible trees in each of the 4 directions)
    for i in range(N):

        for j in range(N):
            # trees on the border will get a score of zero
            if i == 0 or i == (N - 1) or j == 0 or j == (N - 1):
                continue

            curr_tree_height = trees[i, j]

            left_score = count_visible_trees(curr_tree_height, trees[i, :j], True)
            right_score = count_visible_trees(curr_tree_height, trees[i, (j + 1) :])
            up_score = count_visible_trees(curr_tree_height, trees[:i, j], True)
            down_score = count_visible_trees(curr_tree_height, trees[(i + 1) :, j])

            curr_score = left_score * right_score * up_score * down_score

            if curr_score > max_score:
                max_score = curr_score

    return max_score
