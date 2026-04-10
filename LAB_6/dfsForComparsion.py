def dfsMaze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    visited = set()
    comparisons = 0   # counter

    def dfs(r, c, dist):
        nonlocal comparisons
        comparisons += 1   # count comparison

        if (r, c) == goal:
            return dist
        
        visited.add((r, c))

        for dr, dc in directions:
            newRow, newCol = r + dr, c + dc

            if (0 <= newRow < rows and
                0 <= newCol < cols and
                maze[newRow][newCol] == 0 and
                (newRow, newCol) not in visited):

                result = dfs(newRow, newCol, dist + 1)
                if result != -1:
                    return result

        return -1  # backtrack

    distance = dfs(start[0], start[1], 0)
    return distance, comparisons


maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,1],
    [1,1,0,0,0],
]

start = (0,0)
goal = (3,2)

dfs_dist, dfs_comp = dfsMaze(maze, start, goal)
bfs_dist, bfs_comp = bfsMaze(maze, start, goal)

print("DFS → Distance:", dfs_dist, "Comparisons:", dfs_comp)
print("BFS → Distance:", bfs_dist, "Comparisons:", bfs_comp)
