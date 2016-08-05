import random

# Remove first element from list and convert elements to integers
def read_input(argv):
    # Process arguments, removing first element (filename)
    input = argv[1:]

    # Check size
    if (len(input) == 0):
        print("No input given. Using 10 random numbers")
        input = random.sample(range(1, 100), 10)

    # Convert values from string to integer
    return list(map(int, input))