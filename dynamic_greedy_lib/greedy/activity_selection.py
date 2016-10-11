"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python activity_selection.py
    Resources:
        http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/
        https://en.wikipedia.org/wiki/Activity_selection_problem

    Description:

    Complexity:

    Application:
"""


def solve(input):
    """
    Input : ---
    Output : ---
    """

    return _activity_selection(input[0], input[1])


def _activity_selection(starts, finishes):
    if len(starts) == 0 or len(finishes) == 0:
        return "Empty lists are not accepted"

    if len(starts) != len(finishes):
        return -1

    # The first activity is always selected
    selected_activities = [0]

    i = j = 0

    # Analyze rest of the activities
    while i < len(finishes):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if starts[i] >= finishes[j]:
            selected_activities.append(i)
            j = i

        i += 1

    return selected_activities
