from utils import table as table_utils

"""
Given a set of coins and a change value, find how many different ways
there are to provide this change. The order of coins does not matter in
the final result.

Complexity: O(m * n)
    O(1) in all positions on table of size m * n, where m is number
    of different possible coins on input and n is change size.

Author: Fernando Brito (11111309)

Resources:
    - http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
"""

def solve(input):
    """
    :param input: array with change value (integer >= 0) and coin values set, ordered ([1, 5, 10])
    :return: number of possible solutions
    """

    change = input[0]
    coins = input[1]

    return _coin_change(change, coins)


def _coin_change(total_change, coins):
    # Initialize table. Rows for change and columns for index of which
    # coins should be included (cumulative effect, including previous set)

    #       {c1}, {c1,c2}, {c1, c2, c3}
    #    0
    #    1
    #    2
    table = table_utils.initialize(total_change + 1, len(coins), 0)

    # Fill entries for the first row with 1, as for 0 change we can always
    # find a solution (not giving any coins)
    for coin in range(len(coins)):
        table[0][coin] = 1

    # Fill table in a bottom up manner, iterating over all coin possibilities
    # for a fixed change, starting from change 0
    for change in range(1, total_change + 1):

        # For all indices of coins
        for coin in range(len(coins)):
            # If there were other (smaller) coins, solutions
            # with this coin should be at least the same
            if (coin >= 1):
                without_this_coin = table[change][coin-1]
            else:
                without_this_coin = 0

            # If we can include this coin:
            if change - coins[coin] >= 0:
                # Then take number of solutions with this same coin, but
                # for (change - value of this coin)
                with_this_coin = table[change - coins[coin]][coin]
            else:
                with_this_coin = 0

            # Add number of solutions without and with this coin
            table[change][coin] = without_this_coin + with_this_coin

    # Return last element
    return table[total_change][len(coins)-1]