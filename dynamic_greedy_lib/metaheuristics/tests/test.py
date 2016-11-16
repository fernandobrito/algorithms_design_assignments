import pprint
from metaheuristics.problems.knapsack import Knapsack

def runTest():
    file = open('input_1.txt', 'r')
    knapsack = Knapsack.from_file(file)

    pprint.pprint(knapsack)

if __name__ == "__main__":
    runTest()