from utils.tests import TestRunner
from dynamic import binomial_coefficient

"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python binomial_coefficient.py
    Resources:
        https://github.com/jcarva/algorithms/blob/dynamic-programming/binomial-coefficient-test.js
"""

runner = TestRunner(binomial_coefficient.solve)

# Verified using http://www.ohrt.com/odds/binomial.php, http://www.calcul.com/show/calculator/binomial-coefficient

# Equal numbers
runner.expect_equal([0, 0], 1) # C(n=0, k=0) => 1
runner.expect_equal([6, 6], 1) # C(n=6, k=6) => 1

# Different numbers, but according the binomial coefficient properties
runner.expect_equal([8, 0], 1) # C(n=8, k=0) => 1
runner.expect_equal([4, 2], 6) # C(n=4, k=2) => 6
runner.expect_equal([5, 2], 10) # C(n=5, k=2) => 10
runner.expect_equal([15, 11], 1365) # C(n=15, k=11) => 1365
runner.expect_equal([50, 3], 19600) # C(n=50, k=3) => 19600
runner.expect_equal([31, 17], 265182525) # C(n=31, k=17) => 265182525
runner.expect_equal([70, 15], 721480692460864) # C(n=70, k=15) => 721480692460864

# Different numbers, where the "k" is not less or equal to "n".
runner.expect_equal([1, 2], -1) # C(n=1, k=2) => The "k" should be less or equal to "n"
runner.expect_equal([3, 7], -1) # C(n=3, k=7) => The "k" should be less or equal to "n"

# Different numbers, but the "k" is a negative number.
runner.expect_equal([13, -2], -1) # C(n=13, k=-2) => The "k" should be non-negative number
runner.expect_equal([3, -5], -1) # C(n=3, k=-5) => The "k" should be non-negative number

# Different numbers, being "n" a negative number.
runner.expect_equal([-13, 2], -1) # C(n=-13, k=2) => The "n" should be non-negative number
runner.expect_equal([-3, 5], -1) # C(n=-13, k=2) => The "n" should be non-negative number
