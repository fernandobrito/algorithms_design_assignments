from utils.tests import TestRunner
from greedy import activity_selection
"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python activity_selection.py
    Resources:
        https://github.com/jcarva/algorithms/blob/dynamic-programming/binomial-coefficient-test.js
"""

runner = TestRunner(activity_selection.solve)

runner.expect_equal([[1], [1]], [0, 1, 3, 4])
