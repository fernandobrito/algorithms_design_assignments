from utils import table as table_utils

def solve(input):
    """
    :param input: Array containing a subset in the position 0 and a sum value in the position 1.
    :return: True if the subset contains a sum of the requested value.
    """

    return _subset_sum_problem(input[0], input[1])

def _subset_sum_problem(subset, sum):
    rows = len(subset) + 1
    cols = sum + 1

    table = table_utils.initialize(rows, cols , False)
    table[0][0] = True

    for r in range(1, rows):
        table[r][0] = True

        for c in range(1, cols):
            if table[r - 1][c] or (c - subset[r - 1]) < 0:
                table[r][c] = table[r - 1][c]
            else:
                table[r][c] = table[r - 1][c - subset[r - 1]]

    return table[rows - 1][cols - 1]
