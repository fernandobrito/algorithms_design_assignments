from utils.tests import TestRunner
from greedy import fractional_knapsack
"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python fractional_knapsack.py
    Resources:
        http://www.geeksforgeeks.org/fractional-knapsack-problem/
"""

runner = TestRunner(fractional_knapsack.solve)

# knapsack with capacity 50 and 3 items types
runner.expect_equal(
    [50, [[60, 10], [100, 20], [120, 30]]], 240.0
)

