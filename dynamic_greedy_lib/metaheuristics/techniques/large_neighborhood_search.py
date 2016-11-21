import random
import copy
from operator import add

from metaheuristics.techniques.metaheuristic import MetaHeuristic

class LargeNeighborhoodSearch(MetaHeuristic):
    def __init__(self):
        """
        Constructor.
        """

        super().__init__()

    def setup(self, knapsack, max_iterations):
        """
        Setup the class.

        :param knapsack: a empty knapsack.
        :param max_iterations: Max number of iteractions
        :return: the best knapsack founded.
        """

        self.num_iteractions = max_iterations
        self.destr_factor = 15 # Destruction facotr (%)
        return knapsack.randomize()

    def execute_once(self, knapsack):
        """
        Run the LNS Heuristic.

        :param knapsack: knapsack solution.
        :return: the best knapsack founded.
        """

        best = knapsack
        current = knapsack
        
        for i in range(self.num_iteractions):
            if best.optimal_solution == best.total_profit or i >= self.num_iteractions:
                break

            temp = copy.deepcopy(current)

            temp = self.repair(self.destructor(temp))

            if self.accept(temp, current):
                current = temp
            
            # Changed to get the highest profit
            if self.c(temp) > self.c(best): 
                best = temp

        self.register_solution(best)

        return best

    def repair(self, knapsack):
        """
        Repairs a destroyed solution.

        :param knapsack: knapsack solution.
        :return: knapsack repaired.
        """

        pos = 0

        while True:
            high = -1

            for i in range(pos, len(knapsack.available_items)):
                if knapsack.available_items[i].profit > high:
                    fits = True

                    for j in range(len(knapsack.available_items[i].constraints)):
                        if knapsack.available_items[i].constraints[j] + knapsack.constraints_level[j] > knapsack.constraint_limits[j]:
                            fits = False
                            break

                    if fits:
                        high = knapsack.available_items[i].profit
                        pos = i

            if high > 0:
                knapsack.insert_item(knapsack.available_items.pop(pos))
                pos += 1
            else:
                break

        return knapsack

    def destructor(self, knapsack):
        """
        Destroys part of the solution of the knapsack.

        :param knapsack: knapsack solution.
        :return: knapsack destroyed.
        """

        num_rm = int((len(knapsack.inserted_items) * self.destr_factor) / 100)
        if num_rm < 1:
            num_rm = 1        

        for i in range(num_rm):
            if not knapsack.has_inserted_items():
                break
            item = knapsack.pop_random_inserted_item()
            knapsack.register_available_item(item)

        return knapsack

    def accept(self, knapsack1, knapsack2):
        """
        Valid if the first solution is better than the second.

        :param knapsack1: knapsack solution.
        :param knapsack2: knapsack solution.
        :return: True if knapsack 1 is better than the knapsack 2 and False if not.
        """

        v1 = self.c(knapsack1)
        v2 = self.c(knapsack2)

        if v1 > v2:
            return True
        elif v1 < v2:
            return False

        constr_score = 0

        for constraint1 in knapsack1.constraints_level:
            for constraint2 in knapsack2.constraints_level:
                constr_score = constraint1 - constraint2

        return constr_score < 0

    # Get profit of the knapsack
    def c(self, knapsack):
        """
        Get profit of this solution..

        :param knapsack: knapsack solution.
        :return: knapsack profit.
        """
        return knapsack.total_profit
