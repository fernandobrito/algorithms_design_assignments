# Heavily inspired in
# https://github.com/remiomosowon/pyeasyga/blob/develop/pyeasyga/pyeasyga.py

import random
from operator import attrgetter

from metaheuristics.techniques.metaheuristic import MetaHeuristic

class GeneticAlgorithm(MetaHeuristic):
    def __init__(self,
                 seed_data,
                 constraint_limits,
                 population_size=10,
                 initial_similarity_probability=0.5,
                 crossover_probability=0.8,
                 mutation_probability=0.5):
        super().__init__()

        self.seed_data = self.build_seed_data(seed_data)
        self.constraint_limits = constraint_limits
        self.population_size = population_size,
        self.initial_similarity_probability = initial_similarity_probability
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.tournament_size = self.population_size // 10
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
        # if random.random() < self.initial_similarity_probability:
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
        """Create a candidate solution representation using the genes from the last solution."""
        genes = [0] * len(seed_data)

        for item in self.build_seed_data(self.knapsack.inserted_items):
            for data in seed_data:
                if data == item:
                    genes[seed_data.index(item)] = 1

        return genes

    def create_individual_randomically(self, seed_data):
        """Create a candidate solution representation using the genes created randomically."""
        return [random.randint(0, 1) for _ in range(len(seed_data))]

    def crossover(self, parent_1, parent_2):
        """Crossover (mate) two parents to produce two children."""
        index = random.randrange(1, len(parent_1))
        child_1 = parent_1[:index] + parent_2[index:]
        child_2 = parent_2[:index] + parent_1[index:]
        return child_1, child_2

    def mutate(self, individual):
        """Reverse the bit of a random index in an individual."""
        mutate_index = random.randrange(len(individual))
        individual[mutate_index] = (0, 1)[individual[mutate_index] == 0]

    def random_selection(self, population):
        """Select and return a random member of the population."""
        return random.choice(population)

    def tournament_selection(self, population):
        """Select a random number of individuals from the population and
        return the fittest member of them all.
        """

        if self.tournament_size == 0:
            self.tournament_size = 2

        members = random.sample(population, self.tournament_size)
        members.sort(key=attrgetter('fitness'), reverse=self.maximise_fitness)

        return members[0]