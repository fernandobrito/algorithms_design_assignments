from utils import table as table_utils

"""
Given a graph and a source vertex in graph, find shortest paths from source to all vertices in the given graph.

Complexity: O(V^2)
    Where V is the number of vertices.
    We spend O(V) 2 times to initialize arrays and then we have
    two nested loops that iterate over all vertices

Author: Fernando Brito (11111309)

Resources:
    - http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
"""

def solve(input):
    """
    :param input: array with first element: index of source vertex
                  and second element:  adjacency matrix (use None to mark absence of edges)
    :return: array with shortest distance from source to each vertex i
    """

    return _dijkstra(input[0], input[1])


def _dijkstra(source, input):
    # Extract number of vertices from square adjacency matrix
    number_of_vertices = len(input)

    # Result array with shortest distance from src to i
    # Initialized with infinite value and source with 0
    # (table.initialize returns 2d array. we want only row 0)
    distances = table_utils.initialize(1, number_of_vertices, float("inf"))[0]
    distances[source] = 0

    # Array to keep track which vertices were already marked as seen
    # Initialized with False
    # (table.initialize returns 2d array. we want only row 0)
    vertices_processed = table_utils.initialize(1, number_of_vertices, False)[0]

    # For every vertex
    for _ in range(number_of_vertices):
        # Choose the vertex with minimum distance to source and that
        # has not been finalized yet. Note that on first iteration,
        # source will be chosen
        vertex = _shortest_distance(distances, vertices_processed)

        # Mark it as processed
        vertices_processed[vertex] = True

        # Update distances of all adjacent vertices
        # to the chosen vertex
        for a_vertex in range(number_of_vertices):

            # Only update if (1) a_vertex hasn't be processed
            # (2) there is an edge from vertex to a_vertex and
            # (3) it's worth updating (distance from source to
            # a_vertex through vertex is small than current distance
            # to a_vertex)
            if vertices_processed[a_vertex] == False and \
                    input[vertex][a_vertex] is not None and \
                    distances[vertex] + input[vertex][a_vertex] < distances[a_vertex]:
                distances[a_vertex] = distances[vertex] + input[vertex][a_vertex]

    return distances


def _shortest_distance(distances, vertices_finalized):
    # Initialize variables to keep track of minimum vertex
    minimum_value = float("inf")
    minimum_index = -1

    # For each vertex
    for vertex in range(len(vertices_finalized)):

        # If it has not be seen and has smaller distance,
        # update values
        if vertices_finalized[vertex] == False and distances[vertex] <= minimum_value:
            minimum_value = distances[vertex]
            minimum_index = vertex

    # Return index of vertex
    return minimum_index
