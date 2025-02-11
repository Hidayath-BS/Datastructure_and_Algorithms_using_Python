def bellman_ford(vertices, edges, source):
    """
    Finds the shortest paths from a single source using Bellman-Ford Algorithm.

    Parameters:
    vertices (int): Number of vertices.
    edges (list): List of edges (u, v, weight).
    source (int): The starting node.

    Returns:
    dict: Shortest distances from source to all nodes or a cycle detection message.
    """
    distances = {v: float('inf') for v in range(vertices)}
    distances[source] = 0

    # Step 1: Relax edges |V| - 1 times
    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Step 2: Check for negative weight cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return "Graph contains a negative weight cycle!"

    return distances

# Example usage:
edges = [
    (0, 1, 4), (0, 2, 1), (1, 3, 1),
    (2, 1, 2), (2, 3, 5), (3, 4, 3),
    (4, 2, -10)  # Negative weight cycle
]
vertices = 5
source = 0
result = bellman_ford(vertices, edges, source)

print("Shortest distances from source:", result)
