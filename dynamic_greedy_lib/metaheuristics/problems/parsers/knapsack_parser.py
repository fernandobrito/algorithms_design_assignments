from utils.string import split_to_int

class KnapsackParser:
    @staticmethod
    def parse(file):
        # Parse values and create object
        return KnapsackParser.create_object(*KnapsackParser.parse_file(file))

    @staticmethod
    def parse_file(file):
        # Parse first line
        header = file.readline()
        amount_items, amount_constraints, optimal_solution = split_to_int(header)

        # Parse profits
        profits = split_to_int(file.readline())

        # Parse constraints coefficients
        constraints_list = []

        for _ in range(amount_constraints):
            constraints_list.append(split_to_int(file.readline()))

        # Parse constraints limit
        constraints_limits = split_to_int(file.readline())

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

        # Build the main object
        knapsack = Knapsack(constraints_limits, optimal_solution)

        # Build the items and add it to the knap sack
        for item_index in range(len(constraints_list)):
            item = Item(constraints_list[item_index], profits[item_index])
            knapsack.register_available_item(item)

        return knapsack


from metaheuristics.problems.knapsack import Knapsack, Item