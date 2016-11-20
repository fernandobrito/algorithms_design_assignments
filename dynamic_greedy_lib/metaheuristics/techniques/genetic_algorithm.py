# Heavily inspired in
# https://github.com/remiomosowon/pyeasyga/blob/develop/pyeasyga/pyeasyga.py

from metaheuristics.techniques.metaheuristic import MetaHeuristic

class GeneticAlgorithm(MetaHeuristic):
    def __init__(self):
        super().__init__()

        self.worst_solution = None

    def execute_once(self, knapsack):

        print ("===> Genetic Algorithm Living")
        return knapsack