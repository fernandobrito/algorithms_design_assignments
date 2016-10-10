"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python word_break.py
    Resources:
        http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/


    Description:

    Complexity:

    Application:
"""

def solve(input):
    """
    Input : should contain a string that will be analyzed and a list that has the words on the dictionary.
    Output : boolean value that answer if string can be table into space separated words.
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
