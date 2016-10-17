"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python longst_comn_subseq.py

    Resources:
        http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
        https://www.youtube.com/watch?v=aSwu8Z9nzOg
        https://www.youtube.com/watch?v=cfCdtJSu5pc

    Description:
        "The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a 
        set of sequences (often just two sequences). It differs from problems of finding common substrings: unlike substrings, subsequences 
        are not required to occupy consecutive positions within the original sequences. The longest common subsequence problem is a classic 
        computer science problem, the basis of data comparison programs such as the diff utility, and has applications in bioinformatics. 
        It is also widely used by revision control systems such as Git for reconciling multiple changes made to a revision-controlled 
        collection of files." [Wikipedia]

    Complexity: O(m*n)
        Where m is the length of first string and n is the length of second string

    Applications:
        ""
"""

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
