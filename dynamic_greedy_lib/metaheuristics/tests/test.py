from pprint import pprint

from metaheuristics.tests.agent import Agent, AgentLogger
from metaheuristics.techniques.simulated_annealing import SimulatedAnnealing

ITERATIONS_PER_FILE = 3

def run_test():
    AgentLogger.clear_log()

    for index in range(ITERATIONS_PER_FILE):
        filename = 'mknap1_2.txt'
        file = open(filename, 'r')

        logger = AgentLogger(filename, str(index))

        heuristic = SimulatedAnnealing()

        agent = Agent(heuristic, file, logger)
        agent.execute()

        print("Best solution:")
        pprint(vars(agent.best_solution()))


if __name__ == "__main__":
    run_test()