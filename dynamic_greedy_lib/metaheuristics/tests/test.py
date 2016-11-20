from pprint import pprint

from metaheuristics.tests.agent import Agent
from metaheuristics.techniques.simulated_annealing import SimulatedAnnealing


def run_test():
    file = open('mknap1_2.txt', 'r')
    heuristic = SimulatedAnnealing()

    agent = Agent(heuristic, file)
    agent.execute()

    print("Best solution:")
    pprint(vars(agent.best_solution()))


if __name__ == "__main__":
    run_test()