from utils.tests import TestRunner
from dynamic_algorithms import shortest_path

runner = TestRunner(shortest_path.solve)

input = [[0, None, 3, 0],
         [-2, 0, None, 1],
         [None, None, 0, 5],
         [None, 4, None, 0]]

output = [[0, 4, 3, 0],
          [-2, 0, 1, -2],
          [7, 9, 0, 5],
          [2, 4, 5, 0]]

runner.expect_equal(input, output)