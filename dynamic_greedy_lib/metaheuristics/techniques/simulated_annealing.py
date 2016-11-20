# Heavily inspired in
# https://github.com/OmeGak/HybridKnapsack/blob/master/src/heuristics/SimulatedAnnealing.java

import math
import random
from pprint import pprint

from metaheuristics.techniques.metaheuristic import MetaHeuristic

# The higher, the lower the chance of accepting worse solutions
POWER_PROBABILITY = 2

class SimulatedAnnealing(MetaHeuristic):
    def __init__(self, temperature=1, freezing_rate=0.999, minimum_temperature=0.01):
        super().__init__()

        self.temperature = temperature
        self.minimum_temperature = minimum_temperature
        self.freezing_rate = freezing_rate

        self.temperature_logger = Logger()

    def setup(self, knapsack):
        return knapsack.randomize()

    def execute_once(self, knapsack):
        # Generate a random number
        number_neighbours = self.generate_random_number()

        # Generate N random neighbours and return best
        best_neighbour = self.get_best_from_random_neighbours(knapsack, number_neighbours)

        if best_neighbour is None:
            print("====> No valid neighbour found")
            return knapsack

        print("Selected best best_neighbour")
        pprint(vars(best_neighbour))

        print("===> Probability :", self.__calculate_probability(knapsack, best_neighbour))

        chosen = None

        if best_neighbour.compare_with(knapsack) > 1:
            # If best neighbour is best than current backpack
            # choose it and freeze the temperature
            print("====> Better solution. Freezing. Current temperature ", self.temperature)
            self.__freeze_temperature()
            chosen = best_neighbour
        else:
            print("====> Worse solution")

            # Else, there is a chance that we still choose
            # a worst solution
            calculated_random = random.random()
            calculated_probability = self.__calculate_probability(knapsack, best_neighbour)

            if calculated_probability >= calculated_random:
                print("====> Chose worst. ", calculated_probability, " > ", calculated_random)

                self.__heat_temperature()
                chosen = best_neighbour
            else:
                print("====> Stayed with best. ", calculated_probability, " < ", calculated_random)
                self.__freeze_temperature()
                chosen = knapsack


        self.temperature_logger.log(self.iterations, chosen.rpd(), self.temperature,
                                    self.__calculate_probability(knapsack, best_neighbour))

        self.register_solution(chosen)

        return chosen


    def has_finished(self):
        return (self.temperature < self.minimum_temperature)

    def __calculate_probability(self, current, next):
        # In %
        current_profit = current.evaluate()

        if current_profit != 0:
            delta = (current_profit - next.evaluate())/current_profit
        else:
            delta = 0.5

        return math.pow(math.exp(-delta / self.temperature), POWER_PROBABILITY)

    def __heat_temperature(self):
        self.temperature *= 1 + (math.pow(1 - self.freezing_rate, 1.1))

    def __freeze_temperature(self):
        self.temperature *= self.freezing_rate




class Logger:
    def __init__(self):
        self.file = open('../output/output.txt', 'w')
        self.file.write('iteration;rpd;temperature;probability\n')

    def log(self, iteration, rpd, temperature, probability):
        self.file.write("{0};{1};{2};{3}\n".format(iteration, rpd, temperature, probability))