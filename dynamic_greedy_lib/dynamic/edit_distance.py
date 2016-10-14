from utils import table as table_utils

"""
Given two strings str1 and str2 and 3 operations (insert, remove and replace)
that can performed on str1, find minimum number of edits (operations)
required to convert ‘str1′ into ‘str2′. Also known as Levenshtein distance.

Applications:
    "Wide range of applications, for instance, spell checkers, correction
     systems for optical character recognition, and software to assist
    natural language translation based on translation memory." [Wikipedia]

Complexity: O(m * n)
    O(1) in all positions on table of size m * n, where m and n
    are lengths of strings.

Author: Fernando Brito (11111309)

Resources:
    - http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
"""

def solve(input):
    """
    Input should contain two strings
    Output edit distance as an integer
    """
    return _edit_distance(input[0], input[1], len(input[0]), len(input[1]))


def _edit_distance(str1, str2, m, n):
    """
    Calculate the edit distance between two strings using dynamic programming
    """

    # Initialize table to store solution of sub problems
    # with length1 + 1 rows and length2 + 1 columns
    table = table_utils.initialize(m+1, n+1)

    _fill_table(table, str1, str2, m, n)

    return table[m][n]


def _fill_table(table, str1, str2, m, n):
    """
    Fill the table, column-wise, starting from (0, 0)
    """

    # Iterate over all rows
    for row in range(m + 1):

        # Iterate over all columns
        for column in range(n + 1):

            # When one string is empty, we consider its cost
            # as inserting all elements from the other string
            if row == 0:
                table[row][column] = column
            elif column == 0:
                table[row][column] = row

            # If last chars from both strings are equal,
            # nothing is added to the cost, and cost is equal
            # to comparing both substrings with -1 length
            elif str1[row - 1] == str2[column - 1]:
                table[row][column] = table[row - 1][column - 1]

            # If last chars are different, add one to the cost of
            # the optimal (minimum) subsolution either adding, removing
            # or replacing char
            else:
                table[row][column] = 1 + min([table[row][column - 1], table[row - 1][column],
                                      table[row - 1][column - 1]])