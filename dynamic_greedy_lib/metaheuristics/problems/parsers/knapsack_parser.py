from utils.string import split_to_int


class KnapsackParser:
    @staticmethod
    def parse(file):
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

        print(amount_items, amount_constraints, optimal_solution, profits)
        print(constraints_list)
        print(constraints_limits)