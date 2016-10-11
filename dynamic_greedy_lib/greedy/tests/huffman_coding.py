from utils.tests import TestRunner
from greedy import huffman_coding
"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python huffman_coding.py
    Resources:
        https://github.com/jcarva/algorithms/blob/dynamic-programming/binomial-coefficient-test.js
"""

runner = TestRunner(huffman_coding.solve)

# Empty lists
runner.expect_equal([[], []], "Empty lists are not accepted")

# Empty dictionary list
runner.expect_equal([[], [5, 9, 12, 13, 16, 45]], "Empty lists are not accepted")
runner.expect_equal([[], [5, 9, 12, 13, 16, 45, 33, 80, 21, 45]], "Empty lists are not accepted")

# Empty frequency list
runner.expect_equal([['a', 'b', 'c', 'd', 'e', 'f'], []], "Empty lists are not accepted")
runner.expect_equal([['k', 'l', 'i', 'd', 'e', 'f', 'm', 'o', 'r', 'j'], []], "Empty lists are not accepted")

# Symbol list bigger than frenquecy list
runner.expect_equal([['a', 'b', 'c', 'd', 'e'], [24, 12, 10, 8]], -1)
runner.expect_equal([['a', 's', 'x', 'd', 'e', 'f', 'x'], [12, 13, 16, 45]], -1)

# Frequency list bigger than symbol list
runner.expect_equal([['a', 'b', 'c', 'e'], [5, 9, 12, 13, 16, 45, 33, 80, 21, 45]], -1)
runner.expect_equal([['a'], [12, 13, 16, 45]], -1)

# The below tests can be verified onhttp://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/  #- [Run on IDE]
runner.expect_equal([['a', 'b', 'c', 'd', 'e'], [24, 12, 10, 8, 8]]
                    ,
                    [['a', '0'], ['b', '111'], ['c', '110'], ['d', '100'], ['e', '101']]
)
runner.expect_equal([['a', 'b', 'c', 'd', 'e', 'f'], [5, 9, 12, 13, 16, 45]]
                    ,
                    [['a', '1100'], ['b', '1101'], ['c', '100'], ['d', '101'], ['e', '111'], ['f', '0']]
)
runner.expect_equal([['k', 'l', 'i', 'd', 'e', 'f', 'm', 'o', 'r', 'j'], [5, 9, 12, 13, 16, 45, 33, 80, 21, 45]]
                    ,
                    [['d', '0011'], ['e', '0101'], ['f', '110'], ['i', '0010'], ['j', '111'], ['k', '01000'],
                     ['l', '01001'], ['m', '011'], ['o', '10'], ['r', '000']
                    ]
)
runner.expect_equal([['a','f', 'g', 'j', 'm', 'q', 's', 'u', 'v', 'x', 'z'], [39, 11, 2, 25, 16, 45, 3, 43, 64, 21, 35]]
                    ,
                    [['a', '100'], ['f', '01011'], ['g', '010100'], ['j', '1111'], ['m', '0100'], ['q', '110'],
                     ['s', '010101'], ['u', '101'], ['v', '00'], ['x', '1110'], ['z', '011']
                    ]
)
runner.expect_equal([['a','f', 'g', 'j', 'm', 'q', 's', 'u', 'v', 'x', 'z'], [5, 9, 12, 13, 16, 45, 3, 43, 64, 21, 35]]
                    ,
                    [['a', '100101'], ['f', '10011'], ['g', '0010'], ['j', '0011'], ['m', '1000'], ['q', '111'],
                     ['s', '100100'], ['u', '110'], ['v', '01'], ['x', '000'], ['z', '101']
                    ]
)
