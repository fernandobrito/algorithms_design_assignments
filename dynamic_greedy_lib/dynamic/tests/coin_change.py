from utils.tests import TestRunner
from dynamic import coin_change

runner = TestRunner(coin_change.solve)

runner.expect_equal([15, [2, 5, 10]], 3)