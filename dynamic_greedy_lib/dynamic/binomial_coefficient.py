from utils import table as table_utils

"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python binomial_coefficient.py

    Resources:
        https://github.com/jcarva/algorithms/blob/dynamic-programming/binomial-coefficient.js
        http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/
        https://en.wikipedia.org/wiki/Binomial_coefficient

    Description:
        A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that
        k objects can be chosen from among n objects; more formally, the number of k-element subsets
        (or k-combinations) of an n-element set.

    Complexity: O(n*k)

    Applications:
        Some modeling chemical systems and solving by numerical approaches uses binomial coefficient
        to generate central difference equations to odd-ordered partial differentials in a single-step
        operation. All finite difference equations to partial differentials shown herein display finite
        series of palindromic coefficients with alternating signs.
"""

def solve(input):
    """
    :param input:   array that contains two non negatives integers, where the second value should be
                    less or equal to the first.
                                ex: [50, 3]

    :return:        integer that represents the calculated binomial coefficient.
                                ex: 19600
    """
    return _binomial_coefficient(input[0], input[1])


def _binomial_coefficient(n, k):
    if (n >= k) and (k >= 0):

        # Create a table to store values that are used to solve shortest problems
        c = table_utils.initialize(1, k + 1, 0)[0]

        # Set the first position with 1
        c[0] = 1

        for i in range(1, n+1):

            # Calculate the current row of pascal triangle using the previous column
            j = min(i, k)
            while j > 0:
                c[j] = c[j] + c[j-1]
                j -= 1

        return c[k]

    else:
        return -1
