"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python subset_sum_problem.py

    Resources:
        http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
        https://www.youtube.com/watch?v=tfN2bFx9VRI
        https://www.youtube.com/watch?v=5td2QH-x5ck

    Description:
        "In computer science, the subset sum problem is an important problem in complexity theory and cryptography. The problem is 
         this: given a set (or multiset) of integers, is there a non-empty subset whose sum is zero? For example, 
         given the set {−7, −3, −2, 5, 8}, the answer is yes because the subset {−3, −2, 5} sums to zero. The problem is NP-complete. An equivalent 
         problem is this: given a set of integers and an integer s, does any non-empty subset sum to s? Subset sum can also be thought of as a 
         special case of the knapsack problem. One interesting special case of subset sum is the partition problem, in which s is half of the 
         sum of all elements in the set." [Wikipedia]

    Complexity: O(sum*n)
        Where n is the number of elements

"""

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
