# Heavily inspired in
# https://github.com/OmeGak/HybridKnapsack/blob/master/src/heuristics/SimulatedAnnealing.java

import math
import random
from pprint import pprint

from metaheuristics.techniques.metaheuristic import MetaHeuristic

class SimulatedAnnealing(MetaHeuristic):
    def __init__(self, temperature=100, freezing_rate=0.99):
        self.temperature = temperature
        self.freezing_rate = freezing_rate

    def execute_once(self, knapsack):
        # Generate a random number
        number_neighbours = self.generate_random_number()

        # Generate N random neighbours and return best
        best_neighbour = self.get_best_from_random_neighbours(knapsack, number_neighbours)

        print("Selected best best_neighbour")
        pprint(vars(best_neighbour))

        print("===> Probability :", self.__calculate_probability(knapsack, best_neighbour))

        if best_neighbour.compare_with(knapsack) > 1:
            # If best neighbour is best than current backpack
            # choose it and freeze the temperature
            print("====> Better solution. Freezing. Current temperature ", self.temperature)
            self.__freeze_temperature()
            return best_neighbour
        else:
            print("====> Worse solution")

            # Else, there is a chance that we still choose
            # a worst solution
            calculated_random = random.random()
            calculated_probability = self.__calculate_probability(knapsack, best_neighbour)

            if calculated_random >= calculated_probability:
                print("====> Chose worst. ", calculated_random, " > ", calculated_probability)

                self.__heat_temperature()
                return best_neighbour
            else:
                print("====> Stayed with best. ", calculated_random, " < ", calculated_probability)
                return knapsack


    def __calculate_probability(self, current, next):
        delta = next.evaluate() - current.evaluate()
        return 1/(1 + math.exp(delta / self.temperature))

    def __heat_temperature(self):
        self.temperature *= self.freezing_rate

    def __freeze_temperature(self):
        self.temperature *= self.freezing_rate
