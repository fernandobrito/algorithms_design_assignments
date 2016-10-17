from utils.tests import TestRunner
from greedy import fractional_knapsack
"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python fractional_knapsack.py
"""

runner = TestRunner(fractional_knapsack.solve)

# knapsack with capacity 50 and 3 items types
# Resource: http://www.geeksforgeeks.org/fractional-knapsack-problem/
runner.expect_equal([50, [[60, 10], [100, 20], [120, 30]]], 240.0)

# knapsack with capacity 6 and 5 items types
# Resource: https://www.youtube.com/watch?v=c2Ush3m_sfc
runner.expect_equal([6, [[25, 3], [20, 2], [15, 1], [40, 4], [50, 5]]], 65.0)

# knapsack with capacity 23 and 4 items types
# Resource: https://www.youtube.com/watch?v=kFUs5VUxO-s
runner.expect_equal([23, [[10, 20], [5, 5], [5, 15], [15, 5]]], 26.5)
