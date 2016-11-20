from pprint import pprint
import time

from metaheuristics.problems.knapsack import Knapsack

MAX_ITERATIONS = 20000
MAX_TIME = 3 # in seconds

class Agent:
    """
    Agent to run a single heuristic, once, on a single file.
    """

    def __init__(self, heuristic, file, logger):
        # Store variables
        self.heuristic = heuristic
        self.knapsack = Knapsack.from_file(file)

        # Initial state of knapsack
        self.knapsack = self.heuristic.setup(self.knapsack)

        # Timer
        self.timer = 0

        # Logger
        self.logger = logger

    def execute(self):
        for index in range(MAX_ITERATIONS):
            print("\n\n=== Running ", index)

            # Execute execute_once on heuristic and time it
            start_time = time.time()
            self.knapsack = self.__run_step()
            end_time = time.time()

            # Print the time difference
            time_difference = end_time - start_time
            self.timer += time_difference
            print("====> Timer: ", self.timer)

            # Check stop conditions
            # From heuristic
            if self.heuristic.has_finished():
                break

            # From time
            if self.__has_timedout():
                print("timed out!")
                break

        self.__log()

    def __run_step(self):
        print("Current")
        pprint(vars(self.knapsack))
        return self.heuristic.execute_once(self.knapsack)

    def __log(self):
        self.logger.log(self.heuristic.__class__.__name__, self.best_solution().rpd())

    def __has_timedout(self):
        return self.timer > MAX_TIME

    def best_solution(self):
        return self.heuristic.best_solution



class AgentLogger:
    def __init__(self, filename, counter):
        self.filename = filename
        self.counter = counter

        self.file = open('../output/agents.txt', 'a')
        self.file.write('counter;filename;heuristic;rpd\n')

    @staticmethod
    def clear_log():
        file = open('../output/agents.txt', 'w')
        file.truncate()

    def log(self, heuristic, rpd):
        self.file.write("{0};{1};{2};{3}\n".format(self.counter, self.filename, heuristic, rpd))