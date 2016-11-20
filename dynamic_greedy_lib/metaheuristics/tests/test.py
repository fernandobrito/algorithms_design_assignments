from pprint import pprint

from metaheuristics.tests.agent import Agent, AgentLogger
from metaheuristics.techniques.simulated_annealing import SimulatedAnnealing
from metaheuristics.techniques.genetic_algorithm import GeneticAlgorithm

# Parameters for the experiment
HEURISTIC_CLASSES = [SimulatedAnnealing, GeneticAlgorithm]
INPUT_FILES = ['mknap1_1.txt', 'mknap1_2.txt', 'mknap1_3.txt',
               'mknap1_4.txt', 'mknap1_5.txt', 'mknap1_6.txt', 'mknap1_7.txt']
ITERATIONS_PER_FILE = 7


def run_test():
    AgentLogger.clear_log()

    """
    Run all heuristics on all files N amount of times.
    """
    for heuristic_class in HEURISTIC_CLASSES:
        for filename in INPUT_FILES:
            for index in range(ITERATIONS_PER_FILE):
                file = open(filename, 'r')

                logger = AgentLogger(filename, str(index))

                agent = Agent(heuristic_class(), file, logger)
                agent.execute()

                print("Best solution:")
                pprint(vars(agent.best_solution()))


if __name__ == "__main__":
    run_test()
