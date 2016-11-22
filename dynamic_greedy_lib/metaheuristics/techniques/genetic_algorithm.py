# Heavily inspired in
# https://github.com/remiomosowon/pyeasyga/blob/develop/pyeasyga/pyeasyga.py

import copy
import random
from operator import attrgetter

from metaheuristics.techniques.metaheuristic import MetaHeuristic


class GeneticAlgorithm(MetaHeuristic):
    def __init__(self,
                 population_size=8,
                 generations=4,
                 initial_similarity_probability=0.9,
                 crossover_probability=0.8,
                 mutation_probability=0.5,
                 elitism=True,
                 maximise_fitness=True):
        super().__init__()

        self.worst_solution = None
        self.seed_data = None
        self.constraint_limits = None
        self.population_size = population_size
        self.generations = generations
        self.initial_similarity_probability = initial_similarity_probability
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.knapsack = None
        self.current_generation = None
        self.tournament_size = self.population_size // 10
        self.generations_counter = 0
        self.fitness_evaluations = 0
        self.max_fitness_evaluations = None
        self.elitism = elitism
        self.maximise_fitness = maximise_fitness
        self.best_genes = []
        self.worst_genes = []
        self.genes_evaluations_logger = Logger()

    def setup(self, knapsack, max_iterations):
        self.constraint_limits = knapsack.constraint_limits
        self.seed_data = self.build_seed_data(knapsack.available_items)
        self.max_fitness_evaluations = max_iterations * self.generations * self.population_size

        return knapsack.randomize()

    def execute_once(self, knapsack):
        self.iterations += 1
        self.knapsack = knapsack

        self.run()

        self.update_knapsack(self.best_individual())

        self.set_global_individuals(self.best_individual())

        self.genes_evaluations_logger.log(self.iterations, self.knapsack.rpd(), self.fitness_evaluations, self.max_fitness_evaluations)

        self.DEBUG and print("\n===> Optimal solution: ", self.knapsack.optimal_solution)
        self.DEBUG and print("===> Current solution: ", self.knapsack.total_profit)
        self.DEBUG and print("===> Current distance from optimal solution(scale of 0 to 1): ", self.knapsack.rpd())
        self.DEBUG and print("===> Population size: ", self.population_size)
        self.DEBUG and print("===> Generations: ", self.generations_counter)
        self.DEBUG and print("===> Total of fitness evaluations : ", self.fitness_evaluations)
        self.DEBUG and print("===> Less distance from optimal solution(scale of 0 to 1): ", self.best_solution.rpd())
        self.DEBUG and print("===> Best  solution: { Profit: ", self.best_solution.total_profit, ", Genes:", self.best_genes, "}")
        self.DEBUG and print("===> Worst solution: { Profit: ", self.worst_solution.total_profit, ", Genes:", self.worst_genes, "}")

        return self.knapsack

    def has_finished(self):
        if self.fitness_evaluations < self.max_fitness_evaluations*0.6:
            return False
        else:
            return True

    def update_knapsack(self, individual):
        self.knapsack.total_profit = individual[0]

        self.knapsack.available_items = []
        self.knapsack.inserted_items = []

        for (selected, item) in zip(individual[1], self.seed_data):
            if selected:
                self.knapsack.inserted_items.append(item)
            else:
                self.knapsack.available_items.append(item)

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
        for item in self.knapsack.inserted_items:
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

    def genes_evaluate(self, individual, data):
        self.fitness_evaluations += 1
        accumulator = [0] * len(data[0])

        for (selected, item) in zip(individual, data):
            if selected:
                for index in range(len(accumulator)):
                    accumulator[index] += item[index]

        for index in range(len(accumulator) - 1):
            if accumulator[index] > self.constraint_limits[index]:
                accumulator[-1] = 0
                break

        return accumulator[-1]

    def create_initial_population(self):
        """Create members of the first population randomly."""
        initial_population = []
        for _ in range(self.population_size):
            if random.random() < self.initial_similarity_probability:
                genes = self.create_individual_by_inheritance(self.seed_data)
            else:
                genes = self.create_individual_randomically(self.seed_data)

            individual = Chromosome(genes)
            initial_population.append(individual)

        self.current_generation = initial_population

    def calculate_population_fitness(self):
        """Calculate the fitness of every member of the given population using the genes_evaluate."""
        for individual in self.current_generation:
            individual.fitness = self.genes_evaluate(individual.genes, self.seed_data)

    def rank_population(self):
        """Sort the population by fitness according to the order defined by maximise_fitness."""
        self.current_generation.sort(
            key=attrgetter('fitness'), reverse=self.maximise_fitness)

        self.crossover_function = self.crossover
        self.mutate_function = self.mutate
        self.selection_function = self.tournament_selection

    def create_new_population(self):
        """Create a new population using the genetic operators (selection, crossover, and mutation) supplied."""
        new_population = []
        elite = copy.deepcopy(self.current_generation[0])
        selection = self.selection_function

        while len(new_population) < self.population_size:
            parent_1 = copy.deepcopy(selection(self.current_generation))
            parent_2 = copy.deepcopy(selection(self.current_generation))

            child_1, child_2 = parent_1, parent_2
            child_1.fitness, child_2.fitness = 0, 0

            can_crossover = random.random() < self.crossover_probability
            can_mutate = random.random() < self.mutation_probability

            if can_crossover:
                child_1.genes, child_2.genes = self.crossover_function(
                    parent_1.genes, parent_2.genes)

            if can_mutate:
                self.mutate_function(child_1.genes)
                self.mutate_function(child_2.genes)

            new_population.append(child_1)
            if len(new_population) < self.population_size:
                new_population.append(child_2)

        if self.elitism:
            new_population[0] = elite

        self.current_generation = new_population

    def create_first_generation(self):
        """Create the first population, calculate the population's fitness and
        rank the population by fitness according to the order specified.
        """
        self.generations_counter += 1

        self.create_initial_population()
        self.calculate_population_fitness()
        self.rank_population()

    def create_next_generation(self):
        """Create subsequent populations, calculate the population fitness and
        rank the population by fitness in the order specified.
        """
        self.generations_counter += 1

        self.create_new_population()
        self.calculate_population_fitness()
        self.rank_population()

    def run(self):
        """Run (solve) the Genetic Algorithm."""
        self.create_first_generation()

        for _ in range(1, self.generations):
            self.create_next_generation()

    def best_individual(self):
        """Return the individual with the best fitness in the current generation.
        """
        best = self.current_generation[0]
        return best.fitness, best.genes

    def set_global_individuals(self, best_individual):
        if self.iterations == 1:
            self.worst_solution = self.knapsack
            self.best_solution = self.knapsack
            self.best_genes = self.worst_genes = best_individual[1]
        elif best_individual[0] < self.worst_solution.total_profit:
                self.worst_genes = best_individual[1]
                self.worst_solution = self.knapsack
        elif best_individual[0] > self.best_solution.total_profit:
                self.best_genes = best_individual[1]
                self.best_solution = self.knapsack


class Chromosome(object):
    """ Chromosome class that encapsulates an individual's fitness and solution
    representation.
    """
    def __init__(self, genes):
        """Initialise the Chromosome."""
        self.genes = genes
        self.fitness = 0

    def __repr__(self):
        """Return initialised Chromosome representation in human readable form.
        """
        return repr((self.fitness, self.genes))


class Logger:
    def __init__(self):
        self.file = open('../output/ga_output.txt', 'w')
        self.file.write('iteration;rpd;genes_evaluations\n')

    def log(self, iteration, rpd, genes_evaluations, max_genes_evaluations):
        current_distance_from_max_genes_evaluations_scale_0_1 = (float(genes_evaluations) / float(max_genes_evaluations))
        self.file.write("{0};{1};{2}\n".format(iteration, rpd, current_distance_from_max_genes_evaluations_scale_0_1))

