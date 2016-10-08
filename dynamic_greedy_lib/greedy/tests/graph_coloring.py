from utils.tests import TestRunner
from greedy import graph_coloring

runner = TestRunner(graph_coloring.solve)

# Very simple graph
runner.expect_equal(
    [5, [[0, 1], [0,2], [1,2], [1,3], [2,3], [3,4]]]
    ,
    [0, 1, 2, 0, 1]
)