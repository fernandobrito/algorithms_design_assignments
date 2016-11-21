from utils.string import split_to_float


class KnapsackParser:
    """
    Parse input file following format describer in:
    http://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html

    Accepts only 1 instance per file.
    """

    @staticmethod
    def parse(file):
        """
        Parse 'file' and converts it to a knapsack instance.

        :param file: file object
        :return: knapsack instance, with empty inserted items and
        all items on available set
        """
        # Parse values and create object
        return KnapsackParser.create_object(*KnapsackParser.parse_file(file))

    @staticmethod
    def parse_file(file):
        """
        Parse 'file' and returns raw data. Used internally.

        :param file: file object
        :return: optimal_solution, profits, constraints_limits, constraints_list
        """
        # Parse first line
        header = file.readline()
        amount_items, amount_constraints, optimal_solution = split_to_float(header)

        amount_items = int(amount_items)
        amount_constraints = int(amount_constraints)

        # Parse profits
        profits = split_to_float(file.readline())

        # Parse constraints coefficients
        constraints_list = []

        for _ in range(amount_constraints):
            constraints_list.append(split_to_float(file.readline()))

        # Parse constraints limit
        constraints_limits = split_to_float(file.readline())

        # Transpose matrix
        # File gives a row for constraint, each item on a column
        # We want each row as an item, each column as a constraint
        constraints_list = [list(i) for i in zip(*constraints_list)]

        print(amount_items, amount_constraints, optimal_solution, profits)
        print(constraints_list)
        print(constraints_limits)

        return optimal_solution, profits, constraints_limits, constraints_list

    @staticmethod
    def create_object(optimal_solution, profits, constraints_limits, constraints_list):
        """
        Take raw data from parse_file() and create knapsack instance. Used internally.

        :param optimal_solution: number
        :param profits: list of numbers
        :param constraints_limits: list of numbers
        :param constraints_list: list of lists
        :return:
        """
        # Build the main object
        knapsack = Knapsack(constraints_limits, optimal_solution)

        # Build the items and add it to the knap sack
        for item_index in range(len(constraints_list)):
            item = Item(constraints_list[item_index], profits[item_index])
            knapsack.register_available_item(item)

        return knapsack


from metaheuristics.problems.knapsack import Knapsack, Item