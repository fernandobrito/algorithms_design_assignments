from utils.tests import TestRunner
from dynamic import word_break

"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python word_break.py
    Resources:
        https://github.com/jcarva/algorithms/blob/dynamic-programming/binomial-coefficient-test.js
"""

runner = TestRunner(word_break.solve)

# Empty string and dictionary
runner.expect_equal(["", []], True)

# Empty string
runner.expect_equal(["", ["test", "word", "break"]], True)
runner.expect_equal(["", ["analysis", "algorithms", "design", "and"]], True)

# Empty dictionary
runner.expect_equal(["testwordbreak", []], False)
runner.expect_equal(["dynamicprogramming", []], False)

# Non-empty string and dictionary
runner.expect_equal(["dynamicprogramming", ["programming", "dynamic"]], True)
runner.expect_equal(["analysisanddesignofalgorithms", ["analysis", "algorithms", "design", "and"]], False)
runner.expect_equal(["analysisanddesignalgorithms", ["analysis", "algorithms", "design", "and"]], True)

# The below tests can be verified on http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/
dictionary = ["mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream"]

runner.expect_equal(["ilikesamsung", dictionary], True)
runner.expect_equal(["iiiiiiii", dictionary], True)
runner.expect_equal(["", dictionary], True)
runner.expect_equal(["ilikelikeimangoiii", dictionary], True)
runner.expect_equal(["samsungandmango", dictionary], True)
runner.expect_equal(["samsungandmangok", dictionary], False)