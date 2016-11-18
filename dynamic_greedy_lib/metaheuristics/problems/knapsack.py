import random
import copy
from operator import add

PARTS_TO_REMOVE_ON_INITIALIZATION = 8


class Knapsack:

    """
    Represents a Knapsack instance/solution.
    """

    @staticmethod
    def from_file(file):
        """
        Given a file, creates a knapsack instance.

        :param file: file object
        :return: Knapsack instance
        """
        return KnapsackParser.parse(file)

    def __init__(self, constraints_limits, optimal_solution):
        """


        :param constraints_limits:
        :param optimal_solution:
        """
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
        if other_knapsack.evaluate() == 0:
            return self.evaluate()

        return self.evaluate() / other_knapsack.evaluate()

    def insert_item(self, item):
        self.inserted_items.append(item)
        self.total_profit += item.profit

    def pop_random_available_item(self):
        return self.available_items.pop(random.randrange(len(self.available_items)))

    def pop_random_inserted_item(self):
        item = self.inserted_items.pop(random.randrange(len(self.inserted_items)))
        self.total_profit -= item.profit

        return item

    def has_available_items(self):
        return len(self.available_items) != 0

    def has_inserted_items(self):
        return len(self.inserted_items) != 0

    def evaluate(self):
        """
        Evaluate function

        :return: profit if valid or -1 if invalid. It makes invalid solutions appear
        last when ordering
        """

        # Handle precision errors
        if self.total_profit < 0.0001:
            self.total_profit = 0

        # Start array with 0s
        accumulator = [0 for _ in self.constraint_limits]

        # Add constraints from item by item in accumulator
        for item in self.inserted_items:
            accumulator = list(map(add, accumulator, item.constraints))

            # Check if constraint was exceeded
            for index in range(len(accumulator)):
                if accumulator[index] > self.constraint_limits[index]:
                    return -1

        return self.total_profit

    def randomize(self):
        """
        Assumes a random knapsack at start and insert random items
        until it's full. Then it removes half of the inserted items.

        :return: a new backpack instance
        """

        previous = None
        new = copy.deepcopy(self)

        while new.evaluate() != -1:
            previous = copy.deepcopy(new)
            new.insert_item(new.pop_random_available_item())

        for _ in range(int(len(previous.inserted_items)/PARTS_TO_REMOVE_ON_INITIALIZATION)):
            previous.pop_random_inserted_item()

        return previous

    def rpd(self):
        """
        Relative percent deviation. How many % from optimal solution
        :return:
        """

        return 1 - (self.total_profit / self.optimal_solution)

class Item:
    def __init__(self, constraints, profit):
        self.constraints = constraints
        self.profit = profit

    def __repr__(self):
        return '(' + ','.join(str(e) for e in self.constraints) + ") " + str(self.profit)

from metaheuristics.problems.parsers.knapsack_parser import KnapsackParser