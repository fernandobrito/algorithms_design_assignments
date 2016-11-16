import random

class Knapsack:
    @staticmethod
    def from_file(file):
        return KnapsackParser.parse(file)

    def __init__(self, constraints_limits, optimal_solution):
        self.constraint_limits = constraints_limits
        self.optimal_solution = optimal_solution

        self.available_items = []
        self.inserted_items = []

        self.total_profit = 0

    def register_available_item(self, item):
        self.available_items.append(item)

    def compare_with(self, other_knapsack):
        """
        :param other_knapsack:
        :return: ratio of improvement
        """
        if other_knapsack.total_profit == 0:
            return self.total_profit

        return self.total_profit / other_knapsack.total_profit

    def insert_item(self, item):
        self.inserted_items.append(item)
        self.total_profit += item.profit

    def pop_random_available_item(self):
        return self.available_items.pop(random.randrange(len(self.available_items)))

    def pop_random_inserted_item(self):
        return self.inserted_items.pop(random.randrange(len(self.inserted_items)))

    def has_no_inserted_items(self):
        return len(self.available_items) != 0

    def has_inserted_items(self):
        return len(self.inserted_items) != 0


class Item:
    def __init__(self, constraints, profit):
        self.constraints = constraints
        self.profit = profit

    def __repr__(self):
        return '(' + ','.join(str(e) for e in self.constraints) + ") " + str(self.profit)

from metaheuristics.problems.parsers.knapsack_parser import KnapsackParser