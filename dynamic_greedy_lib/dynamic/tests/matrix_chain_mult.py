from utils.tests import TestRunner
from dynamic import matrix_chain_mult

"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python matrix_chain_mult.py
"""

runner = TestRunner(matrix_chain_mult.solve)

# Resource: http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
runner.expect_equal([1, 2, 3, 4], 18)

# Resource: http://www.columbia.edu/~cs2035/courses/csor4231.F11/matrix-chain.pdf
runner.expect_equal([10, 100, 5, 50, 1], 1750)

