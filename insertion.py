# Author: Fernando Brito
# Python 3,4
# Usage: python3.4 insertion.py <input>
# Example: python3.4 insertio.py 3 5 6 1 2 4 3 2

import sys
import common

print("== INSERTION SORT ==")

# Read input
input = common.read_input(sys.argv)

print("Input: " + str(input))
print()

# Insertion sort:
# "Insertion sort iterates, consuming one input element each repetition, and growing a 
#  sorted output list. Each iteration, insertion sort removes one element from the input
#  data, finds the location it belongs within the sorted list, and inserts it there. It 
#  repeats until no input elements remain." (Wikipedia)

# For every number on input (expect for the first one, since array with 1 element
# is trivially sorted):
for i in range(1, len(input)):
    # Auxiliary index to iterate from position i to beginning of array
    j = i - 1

    # Store current value
    current_value = input[i]

    # INFO
    print("== Assuming " + str(input[0:i]) + ' is already sorted')
    print("== Looking where to put element: " + str(current_value))

    # Starting from i, we go backwards in the array (which is already sorted)
    # looking where to insert input[i]. While we do this, we shift elements
    # to the right. 
    while (j >= 0 and input[j] > current_value):
        input[j+1] = input[j]
        j -= 1

    # Not that we found where to put the current value, we do it
    input[j+1] = current_value

    print("== New array: " + str(input[0:i+1]))
    print()

# Print result
print(input)