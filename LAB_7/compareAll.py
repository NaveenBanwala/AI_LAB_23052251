from collections import deque

# -------------------- Maze Definition --------------------

maze = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 1, 1, 1]
]

start = (0, 0)
goal = (3, 3)

directions = [(-1,0), (1,0), (0,-1), (0,1)]


# -------------------- BFS --------------------

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


# -------------------- DFS --------------------

def dfs(maze, current, goal, visited, nodes):
    nodes[0] += 1

    if current == goal:
        return True

    visited.add(current)
    x, y = current

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] == 1 and (nx, ny) not in visited:
                if dfs(maze, (nx, ny), goal, visited, nodes):
                    return True

    return False


# -------------------- DLS (for IDDFS) --------------------

def dls(maze, current, goal, depth, visited, nodes):
    nodes[0] += 1

    if current == goal:
        return True

    if depth == 0:
        return False

    visited.add(current)
    x, y = current

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] == 1 and (nx, ny) not in visited:
                if dls(maze, (nx, ny), goal, depth - 1, visited, nodes):
                    return True

    visited.remove(current)   # backtracking
    return False


# -------------------- IDDFS --------------------

def iddfs(maze, start, goal):
    max_depth = len(maze) * len(maze[0])
    nodes = [0]

    for depth in range(max_depth):
        visited = set()
        if dls(maze, start, goal, depth, visited, nodes):
            return True, depth, nodes[0]

    return False, -1, nodes[0]


# -------------------- Run All Algorithms --------------------

bfs_found, bfs_nodes = bfs(maze, start, goal)

dfs_nodes = [0]
dfs_found = dfs(maze, start, goal, set(), dfs_nodes)

iddfs_found, iddfs_depth, iddfs_nodes = iddfs(maze, start, goal)


# -------------------- Output --------------------

print("Maze Solver Results\n")

print("BFS:")
print("  Goal Found:", bfs_found)
print("  Nodes Explored:", bfs_nodes)

print("\nDFS:")
print("  Goal Found:", dfs_found)
print("  Nodes Explored:", dfs_nodes[0])

print("\nIDDFS:")
print("  Goal Found:", iddfs_found)
print("  Depth Found:", iddfs_depth)
print("  Nodes Explored:", iddfs_nodes)
