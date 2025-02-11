from collections import deque

def lee_algorithm(grid, start, end):
    """
    Finds the shortest path in a grid using Lee Algorithm (BFS).

    Parameters:
    grid (list): 2D grid with 0 (free cell) and 1 (blocked cell).
    start (tuple): (row, col) of the start position.
    end (tuple): (row, col) of the destination.

    Returns:
    int: The shortest path length, or -1 if no path exists.
    """
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    dr, dc = end

    # If start or end is blocked, return -1
    if grid[sr][sc] == 1 or grid[dr][dc] == 1:
        return -1

    # Directions (Right, Left, Down, Up)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(sr, sc, 0)])  # (row, col, distance)
    visited = set()
    visited.add((sr, sc))

    while queue:
        r, c, dist = queue.popleft()

        # If destination is reached, return distance
        if (r, c) == (dr, dc):
            return dist

        # Explore all 4 possible moves
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                queue.append((nr, nc, dist + 1))
                visited.add((nr, nc))

    return -1  # No path found

# Example usage:
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
start = (0, 0)
end = (3, 3)

print("Shortest Path Length:", lee_algorithm(grid, start, end))
