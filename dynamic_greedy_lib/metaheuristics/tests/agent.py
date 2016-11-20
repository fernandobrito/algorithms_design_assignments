from pprint import pprint
import time

from metaheuristics.problems.knapsack import Knapsack

MAX_ITERATIONS = 10000
MAX_TIME = 5 # in seconds

class Agent:
    """
    Agent to run a single heuristic, once, on a single file.
    """

    def __init__(self, heuristic, file):
        # Store variables
        self.heuristic = heuristic
        self.knapsack = Knapsack.from_file(file)

        # Initial state of knapsack
        self.knapsack = self.heuristic.setup(self.knapsack)

        # Timer
        self.timer = 0

    def execute(self):
        for index in range(MAX_ITERATIONS):
            print("\n\n=== Running ", index)

            start_time = time.time()
            self.__run_step()
            end_time = time.time()

            time_difference = end_time - start_time
            self.timer += time_difference
            print("====> Timer: ", self.timer)

            # log

            if self.heuristic.has_finished():
                break

            if self.__has_timedout():
                print("timed out!")
                break

    def __run_step(self):
        print("Current")
        pprint(vars(self.knapsack))
        self.knapsack = self.heuristic.execute_once(self.knapsack)

    def __log(self):
        pass

    def __has_timedout(self):
        return self.timer > MAX_TIME

    def best_solution(self):
        return self.heuristic.best_solution