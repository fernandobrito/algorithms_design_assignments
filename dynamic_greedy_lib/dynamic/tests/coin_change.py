from utils.tests import TestRunner
from dynamic import coin_change

runner = TestRunner(coin_change.solve)

# Trivial examples
runner.expect_equal([0, [1]], 1)
runner.expect_equal([1, [1]], 1)
runner.expect_equal([1, [2]], 0)
runner.expect_equal([10, [2]], 1)
runner.expect_equal([10, [2, 5]], 2)
runner.expect_equal([15, [100]], 0)

# Example from lecture
runner.expect_equal([15, [2, 5, 10]], 3)

# Examples from UVA: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=615
runner.expect_equal([11, [1, 5, 10, 25, 50]], 4)
runner.expect_equal([26, [1, 5, 10, 25, 50]], 13)

# Examples from: https://www.hackerrank.com/challenges/coin-change
runner.expect_equal([4, [1, 2, 3]], 4)
runner.expect_equal([10, [2, 3, 5, 6]], 5)