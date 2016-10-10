from utils.tests import TestRunner
from dynamic import knapsack

"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python knapsack.py
    Resources:
        https://github.com/jcarva/algorithms/blob/dynamic-programming/binomial-coefficient-test.js
"""

runner = TestRunner(knapsack.solve)


runner.expect_equal([15, [10, 20, 30], [60, 100, 120]], 60)
runner.expect_equal([98, [2, 5, 10, 15, 30], [25, 30, 90]], 145)
runner.expect_equal([50, [10, 20, 30], [60, 100, 120]], 220)
runner.expect_equal([25, [5, 10, 15, 30], [60, 100, 180]], 280)