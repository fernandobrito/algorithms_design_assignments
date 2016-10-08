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
    """
    Set numbers of interactions.
    """
    n = len(val)

    """
    Create a table to store values that are used to solve shortest problems.
    """
    column = [0] * (W + 1)
    k = list(column)

    for i in range(1, n):
        cache = list(k)
        k = list(column)

        j = 1
        while j < (W + 1):
            if wt[i] > j:
                k[j] = cache[j]
            else:
                k[j] = max(cache[j], val[i] + cache[j - wt[i]])
            j += 1

    return k[W]