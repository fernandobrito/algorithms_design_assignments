"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python huffman_coding.py

    Resources:
        http://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/
        https://en.wikipedia.org/wiki/Huffman_coding
        http://www.cprogramming.com/tutorial/computersciencetheory/huffman.html

    Description:
        A algorithm for the lossless compression of files based on the frequency of occurrence of a symbol in the
        file that is being compressed. The Huffman algorithm is based on statistical coding, which means that the
        probability of a symbol has a direct bearing on the length of its representation. The more probable the
        occurrence of a symbol is, the shorter will be its bit-size representation.

    Complexity: O(nlogn * n)
        Where n is the number of unique characters and O(nlogn) is the complexity ins the average case performance
        to build each internal node in the three. Still there is a additional complexity O(logn) to traverse the
        tree and assign the codes. So, overall complexity is O(nlogn * n).

    Applications:
        Huffman is widely used in all the mainstream compression formats that you might encounter - from GZIP,
        PKZIP (winzip etc) and BZIP2, to image formats such as JPEG and PNG.

        http://www.wikihow.com/Compress-Data-Using-Huffman-Encoding
        http://web.stanford.edu/class/archive/cs/cs106b/cs106b.1126/handouts/220%20Huffman%20Encoding.pdf
        http://www.compressconsult.com/huffman/
        https://en.wikipedia.org/wiki/Huffman_coding
"""


def solve(input):
    """
    :param input:   array with first element: symbol list (should be non-empty), second element: list
                    contains the respective symbols frequency (should be non-empty and the same length
                    of the symbol list).
                                ex: [['a', 'b', 'c', 'd', 'e'], [24, 12, 10, 8, 8]]

    :return:        array that contain the inserted symbols and their respective huffman code (sorted by
                    alphabetical order of the symbols)
                                ex: [['a', '0'], ['b', '111'], ['c', '110'], ['d', '100'], ['e', '101']]
    """
    return _huffman_coding(input[0], input[1])


def _huffman_coding(symbols, frequencies):
    if len(symbols) == 0 or len(frequencies) == 0:
        return "Empty lists are not accepted"

    if len(symbols) != len(frequencies):
        return -1

    return _traverse_huffman_tree(_build_huffman_tree(_create_leafs(symbols, frequencies)))


class Node(object):
    def __init__(self, value, frequency, left=None, right=None):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right
        self.code = ""


# Traverse the Huffman Tree and assign codes to characters
def _traverse_huffman_tree(root):
    current_level = [root]
    codes = []

    while current_level:
        next_level = []

        for node in current_level:

            if str(node.value) != '$':
                codes.append([node.value, node.code])
            if node.left:
                node.left.code = node.code + "0"
                next_level.append(node.left)
            if node.right:
                node.right.code = node.code + "1"
                next_level.append(node.right)

        current_level = next_level

    return sorted(codes, key=lambda code: code[0])

# Build a Huffman Tree through leaf list
def _build_huffman_tree(huffman_tree):

    while len(huffman_tree) > 1:
        huffman_tree = sorted(huffman_tree, key=lambda node: node.frequency)

        # Extract two nodes with the minimum frequency from
        min1 = huffman_tree.pop(0)
        min2 = huffman_tree.pop(0)

        # Create a new internal node with frequency equal to the sum of the two nodes
        # frequencies. Make the first extracted node as its left child and the other extracted
        # node as its right child. Add this node to the min heap.
        huffman_tree.append(Node("$", min1.frequency + min2.frequency, min1, min2))

    return huffman_tree.pop(0)


# Create a leaf node for each unique character
def _create_leafs(symbols, frequencies):
    leaf_list = []

    for i in range(len(symbols)):
        leaf_list.append(Node(symbols[i], frequencies[i]))

    return leaf_list

