class Knapsack:
    def __init__(self, constraints_limits, optimal_solution):
        self.constraint_limits = constraints_limits
        self.optimal_solution = optimal_solution

        self.available_items = []
        self.selected_items = []

    def add_available_item(self, item):
        self.available_items.append(item)


    @staticmethod
    def from_file(file):
        return KnapsackParser.parse(file)


class Item:
    def __init__(self, constraints, profit):
        self.constraints = constraints
        self.value = profit

from metaheuristics.problems.parsers.knapsack_parser import KnapsackParser