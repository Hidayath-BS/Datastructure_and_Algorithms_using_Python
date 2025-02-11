from collections import deque

def kahn_topological_sort(vertices, edges):
    """
    Finds the topological order of a DAG using Kahn’s Algorithm (BFS-based).

    Parameters:
    vertices (int): Number of vertices.
    edges (list): List of edges (u, v) where u → v.

    Returns:
    list: A topological ordering of vertices or an error if a cycle exists.
    """
    # Step 1: Compute in-degree of all vertices
    in_degree = {i: 0 for i in range(vertices)}
    adj_list = {i: [] for i in range(vertices)}

    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    # Step 2: Add all vertices with in-degree = 0 to the queue
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    topo_sort = []

    while queue:
        node = queue.popleft()
        topo_sort.append(node)

        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: Check if all vertices are processed (DAG verification)
    if len(topo_sort) != vertices:
        return "Graph contains a cycle, topological sorting is not possible!"

    return topo_sort

# Example usage:
edges = [(5, 0), (5, 2), (2, 3), (3, 1), (4, 1), (4, 0)]
vertices = 6
print("Topological Sort (Kahn's Algorithm):", kahn_topological_sort(vertices, edges))




################# using stack
def dfs_topological_sort(vertices,edges):
    adj_list = {i:[] for i in range(vertices)}
    for u,v in edges:
        adj_list[u].append(v)
    visited = set()
    stack = []
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adj_list[node]:
            dfs(neighbor)
        stack.append(node)
    for v in range(vertices):
        if v not in visited:
            dfs(v)
    return stack[::-1]
print("topological sort(dfs)",dfs_topological_sort(vertices, edges))