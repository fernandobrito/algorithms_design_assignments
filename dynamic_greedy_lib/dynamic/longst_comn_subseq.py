from utils import table as table_utils

def solve(input):
    """
    :param input: array with two strings
    :return: length of longest common subsequence of the two strings
    """

    return _longest_common_subsequence(input[0], input[1])

def _longest_common_subsequence(seq, sub):
    seq_len = len(seq) + 1
    sub_len = len(sub) + 1

    table = table_utils.initialize(seq_len, sub_len, 0)

    for r in range(1, seq_len):
        r_bk = r - 1

        for c in range(1, sub_len):
            c_bk = c - 1

            if(seq[r_bk] == sub[c_bk]):
                table[r][c] = table[r_bk][c_bk] + 1
            else:
                r_val = table[r_bk][c]
                c_val = table[r][c_bk]
                table[r][c] = r_val if r_val > c_val else c_val

    return table[seq_len - 1][sub_len - 1]
