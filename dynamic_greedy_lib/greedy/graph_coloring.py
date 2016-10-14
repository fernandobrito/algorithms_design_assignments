"""
Find a way of coloring the vertices of a *undirected* graph such that no
two adjacent vertices are colored using same color.

"This problem is a known NP Complete problem. This solution doesn’t guarantee
to use minimum colors, but it guarantees an upper bound on the number of colors.
The basic algorithm never uses more than d+1 colors where d is the maximum
degree of a vertex in the given graph."

Applications:
    "The problem of coloring a graph arises in many practical areas such
    as pattern matching, sports scheduling, designing seating plans, exam
    timetabling, the scheduling of taxis, and solving Sudoku puzzles.

    Vertex coloring models to a number of scheduling problems. For example,
    when assigning aircraft to flights, the resulting conflict graph is an
    interval graph, so the coloring problem can be solved efficiently. In
    bandwidth allocation to radio stations, the resulting conflict graph
    is a unit disk graph, so the coloring problem is 3-approximable." [Wikipedia]

Complexity: O(V^2 + E)
    Where V is the number of vertices and E the number of edges

Author: Fernando Brito (11111309)

Resources:
    - http://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
"""

def solve(input):
    """
    :param input: array with first element: number of vertices (should be at least 1)
                  second element: array of arrays with 2 elements, representing edges
                                  ex: [[0, 2], [0, 3], ...]
    :return: array where i-th element is number of color of i-th vertex
    """

    # Store number of vertices
    number_of_vertices = input[0]

    # Create array of V vertices. Each element is an array of which vertices
    # have edges to current vertex
    edges = [[] for _ in range(number_of_vertices)]

    # Parse input and store it using adjacency list
    _parse_input(edges, input[1])

    # Call main routine
    return _coloring(number_of_vertices, edges)


def _coloring(number_of_vertices, edges):
    # Array storing color number (int) for i-th vertex
    result = [None for _ in range(number_of_vertices)]

    # Assign first color to first vertex
    result[0] = 0

    # Temporary array to store used colors.
    # True means color has been used on one of its
    # adjacent vertices
    colors_used = [False for _ in range(number_of_vertices)]

    # Iterate over all remaining vertices
    for vertex in range(1, number_of_vertices):
        # Process adjacent vertices and mark their colors
        # as used
        for adjacent_vertex in edges[vertex]:
            color_of_adjacent_vertex = result[adjacent_vertex]

            if color_of_adjacent_vertex is not None:
                colors_used[color_of_adjacent_vertex] = True

        # Find the first available color
        for color_index in range(len(colors_used)):
            if colors_used[color_index] == False:
                color = color_index
                break

        # Assign this color to current vertex
        result[vertex] = color

        # Reset temporary array of used colors
        colors_used = [False for _ in range(number_of_vertices)]

    return result


def _parse_input(edges, input):
    # For each pair of vertices on input
    for edge in input:
        source = edge[0]
        destination = edge[1]

        # Store it on edges array
        edges[source].append(destination)
        edges[destination].append(source)