# Author: Fernando Brito
# Python 3,4
# Usage: python3.4 selection.py <input>
# Example: python3.4 selection.py 3 5 6 1 2 4 3 2

import sys
import common

print("== SELECTION SORT ==")

# Read input
input = common.read_input(sys.argv)

print("Input: " + str(input))
print()


# Selection sort:
# #1 Find smallest value on entire array, put on index 0
# #2 Find smallest value on what is left, put on index 1...

# For every number in input
for i in range(len(input)):
	# INFO
	print("= Searching smallest on: " + str(input[i:]))

	# Assume number on iis the smallest
	smallest = input[i]
	smallestIndex = i

	# Iterate over what is left from the array to find the real smallest
	for j in range(i, len(input)):

		# If this new element is smaller, update our smallest
		if input[j] < smallest:
			smallest = input[j]
			smallestIndex = j

	# INFO
	print("== Smallest found: " + str(smallest) + " on index " + str(smallestIndex))

	# Swap i and j
	input[smallestIndex] = input[i]
	input[i] = smallest

	# INFO
	print("== New array, after swapping: " + str(input))
	print()

# Print result
print(input)