# Heavily inspired in
# https://github.com/remiomosowon/pyeasyga/blob/develop/pyeasyga/pyeasyga.py

from metaheuristics.techniques.metaheuristic import MetaHeuristic

class GeneticAlgorithm(MetaHeuristic):
    def __init__(self, seed_data, constraint_limits):
        super().__init__()

        def build_seed_data(raw_data):
            """Create a items set in a list representation, where each item is a list and its respective
                profit is the last position
            """
            seed_data = []
            for i in range(len(raw_data)):
                data = list(raw_data[i].constraints)
                data.append(raw_data[i].profit)
                seed_data.append(data)

            return seed_data

        self.seed_data = build_seed_data(seed_data)
        self.constraint_limits = constraint_limits

    def execute_once(self, knapsack):

        self.worst_solution = 2
        self.best_solution = 10

        print ("===> Genetic Algorithm Living")
        print ("===> Best  solution: {", self.best_solution, "}")
        print ("===> Worst  solution: {", self.worst_solution, "}")
        print ("Seed data: ", self.seed_data)

        return knapsack

    def has_finished(self):
        return False