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

    Complexity:

    Application:
"""


def solve(input):
    """
    Input : should contain a values list, a weight list and the total capacity.
    Output : maximum value that can be put in a backpack of the given capacity.
    """
    return _knapsack(input[0], input[1], input[2])


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
