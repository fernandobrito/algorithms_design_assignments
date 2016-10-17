"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python word_break.py

    Resources:
        http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/


    Description:
        Given an input string and a dictionary of words, find out if the input string can be segmented
        into a space-separated sequence of dictionary words.

    Complexity: O(n²)

    Application:
        Spellchecker for mobile devices

"""

def solve(input):
    """
    :param input:   array with first element: a string that will be analyzed, second element: list that
                    has the words on the dictionary.
                                ex: ["dynamicprogramming", ["programming", "dynamic"]]

    :return:        boolean value that answers if string can be segmented into space separated words.
                                ex: True
    """
    return _word_break(input[0], input[1])


def _word_break(str, dictionary):

    # Create a list to store values that are used to solve shortest problems
    table = [True]

    for i in range(0, len(str)):
        table.append(False)
        j = i

        while j >= 0:
            if table[j] and str[j:i + 1] in dictionary:
                table[-1] = True
                break
            j -= 1

    return table[-1]
