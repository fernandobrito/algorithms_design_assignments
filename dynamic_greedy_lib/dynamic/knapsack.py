from utils import table as table_utils

"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python knapsack.py
    Resources:
        http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
        https://dzone.com/articles/algorithm-week-python-vs-ruby
        https://en.wikipedia.org/wiki/Knapsack_problem
        http://cse.unl.edu/~goddard/Courses/CSCE310J/Lectures/Lecture8-DynamicProgramming.pdf
        http://www.grokit.ca/cnt/KnapsackProblem/

    Description:
        Given weights and values of n items, put these items in a knapsack of capacity W
        to get the maximum total value in the knapsack.

    Complexity: O(nW)
        Where n is the number of items and W is the capacity of knapsack.

    Applications:
        The spaceships which they will be taking to mars for human settlement there would
        use similar algorithm to maximize the values of goods which they want to carry.
"""


def solve(input):
    """
    :param input:   array with first element: total capacity of the knapsack, second element: weight
                    list (should be non-empty) and third element: value list (should be non-empty).
                                ex: [15, [10, 20, 30], [60, 100, 120]]

    :return:        integer that represents maximum value that can be put in a backpack of the given capacity.
                                ex: 60
    """
    return _knapsack(input[0], input[1], input[2])


# val = values list
# wt = weight list
# W = total capacity
def _knapsack(W, wt, val):

    # Get numbers of rows on the table
    n = len(val)

    # Create a table to store values that are used to solve shortest problems
    k = table_utils.initialize(n + 1, W + 1, 0)

    # Iterate over all rows
    for i in range(n + 1):

        # Iterate over all columns
        j = 1
        while j < (W + 1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif wt[i - 1] <= j:
                k[i][j] = max(val[i - 1] + k[i - 1][j - wt[i - 1]], k[i - 1][j])
            else:
                k[i][j] = k[i - 1][j]

            j += 1

    return k[n][W]
