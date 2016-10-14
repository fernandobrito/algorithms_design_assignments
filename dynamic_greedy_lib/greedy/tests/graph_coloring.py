from utils.tests import TestRunner
from greedy import graph_coloring

runner = TestRunner(graph_coloring.solve)

# Trivial example: one vertex
runner.expect_equal(
    [1, []], [0]
)

# Trivial example: two vertices and no edges
runner.expect_equal(
    [2, []], [0, 0]
)

# Trivial example: two vertices and 1 edge
runner.expect_equal(
    [2, [[0, 1]]], [0, 1]
)

# Graph from http://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
runner.expect_equal(
    [5, [[0,1], [0,2], [1,2], [1,3], [2,3], [3,4]]]
    ,
    [0, 1, 2, 0, 1]
)

# Graph from http://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
runner.expect_equal(
    [5, [[0,1], [0,2], [1,2], [1,4], [2,4], [4,3]]]
    ,
    [0, 1, 2, 0, 3]
)