"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python activity_selection.py

    Resources:
        http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/
        https://en.wikipedia.org/wiki/Activity_selection_problem

    Description:
        The activity selection problem is a combinatorial optimization problem concerning the
        selection of non-conflicting activities to perform within a given time frame, given a
        set of activities each marked by a start time (S[i]) and finish time (F[i]). The problem
        is to select the maximum number of activities that can be performed by a single person or
        machine, assuming that a person can only work on a single activity at a time.

    Complexity: O(n)
        Where n is the number of activities

    Applications:
        A classic application of this problem is in scheduling a room for multiple competing events,
        each having its own time requirements (start and end time), and many more arise within the
        framework of operations research.
"""


def solve(input):
    """
    :param input:   array with first element: list that contains start time of all activities (should be
                    non-empty), second element: list that contains the respective finish time of all
                    activities (should be non-empty, sorted by ascending order, and must have the same
                    length of the first list).
                                ex: [[1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]]

    :return:        array that contain the index of the selected activities
                                ex: [0, 1, 3, 4]
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
