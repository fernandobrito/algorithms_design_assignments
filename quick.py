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

def quicksort(list, low, high, level=1):
    if low < high:
        level+=1

        partition_point = partition(list, low, high)

        print("=" * level*3 + " " + str(list[low:partition_point-1]) + " + " + str(list[partition_point]) + " + " + str(list[partition_point+1:]))

        quicksort(list, low, partition_point - 1, level)
        quicksort(list, partition_point + 1, high, level)

def partition(list, low, high):
    # Pick first element is pivot
    pivot = list[low]

    left = low + 1
    right = high

    while True:
        while left <= right and list[left] <= pivot:
            left += 1

        while list[right] >= pivot and right >= left:
            right -= 1

        if right >= left:
            list[left], list[right] = list[right], list[left]
        else:
            break

    list[low], list[right] = list[right], list[low]

    return right

# Call the function and print output
quicksort(input, 0, len(input) - 1)
print()
print(input)