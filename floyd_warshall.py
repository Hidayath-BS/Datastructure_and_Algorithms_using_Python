def floyd_warshall(graph):
    """
    Finds the shortest paths between all pairs of vertices using Floyd-Warshall Algorithm.

    Parameters:
    graph (list): Adjacency matrix representation of the graph.

    Returns:
    list: The shortest distance matrix.
    """
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]  # Copy initial graph

    # Step 2: Update distances using each vertex as an intermediate node
    for k in range(V):  # Intermediate vertex
        for i in range(V):  # Source vertex
            for j in range(V):  # Destination vertex
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Step 3: Check for negative weight cycles
    for i in range(V):
        if dist[i][i] < 0:
            return "Graph contains a negative weight cycle!"

    return dist

# Example usage:
INF = float('inf')
graph = [
    [0, 3, INF, INF, INF, INF],
    [INF, 0, 1, INF, INF, INF],
    [INF, INF, 0, 7, INF, 2],
    [INF, INF, INF, 0, INF, 3],
    [INF, INF, INF, 2, 0, INF],
    [INF, INF, INF, INF, 1, 0]
]

shortest_paths = floyd_warshall(graph)

print("All-Pairs Shortest Paths:")
for row in shortest_paths:
    print(row)
