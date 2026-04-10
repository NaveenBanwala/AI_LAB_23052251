from collections import deque

def bfsMaze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0), (1,0), (0,1), (0,-1)]

    queue = deque()
    queue.append((start[0], start[1], 0))

    visited = set()
    visited.add(start)

    comparisons = 0  # counter

    while queue:
        r, c, dist = queue.popleft()
        comparisons += 1  # count comparison

        if (r, c) == goal:
            return dist, comparisons

        for dr, dc in directions:
            newRow, newCol = r + dr, c + dc

            if (0 <= newRow < rows and
                0 <= newCol < cols and
                maze[newRow][newCol] == 0 and
                (newRow, newCol) not in visited):

                visited.add((newRow, newCol))
                queue.append((newRow, newCol, dist + 1))

    return -1, comparisons
