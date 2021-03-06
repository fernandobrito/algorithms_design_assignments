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
        Create an empty knapsack instance. Available items should be added
         one by one using register_available_item().

        :param constraints_limits: list with numbers
        :param optimal_solution: single number
        """
        self.constraint_limits = constraints_limits
        self.optimal_solution = optimal_solution

        self.constraints_level = [0.0] * len(constraints_limits)

        self.available_items = []
        self.inserted_items = []

        self.total_profit = 0

    def register_available_item(self, item):
        """
        Add an item on the available items set on the knapsack.

        :param item: item to be added
        :return: None
        """
        self.available_items.append(item)

    def compare_with(self, other_knapsack):
        """
        Compare profit of current knapsack with other_kanpsack. It returns the
        ratio of profits.

        > 1 if current has more profit
        = 1 if profit is the same
        < 1 if other_knapsack has more profit

        :param other_knapsack: instance of knapsack to be compared
        :return: ratio of profit
        """
        if other_knapsack.evaluate() == 0:
            return self.evaluate()

        return self.evaluate() / other_knapsack.evaluate()

    def insert_item(self, item):
        """
        Insert an item inside the knapsack.
        It does not verify constraints.
        Total profit is updated automatically.

        :param item: item to be inserted inside
        :return: None
        """
        self.inserted_items.append(item)
        self.total_profit += item.profit
        for i in range(len(item.constraints)):
            self.constraints_level[i] += item.constraints[i]

    def pop_random_available_item(self):
        """
        Pop a random item from the available set.
        has_available_items() should be used before attempting to call it.

        :return: a random available item
        """
        return self.available_items.pop(random.randrange(len(self.available_items)))

    def pop_random_inserted_item(self):
        """
        Pop a random item from the inserted set.
        has_inserted_items() should be used before attempting to call it.
        Total profit is updated automatically.

        :return: a random inserted item
        """

        item = self.inserted_items.pop(random.randrange(len(self.inserted_items)))
        self.total_profit -= item.profit
        for i in range(len(item.constraints)):
            self.constraints_level[i] -= item.constraints[i]

        return item

    def has_available_items(self):
        """
        Verifies if there are items available on available set.

        :return: True or False
        """
        return len(self.available_items) != 0

    def has_inserted_items(self):
        """
        Verifies if there are items available on inserted set.

        :return: True or False
        """
        return len(self.inserted_items) != 0

    def evaluate(self):
        """
        Evaluate function. Return profit if knapsack is valid or -1 if constraints
        are not satisfied.

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
        until it's full. Then it removes a fraction of the inserted items.

        Fraction is hardcoded on constant PARTS_TO_REMOVE_ON_INITIALIZATION.

        :return: a new knapsack instance
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
        Relative percent deviation. How many % from optimal solution the current profit
        is. Zero means optimal solution. Close to 1 means very far from solution.

        :return: relative percent deviation
        """

        return 1 - round(self.total_profit, 1) / round(self.optimal_solution, 1)


class Item:
    """
    Represents an item.
    """

    def __init__(self, constraints, profit):
        """
        Initialize an item.

        :param constraints: list of numbers
        :param profit: single number
        """
        self.constraints = constraints
        self.profit = profit

    def __repr__(self):
        """
        Representation for debugging.

        :return:
        """
        return '(' + ','.join(str(e) for e in self.constraints) + ") " + str(self.profit)

from metaheuristics.problems.parsers.knapsack_parser import KnapsackParser