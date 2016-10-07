from utils.tests import TestRunner
from dynamic_algorithms import edit_distance

runner = TestRunner(edit_distance.solve)

# Verified using http://www.let.rug.nl/kleiweg/lev/

# Empty strings
runner.expect_equal(["", ""], 0)
runner.expect_equal(["", "fernando"], 8)
runner.expect_equal(["fernando", ""], 8)

# Normal strings
runner.expect_equal(["david", "fernando"], 7)
runner.expect_equal(["abababababa", "bababababab"], 2)

# Insertion and deletion
runner.expect_equal(["aaabaaaa", "aaaaaaa"], 1)
runner.expect_equal(["aaaaaaa", "aaaabaaa"], 1)
runner.expect_equal(["aaaaaaa", "baaaaaaa"], 1)
runner.expect_equal(["aaaaaaab", "aaaaaaaa"], 1)

# Substitution
runner.expect_equal(["aaaaaaa", "aaaaaax"], 1)
runner.expect_equal(["axaaaaa", "aaaaaaa"], 1)