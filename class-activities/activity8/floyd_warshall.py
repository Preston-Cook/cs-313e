import sys
import math
from collections import defaultdict

def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for finding shortest paths in a weighted, directed graph.

    Parameters:
    graph: Adjacency list representing the graph.

    Returns:
    distance_matrix: Distance matrix containing the shortest distances between all pairs of vertices.
    """
    # You can use sys.maxsize as infinity value. 
    # Initialize distance matrix (a 2d matrix)
    distance_matrix = [[math.inf for _ in range(len(graph))] for _ in range(len(graph))]

    # Initialize distances based on graph
    for i in range(len(graph)):
        distance_matrix[i][i] = 0
        for v, w in graph[i]:
            distance_matrix[i][v] = w

    # Iterate over vertices
    for k in range(len(graph)):
        # Iterate over edges
        for i in range(len(graph)):
            for j in range(len(graph)):
                distance_matrix[i][j] = min(distance_matrix[i][j],distance_matrix[i][k] + distance_matrix[k][j])
    
    return distance_matrix

def main():
    
    # Example Graph
    graph = defaultdict()
    # Our example weighted graph is as follows. 
    # It has 3 vertexes and 5 weighted edges. 

    # 0->1 weight=11
    # 0->2 weight=5
    graph[0] = [(1,11), (2, 5)]
    # 1->3 weight=2
    graph[1] = [(3, 2)]
    # 2->1 weight=4
    # 2->3 weight=6
    graph[2] = [(1, 4), (3, 6)]
    # vertex 3 has no outgoing edge.
    graph[3] = []
    
    
    distance_matrix = floyd_warshall(graph)
    print(distance_matrix)


if __name__ == "__main__":
  main()