from utils.tests import TestRunner
from dynamic import subset_sum_problem

"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python subset_sum_problem.py
"""
runner = TestRunner(subset_sum_problem.solve)

# Resource: https://www.youtube.com/watch?v=5td2QH-x5ck
runner.expect_equal([[1, 3, 9, 2], 5], True)

# Resource: https://www.youtube.com/watch?v=tfN2bFx9VRI
runner.expect_equal([[4, 2, 1, 3], 5], True)

# Resource: http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/ 
runner.expect_equal([[3, 34, 4, 12, 5, 2], 9], True)

# False 
runner.expect_equal([[3, 34, 4, 12, 5], 10], False)
