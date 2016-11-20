# Heavily inspired in
# https://github.com/remiomosowon/pyeasyga/blob/develop/pyeasyga/pyeasyga.py

from metaheuristics.techniques.metaheuristic import MetaHeuristic

class GeneticAlgorithm(MetaHeuristic):
    def __init__(self):
        super().__init__()

    def execute_once(self, knapsack):

        self.worst_solution = 2
        self.best_solution = 10

        print ("===> Genetic Algorithm Living")
        print ("===> Best  solution: {", self.best_solution, "}")
        print ("===> Worst  solution: {", self.worst_solution, "}")

        return knapsack

    def has_finished(self):
        return False