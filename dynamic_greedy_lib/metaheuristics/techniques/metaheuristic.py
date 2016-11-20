import copy
import random


class MetaHeuristic:
    DEBUG = False

    """
    Base meta-heuristic class to be extended by each specific technique.
    """
    def __init__(self):
        """
        Base constructor. Should be used by children.
        Initialize some variables.
        """

        self.iterations = 0
        self.best_solution = None

    # Should be overriden
    def setup(self, knapsack):
        """
        It will be called once by the agent before running execute_once()
        Some heuristics may call randomize() here, or do some custom set up.

        :param knapsack: initial empty knapsack created by parser
        :return: initial state
        """
        pass

    # Should be overridden
    def execute_once(self, knapsack):
        """
        Main method. Runs the meta-heuristic once.
        Should be overridden.

        :param knapsack: solution to be used
        :return: a new (or maybe the same) knapsack instance
        """
        pass

    # Should be overridden
    def has_finished(self):
        """
        Each meta-heuristic can define it's own stop criteria.
        Example: temperature below threshold on Simulated Annealing.
        Should be overridden.

        :return:
        """
        pass

    # Should be called
    def register_solution(self, knapsack):
        """
        After each iteration, specific meta-heuristics should register solution.
        This variable will keep the best solution to be retrieved after all
        iterations are done.

        This is useful because some meta-heuristics can finalize on a hill-climbing
        movement.

        Should be called at the end of execute_once() implementation and
        it automatic increment the number of iterations.

        :param knapsack: solution to be registered
        :return: nothing. Use best_solution() after all iterations are done
        to retrieve best solution
        """

        self.iterations += 1

        if self.best_solution is None or knapsack.compare_with(self.best_solution) > 1:
            # If first solution being registered, register it
            # or if new solution is better than current, register it
            self.best_solution = knapsack

    def number_iterations(self):
        """
        Getter of number of iterations executed.

        Number of iterations is automatically incremented when
        register_solution() is called.

        :return: number of iterations executed.
        """
        return self.iterations

    def get_best_from_random_neighbours(self, knapsack, number_instances):
        """
        Generate a number_random number of neighbours and selects the best one.

        :param knapsack: base knapsack
        :param number_instances: number of neighbours to be generated
        :return: best of the generated neighbours (valid) or None if
        all are invalid.
        """
        neighbours = []

        # Generate N random neighbours
        for _ in range(number_instances):
            neighbours.append(self.generate_neighbour(knapsack))

        neighbours.sort(key=lambda n: n.evaluate())

        best = neighbours.pop()

        if best.evaluate() == -1:
            return None
        else:
            return best

    def generate_neighbour(self, knapsack):
        """
        Given a knapsack solution, creates a neighbour. 50% chance to insert a new item
        (if there is one to be inserted, otherwise take it out) and 50% chance to remove
        an item (if there is one inside, otherwise insert one).

        :param knapsack: base solution
        :return: a copy, with different configuration
        """

        neighbour = copy.deepcopy(knapsack)

        if random.random() > 0.5:
            # Intention is: Try to insert an item in the knapsack
            # However, it may be the case that all items have already been inserted,
            # in this case, the only thing we can do is remove an item.

            if neighbour.has_available_items():
                # Insert item
                neighbour.insert_item(neighbour.pop_random_available_item())
            else:
                # Take item out
                neighbour.register_available_item(neighbour.pop_random_inserted_item())
        else:
            # Intention is: Try to take out an item from the knapsack
            # However, it may be the case that there are no items to be taken,
            # in this case, the only thing we can do is put an item.

            if neighbour.has_inserted_items():
                # Take item out
                neighbour.register_available_item(neighbour.pop_random_inserted_item())
            else:
                # Insert item
                neighbour.insert_item(neighbour.pop_random_available_item())

        return neighbour

    def generate_random_number(self):
        return 1