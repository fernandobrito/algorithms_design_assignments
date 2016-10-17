"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python fractional_knapsack.py

    Resources:
        http://www.geeksforgeeks.org/fractional-knapsack-problem/
        https://www.youtube.com/watch?v=kFUs5VUxO-s
        https://en.wikipedia.org/wiki/Continuous_knapsack_problem

    Description:
        "The knapsack problem or rucksack problem is a problem in combinatorial optimization: Given a set of items, 
        each with a weight and a value, determine the number of each item to include in a collection so that the 
        total weight is less than or equal to a given limit and the total value is as large as possible." [Wikipedia]

        "In Fractional Knapsack, we can break items for maximizing the total value of knapsack. This problem in 
        which we can break item also called fractional knapsack problem." [GeeksforGeeks]

    Complexity: O(n log n)
        Where n is the number of items

    Applications:
        "Knapsack problems appear in real-world decision-making processes in a wide variety of fields, such as finding the 
        least wasteful way to cut raw materials, selection of investments and portfolios, selection of assets for asset-backed 
        securitization, and generating keys for the Merkle–Hellman and other knapsack cryptosystems.
        One early application of knapsack algorithms was in the construction and scoring of tests in which the test-takers have a 
        choice as to which questions they answer. For small examples it is a fairly simple process to provide the test-takers with such a 
        choice. For example, if an exam contains 12 questions each worth 10 points, the test-taker need only answer 10 questions to achieve 
        a maximum possible score of 100 points. However, on tests with a heterogeneous distribution of point values—i.e. different questions 
        are worth different point values — it is more difficult to provide choices. Feuerman and Weiss proposed a system in which students are 
        given a heterogeneous test with a total of 125 possible points. The students are asked to answer all of the questions to the best of 
        their abilities. Of the possible subsets of problems whose total point values add up to 100, a knapsack algorithm would determine 
        which subset gives each student the highest possible score." [Wikipedia]
"""

def solve(input):
    """
    :param input: An array containing the maximum capacity of knapsack in the first position and the items collection in the second position.
    :return: The maximum possible items.
    """

    return _fractional_knapsack(input[0], input[1])

def _fractional_knapsack(capacity, items):
    total_value = 0.0
    total_weight = 0
    sorted_items = sorted(items, key=lambda item: float(item[0] / item[1]))
    sorted_items = sorted_items[::-1]

    for item in sorted_items:
        if total_weight + item[1] > capacity:
            total_value += item[0] * (float(capacity - total_weight) / item[1])
            break
        
        total_value += item[0]
        total_weight += item[1]
    
    return total_value

    