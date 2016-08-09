# Author: Fernando Brito
# Python 3,4
# Usage: python3.4 selection.py

DEBUG = False

import common

# Read input
array = common.read_input()

# Selection sort:
# #1 Find smallest value on entire array, put on index 0
# #2 Find smallest value on what is left, put on index 1...

# For every number in input
for i in range(len(array)):
    # INFO
    DEBUG and print("= Searching smallest on: " + str(array[i:]))

    # Assume number on i is the smallest
    smallest = array[i]
    smallestIndex = i

    # Iterate over what is left from the array to find the real smallest
    for j in range(i, len(array)):

        # If this new element is smaller, update our smallest
        if array[j] < smallest:
            smallest = array[j]
            smallestIndex = j

    # INFO
    DEBUG and print("== Smallest found: " + str(smallest) + " on index " + str(smallestIndex))

    # Swap i and j
    array[smallestIndex] = array[i]
    array[i] = smallest

    # INFO
    DEBUG and print("== New array, after swapping: " + str(array))

# Print result
common.print_output(array)