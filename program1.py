
def count_islands(map_grid):
    if not map_grid:
        return 0

    rows = len(map_grid)
    cols = len(map_grid[0])
    visited = [[False] * cols for _ in range(rows)]
   
    def dfs(r, c):
        # If out of bounds or at water or already visited, return
        if r < 0 or r >= rows or c < 0 or c >= cols or map_grid[r][c] == 'W' or visited[r][c]:
            return
        
        visited[r][c] = True
        # Visit all connected land cells (4 directions)
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
   
    island_count = 0
    for i in range(rows):
        for j in range(cols):
            if map_grid[i][j] == 'L' and not visited[i][j]:
                # New island found
                island_count += 1
                dfs(i, j)  # Visit all connected land masses
   
    return island_count


dispatch1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

dispatch2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]
dispatch3 = [
        ["W", "W", "W", "W"],
        ["W", "L", "L", "W"], 
        ["W", "L", "L", "W"],
        ["W", "W", "W", "W"],

]

print(count_islands(dispatch1)) 
print(count_islands(dispatch2))  
print(count_islands(dispatch3))

