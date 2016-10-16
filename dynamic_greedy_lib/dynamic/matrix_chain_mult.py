import sys
from utils import table as table_utils

def solve(input):
    """
    :param input: Array containing the matrizes dimensions.
    :return: The minimum number of multiplications.
    """

    return _matrix_chain_mult(input)

def _matrix_chain_mult(dims):
    num = len(dims)

    table = table_utils.initialize(num, num, 0)

    for c_len in range(2, num):
        for i in range(1, num - c_len + 1):
            j = i + c_len - 1
            table[i][j] = sys.maxsize
            for k in range(i, j):
                mult = table[i][k] + table[k + 1][j] + dims[i - 1] * dims[j] * dims[k]
                table[i][j] = mult if mult < table[i][j] else table[i][j]

    return table[1][num - 1]
