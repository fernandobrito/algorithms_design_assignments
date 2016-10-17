"""
    Author: Jorismar Barbosa - 11121191
    Python 3.4.3
    Usage: python kruskal_coding.py

    Resources:
        http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
        https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
        https://www.youtube.com/watch?v=5XkK88VEILk

    Description:
        "Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible
         weight that connects any two trees in the forest.It is a greedy algorithm in graph theory as it 
         finds a minimum spanning tree for a connected weighted graph adding increasing cost arcs at each step. 
         This means it finds a subset of the edges that forms a tree that includes every vertex, where the total 
         weight of all the edges in the tree is minimized. If the graph is not connected, then it finds a minimum spanning forest 
         (a minimum spanning tree for each connected component)." [Wikipedia]

    Complexity: O(ElogE) or O(ElogV)
        Where E is the number of edges and V is the number of vertices.

    Applications:
        "The standard application is to a problem like phone network design. You have a business with several offices; 
        you want to lease phone lines to connect them up with each other; and the phone company charges different 
        amounts of money to connect different pairs of cities. You want a set of lines that connects all your offices with a 
        minimum total cost. It should be a spanning tree, since if a network isn’t a tree you can always remove some edges and 
        save money." [GeeksforGeeks]
"""

from utils import table as table_utils

def solve(input):
    """
    :param input: An array with all graph edges. Each edge follows the format [weight, origin, destination].
    :return: An array with all edges of the minimum spanning tree. Each edge follows the format [weight, origin, destination].
    """

    return _kruskal_minimum_spanning_tree(input, _get_num_vertices(input))

def _kruskal_minimum_spanning_tree(graph, num_verts):
    tree = []
    num_edges = len(graph)
    sorted_graph = sorted(graph, key=lambda tup: tup[0])
    subset = table_utils.initialize(num_verts, 2, 0)
    
    for i in range(num_verts):
        subset[i][0] = i

    for edge in sorted_graph:
        v1 = _find_subset(subset, edge[1])
        v2 = _find_subset(subset, edge[2])
        
        if v1 != v2:
            tree.append(edge)
            _union(subset, v1, v2)
            
        if len(tree) >= num_edges - 1:
            break
    return tree

def _get_num_vertices(graph):
    vertices = []

    for edge in graph:
        if not edge[1] in vertices:
            vertices.append(edge[1])

        if not edge[2] in vertices:
            vertices.append(edge[2])

    return len(vertices)

def _find_subset(subset, elem):
    if subset[elem][0] != elem:
        subset[elem][0] = _find_subset(subset, subset[elem][0])

    return subset[elem][0]

def _union(subset, elem1, elem2):
    v1 = _find_subset(subset, elem1)
    v2 = _find_subset(subset, elem2)

    if subset[v1][1] < subset[v2][1]:
        subset[v1][0] = v2
    elif subset[v1][1] > subset[v2][1]:
        subset[v2][0] = v1
    else:
        subset[v2][0] = v1
        subset[v1][1] += 1 
