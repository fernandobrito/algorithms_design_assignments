from utils.tests import TestRunner
from greedy import kruskal_coding
"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python kruskal_coding.py
    Resources:
        http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
"""

runner = TestRunner(kruskal_coding.solve)

# Graph with 5 edges and 4 vertices (Without cyrcles)
runner.expect_equal(
    [[10, 0, 1], [6, 0, 2], [15, 1, 3], [4, 2, 3]], [[4, 2, 3], [6, 0, 2], [10, 0, 1]]
)

# Graph with 5 edges and 4 vertices (With cyrcles)
runner.expect_equal(
    [[10, 0, 1], [6, 0, 2], [5, 0, 3], [15, 1, 3], [4, 2, 3]], [[4, 2, 3], [5, 0, 3], [10, 0, 1]]
)

# Graph with 14 edges and 9 vertices (With cyrcles)
runner.expect_equal(
    [[4, 0, 1], [8, 1, 2], [7, 2, 3], [9, 3, 4], [10, 5, 4], [2, 6, 5], [1, 7, 6], [7, 7, 8], [2, 8, 2], [6, 8, 6], [4, 2, 5], [8, 0, 7], [11, 1, 7], [14, 3, 5]]
    ,
    [[1, 7, 6], [2, 6, 5], [2, 8, 2], [4, 0, 1], [4, 2, 5], [7, 2, 3], [8, 1, 2], [9, 3, 4]]
)