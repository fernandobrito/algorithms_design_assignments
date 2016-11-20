from pprint import pprint

from metaheuristics.tests.agent import Agent, AgentLogger
from metaheuristics.techniques.simulated_annealing import SimulatedAnnealing
from metaheuristics.techniques.genetic_algorithm import GeneticAlgorithm

ITERATIONS_PER_FILE = 3
HEURISTIC_CLASSES = [SimulatedAnnealing, GeneticAlgorithm]

def run_test():
    AgentLogger.clear_log()

    for heuristic_class in HEURISTIC_CLASSES:
        for index in range(ITERATIONS_PER_FILE):
            filename = 'mknap1_2.txt'
            file = open(filename, 'r')

            logger = AgentLogger(filename, str(index))

            agent = Agent(heuristic_class(), file, logger)
            agent.execute()

            print("Best solution:")
            pprint(vars(agent.best_solution()))


if __name__ == "__main__":
    run_test()
