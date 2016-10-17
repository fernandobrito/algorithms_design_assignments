from utils.tests import TestRunner
from dynamic import longst_comn_subseq

"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python longst_comn_subseq.py
"""

runner = TestRunner(longst_comn_subseq.solve)

# Resource: https://www.youtube.com/watch?v=cfCdtJSu5pc
runner.expect_equal(["ABCF", "ACF"], 3)

# Resource: http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
runner.expect_equal(["ABCDGH", "AEDFHR"], 3)
runner.expect_equal(["AGGTAB", "GXTXAYB"], 4)

# Resource: https://www.youtube.com/watch?v=aSwu8Z9nzOg
runner.expect_equal(["ABCB", "BDCAB"], 3)

