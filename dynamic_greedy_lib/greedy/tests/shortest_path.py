from utils.tests import TestRunner
from greedy import shortest_path

runner = TestRunner(shortest_path.solve)

# Very simple graph
runner.expect_equal(
    [0, [[None, 2, 10],
     [None, None, 2],
     [None, None,  None]]]
    ,
    [0, 2, 4]
)