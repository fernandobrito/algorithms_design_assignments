import copy
import random


class MetaHeuristic:
    # To be implemented
    def execute_once(self, knapsack):
        pass

    # To be implemented
    def has_finished(self):
        pass

    def number_iterations(self):
        return self.iterations

    def generate_random_number(self):
        return 2

    def get_best_from_random_neighbours(self, knapsack, number_random):
        neighbours = []

        # Generate N random neighbours
        for _ in range(number_random):
            neighbours.append(self.generate_neighbour(knapsack))

        neighbours.sort(key=lambda n: n.evaluate())

        best = neighbours.pop()

        if best.evaluate() == -1:
            return None
        else:
            return best

    def generate_neighbour(self, knapsack):
        neighbour = copy.deepcopy(knapsack)

        if random.random() > 0.5:
            if neighbour.has_no_inserted_items():
                neighbour.insert_item(neighbour.pop_random_available_item())
            else:
                neighbour.register_available_item(neighbour.pop_random_inserted_item())
        else:
            if neighbour.has_inserted_items():
                neighbour.register_available_item(neighbour.pop_random_inserted_item())
            else:
                neighbour.insert_item(neighbour.pop_random_available_item())

        return neighbour