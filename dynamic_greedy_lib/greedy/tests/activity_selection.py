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

# Empty lists
runner.expect_equal([[], []], "Empty lists are not accepted")

# Empty start list
runner.expect_equal([[], [5, 9, 12, 13, 16, 45]], "Empty lists are not accepted")
runner.expect_equal([[], [5, 9, 12, 13, 16, 45, 33, 80, 21, 45]], "Empty lists are not accepted")

# Empty finish list
runner.expect_equal([[1, 8, 3, 0, 9, 7, 8, 5, 2, 7, 13], []], "Empty lists are not accepted")
runner.expect_equal([[1, 3, 0, 5, 8, 5], []], "Empty lists are not accepted")

# Start list bigger than finish list
runner.expect_equal([[1, 8, 3, 0, 9, 7, 8, 5, 2, 7, 13], [24, 12, 10, 8]], -1)
runner.expect_equal([[1, 2, 3, 0, 7, 8, 5], [12, 13, 16, 45]], -1)

# Finish list bigger than start list
runner.expect_equal([[1, 2, 3, 0, 7, 8, 5], [5, 9, 12, 13, 16, 45, 33, 80, 21, 45]], -1)
runner.expect_equal([[6], [12, 13, 16, 45]], -1)

# The below tests can be verified on http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/  #- [Run on IDE]
runner.expect_equal([[1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]]
                    ,
                    [0, 1, 3, 4]
)
runner.expect_equal([[1, 2, 3, 0, 7, 8, 5], [2, 3, 4, 6, 8, 9, 9]]
                    ,
                    [0, 1, 2, 4, 5]
)
runner.expect_equal([[1, 8, 3, 0, 9, 7, 8, 5, 2, 7, 13], [2, 3, 4, 6, 7, 8, 9, 9, 10, 15, 17]]
                    ,
                    [0, 1, 2, 4, 5, 6, 10]
)
runner.expect_equal([[1, 8, 3, 0, 9, 7, 8, 5, 2, 7, 13, 4, 78, 36, 55, 36], [2, 3, 4, 6, 7, 8, 9, 9, 10, 15, 17, 23, 24, 26, 33, 35]]
                    ,
                    [0, 1, 2, 4, 5, 6, 10, 12, 13, 14, 15]
)
