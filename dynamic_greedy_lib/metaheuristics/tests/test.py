from metaheuristics.problems.knapsack import Knapsack

def runTest():
    file = open('input_1.txt', 'r')
    parser = Knapsack.getParser()

    content = parser.parse(file)

if __name__ == "__main__":
    runTest()