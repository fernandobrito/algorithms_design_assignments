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