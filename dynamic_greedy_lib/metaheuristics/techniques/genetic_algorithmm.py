# Heavily inspired in
# https://github.com/remiomosowon/pyeasyga/blob/develop/pyeasyga/pyeasyga.py

import random

from metaheuristics.techniques.metaheuristic import MetaHeuristic

class GeneticAlgorithm(MetaHeuristic):
    def __init__(self, seed_data, constraint_limits, initial_similarity=0.5):
        super().__init__()

        self.seed_data = self.build_seed_data(seed_data)
        self.constraint_limits = constraint_limits
        self.initial_similarity = initial_similarity
        self.knapsack = None

    def execute_once(self, knapsack):
        self.knapsack = knapsack

        self.worst_solution = 5
        self.best_solution = 10

        print ("===> Genetic Algorithm Living")
        print ("===> Best  solution: {", self.best_solution, "}")
        print ("===> Worst  solution: {", self.worst_solution, "}")
        # print ("inserted_items data: ", self.build_seed_data(self.knapsack.inserted_items))
        #
        # if random.random() < self.initial_similarity:
        #     genes = self.create_individual_by_inheritance(self.seed_data)
        #     print ("#######create_individual_by_inheritance#######")
        #     print (genes)
        #     print ("##############")
        # else:
        #     genes = self.create_individual_randomically(self.seed_data)
        #     print ("#######create_individual_randomically#######")
        #     print (genes)
        #     print ("##############")

        return knapsack

    def has_finished(self):
        return False

    def build_seed_data(self, raw_data):
        """Create a items set in a list representation, where each item is a list and its respective
            profit is the last position.

        """
        seed_data = []
        for i in range(len(raw_data)):
            data = list(raw_data[i].constraints)
            data.append(raw_data[i].profit)
            seed_data.append(data)

        return seed_data

    def create_individual_by_inheritance(self, seed_data):
        """Create a candidate solution representation using the genes from the last solution.

        """
        genes = [0] * len(seed_data)

        for item in self.build_seed_data(self.knapsack.inserted_items):
            for data in seed_data:
                if data == item:
                    genes[seed_data.index(item)] = 1

        return genes

    def create_individual_randomically(self, seed_data):
        """Create a candidate solution representation using the genes created randomically.

        """
        return [random.randint(0, 1) for _ in range(len(seed_data))]

    def crossover(self, parent_1, parent_2):
        """Crossover (mate) two parents to produce two children.

        """
        index = random.randrange(1, len(parent_1))
        child_1 = parent_1[:index] + parent_2[index:]
        child_2 = parent_2[:index] + parent_1[index:]
        return child_1, child_2