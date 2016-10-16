#from utils.tests import TestRunner
from dynamic import subset_sum_problem

print(subset_sum_problem.solve([[1, 3, 9, 2], 5])) # True
print(subset_sum_problem.solve([[4, 2, 1, 3], 5])) # True
print(subset_sum_problem.solve([[3, 34, 4, 12, 5, 2], 9])) # True
print(subset_sum_problem.solve([[3, 34, 4, 12, 5], 10])) # False
