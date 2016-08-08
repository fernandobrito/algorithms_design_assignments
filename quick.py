# Author: Fernando Brito
# Python 3,4
# Usage: python3.4 quick.py <input>
# Example: python3.4 quick.py
# Example 2: python3.4 quick.py 3 5 6 1 2 4 3 2

import sys
import common

print("== QUICK SORT ==")

# Read input
array = common.read_input(sys.argv)

print("Input: " + str(array))
print()

# Quick sort:
# Choose pivot, put everyone lower than it on beginning of array
#  and everyone higher than it, at the end
# Hoare partition. Two indexes, from start and end

# Recursive, main call
def quicksort(array, low, high, level=1):
    if low < high:
        level+=1

        # Find partition point
        partition_point = partition(array, low, high)

        print("=" * level*3 + " " + str(array[low:partition_point-1]) + " + " + str(array[partition_point]) + " + " + str(array[partition_point+1:]))

        # Recursive call, splitting array
        quicksort(array, low, partition_point - 1, level)
        quicksort(array, partition_point + 1, high, level)

def partition(array, low, high):
    # Pick first element is pivot
    pivot = array[low]

    # Initialize pointers
    left = low + 1
    right = high

    # Move left pointer to the right and right pointer to the left
    # swapping elements that are greater than the pivot to the right 
    # and smaller to the left
    while True:
        while left <= right and array[left] <= pivot:
            left += 1

        while array[right] >= pivot and right >= left:
            right -= 1

        if right >= left:
            array[left], array[right] = array[right], array[left]
        else:
            break

    # Swap pivot with right pointer
    array[low], array[right] = array[right], array[low]

    return right

# Call the function and print output
quicksort(array, 0, len(array) - 1)
print()
print(array)