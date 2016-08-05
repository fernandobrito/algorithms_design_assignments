# Author: Fernando Brito
# Python 3,4
# Usage: python3.4 selection.py <input>
# Example: python3.4 selection.py 3 5 6 1 2 4 3 2

import sys
import common

print("== MERGE SORT ==")

# Read input
input = common.read_input(sys.argv)

print("Input: " + str(input))
print()

# Merge sort:
# "1: Divide the unsorted list into n sublists, 
#     each containing 1 element (a list of 1 element is considered sorted).
# 
# 2: Repeatedly merge sublists to produce new sorted sublists until there 
#    is only 1 sublist remaining. This will be the sorted list." (Wikipedia)

# Level is not part of the algorithm. It is being used just to print the call stack
def sort(list, level):
    # Trivial sorted array, with 1 element
    # Base of recursion. Return array
    if len(list) <= 1:
        return list

    # Increment level, for printing purposes
    level += 1

    # Split array in the middle
    middle = int(len(list) / 2)
    left = list[0:middle]
    right = list[middle:]

    # INFO
    print("/" * level*3 + " Split: " + str(list))

    # Call the recursion
    # Sort each subarray and merge the results
    return merge(sort(left, level), sort(right, level), level)

# Merge two arrays
def merge(left, right, level):
    # Start with empty array
    sorted = []

    # INFO
    print("+" * level*3 + " Merge: " + str(left) + " + " + str(right))

    # We take first element from left and from right side
    # Then we see which one is smaller and we put it on sorted
    # Until one of the arrays are empty
    while(len(left) > 0 and len(right) > 0):
        if left[0] <= right[0]:
            sorted.append(left.pop(0))
        else:
            sorted.append(right.pop(0))

    # This is here so we can add the remaining values from left and right
    # Remember either left or right is going to be empty
    # And what is left is a high value element
    sorted = sorted + left + right
    
    # Return sorted array
    return sorted

# Call the function and print output
output = sort(input, 0)
print()
print(output)