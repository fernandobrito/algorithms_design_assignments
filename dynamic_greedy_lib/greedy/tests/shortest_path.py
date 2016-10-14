from utils.tests import TestRunner
from greedy import shortest_path

runner = TestRunner(shortest_path.solve)

# Very simple graph
runner.expect_equal(
    [0, [None]], [0]
)

# Simple graph
runner.expect_equal(
    [0, [[None, 2],
         [None, None]]],
    [0, 2]
)

# Unreachable nodes
runner.expect_equal(
    [0, [[None, None],
         [None, None]]],
    [0, float('inf')]
)

# 3x3
runner.expect_equal(
    [0, [[None, 2, 10],
     [None, None, 2],
     [None, None,  None]]]
    ,
    [0, 2, 4]
)

# 4x4, indirect path. 1 weight to node 1, +1 to node 2, +1 to node 3
runner.expect_equal(
    [0, [[None, 1, None, None],
         [None, None, 1, None],
         [None, None, None, 1],
         [None, None, None, None]]]
    ,
    [0, 1, 2, 3]
)