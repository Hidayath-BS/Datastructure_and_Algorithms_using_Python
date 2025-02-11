def flood_fill(image, sr, sc, new_color):
    """
    Performs flood fill on a given image grid using DFS.

    Parameters:
    image (list): 2D grid representing an image.
    sr (int): Starting row.
    sc (int): Starting column.
    new_color (int): New color to be applied.

    Returns:
    list: The updated image.
    """
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == new_color:
        return image  # Avoid infinite loop

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != original_color:
            return

        image[r][c] = new_color  # Fill the pixel
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    dfs(sr, sc)
    return image

# Example usage:
image = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]
start_row, start_col = 1, 1
new_color = 2

filled_image = flood_fill(image, start_row, start_col, new_color)

print("Updated Image:")
for row in filled_image:
    print(row)


################ queue approch
from collections import deque

def flood_fill_bfs(image, sr, sc, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == new_color:
        return image

    queue = deque([(sr, sc)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    while queue:
        r, c = queue.popleft()
        image[r][c] = new_color

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                queue.append((nr, nc))

    return image

# Example usage:
filled_image_bfs = flood_fill_bfs(image, start_row, start_col, new_color)
print("Updated Image (BFS):")
for row in filled_image_bfs:
    print(row)
