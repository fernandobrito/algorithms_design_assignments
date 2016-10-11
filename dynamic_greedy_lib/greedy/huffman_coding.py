"""
    Author: Jaelson Carvalho - 11427671
    Python 3.4.3
    Usage: python huffman_coding.py
    Resources:
        http://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/

    Description:

    Complexity:

    Application:
"""


def solve(input):
    """
    Input : should contain a symbols list and another list contains their respective frequency
    Output : a list that contain symbols and their respective huffman code
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


def _build_huffman_tree(huffman_tree):

    while len(huffman_tree) > 1:
        huffman_tree = sorted(huffman_tree, key=lambda node: node.frequency)
        min1 = huffman_tree.pop(0)
        min2 = huffman_tree.pop(0)
        huffman_tree.append(Node("$", min1.frequency + min2.frequency, min1, min2))

    return huffman_tree.pop(0)


def _create_leafs(symbols, frequencies):
    leafs_list = []

    for i in range(len(symbols)):
        leafs_list.append(Node(symbols[i], frequencies[i]))

    return leafs_list

