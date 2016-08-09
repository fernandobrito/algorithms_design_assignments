# Author: Fernando Brito
# Based on: http://www.codecodex.com/wiki/Heapsort#Python
# Python 3,4
# Usage: python3.4 heap.py <input>
# Example: python3.4 heap.py
# Example 2: python3.4 heap.py 3 5 6 1 2 4 3 2

import sys
import common

print("== SELECTION SORT ==")

# Read input
array = common.read_input(sys.argv)

print("Input: " + str(array))
print()

# Maintain the heap invariant: parents must be greater than children
# We go down the heap (represented on an array)
# If any of the children is greater than the parent, swap them
# and continue, recursively
def siftdown(array, root, size):  
  left = 2 * root + 1  
  right = 2 * root + 2  
  largest = root  

  if left <= (size - 1) and array[left] > array[root]:  
    largest = left  

  if right <= (size - 1) and array[right] > array[largest]:  
    largest = right  

  if largest != root:  
    array[root], array[largest] = array[largest], array[root] 
    siftdown(array, largest, size)  

# Convert input (array) into heap (tree)
# Start from the half to the start. Why half?
# Because it's useless to call Heapify on the leaves
def heapify(array, size):  
  p = int(size / 2) - 1  

  while p >= 0:   
    siftdown(array, p, size)  
    p -= 1  

# Main function
# Take the input, heapify it
# Take the root of the tree (max), put it in the end
# Call siftdown to keep heap valid
# Repeat
def heapsort(array):          
  size = len(array)    

  heapify(array, size)  
  end = size - 1  

  while(end > 0):
    array[0], array[end] = array[end], array[0]        
    siftdown(array, 0, end)  
    end -= 1



# Call the function and print output
heapsort(array)
print()
print(array)