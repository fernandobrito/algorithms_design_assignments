def read_input():
    array = []

    size = int(input())

    for i in range(size):
        array.append(int(input()))

    return array

def print_output(array):
    for element in array:
        print(element)