from pprint import pprint

from metaheuristics.tests.agent import Agent
from metaheuristics.techniques.simulated_annealing import SimulatedAnnealing
from metaheuristics.techniques.genetic_algorithmm import GeneticAlgorithm

def run_test():
    file = open('mknap1_4.txt', 'r')
    #heuristic = SimulatedAnnealing()
    heuristic = GeneticAlgorithm()

    agent = Agent(heuristic, file)
    agent.execute()

    print("Best solution:")
    pprint(vars(agent.best_solution()))


if __name__ == "__main__":
    run_test()
