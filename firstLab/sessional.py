

maze = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 1, 1, 1]
]

start = (0, 0)
goal = (3, 3)

directions = [(-1,0), (1,0), (0,-1), (0,1)]


def bfs(maze, start, goal):
    queue = deque([start])
    visited = set([start])
    nodes = 0

    while queue:
        x, y = queue.popleft()
        nodes += 1

        if (x, y) == goal:
            return True, nodes

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return False, nodes