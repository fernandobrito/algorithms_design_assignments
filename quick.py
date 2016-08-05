# Author: Fernando Brito
# Python 3,4
# Usage: python3.4 quick.py <input>
# Example: python3.4 quick.py 3 5 6 1 2 4 3 2

import sys
import common

print("== QUICK SORT ==")

# Read input
input = common.read_input(sys.argv)

print("Input: " + str(input))
print()

# Quick sort:
# Choose pivot, put everyone lower than it on beginning of array
#  and everyone higher than it, at the end
# Hoare partition. Two indexes, from start and end

def quicksort(list, low, high):
    if high > low:
        # Pick first element is pivot
        pivot = list[low]
        left = low
        right = high

        # INFO
        print("== Partitionate: " + str(list[low:high+1]))

        # While the indexes have not match
        while left <= right:
            while list[left] < pivot:
                left += 1   

            while list[right] > pivot:
                right -= 1

            # Swap elements
            if left <= right:
                print("===    Swapping: " + str(list[left]) + " and " + str(list[right]))
                list[left], list[right] = list[right], list[left]
                left += 1
                right -= 1

        print("==         Done: " + str(list[low:high+1]))
        print()

        # Recursion
        quicksort(list, low, right)
        quicksort(list, left, high)

# Call the function and print output
quicksort(input, 0, len(input) - 1)
print()
print(input)