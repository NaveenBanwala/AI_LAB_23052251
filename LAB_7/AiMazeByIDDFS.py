# Objective: Implement IDDFS to solve a maze.
# Problem Statement: Given a grid-based maze where 0 represents walls and 1
# represents walkable paths, find the shortest path from a start cell to an end
# cell.
# Tasks:
# • Use IDDFS to find the shortest path.
# • Compare the number of nodes explored by BFS, DFS, and IDDFS.
# • Take the same example graph and give a conclusion in your own words
# on which algorithm is best and why.



# def dls(maze, current, goal, depth, visited, nodes):
#     nodes[0] += 1

#     if current == goal:
#         return True

#     if depth == 0:
#         return False

#     x, y = current
#     visited.add(current)

#     for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
#             if maze[nx][ny] == 1 and (nx, ny) not in visited:
#                 if dls(maze, (nx, ny), goal, depth - 1, visited, nodes):
#                     return True

#     visited.remove(current)
#     return False


# def iddfs(maze, start, goal):
#     max_depth = len(maze) * len(maze[0])
#     nodes = [0]

#     for depth in range(max_depth):
#         visited = set()
#         if dls(maze, start, goal, depth, visited, nodes):
#             return True, depth, nodes[0]

#     return False, -1, nodes[0]

maze = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 1, 1, 1]
]

start = (1, 3)
goal = (3, 3)


def dls(maze, current, goal,depth, visited,node):
    node[0] += 1

    if current == goal:
        return True

    if depth == 0:
        return False
    
    x,y = current
    visited.add(current)
    for dx, dy in [(0,1),(-1,0),(0,-1),(1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] == 1 and (nx, ny) not in visited:
                if dls(maze, (nx, ny), goal, depth - 1, visited, node):
                    return True
                
    visited.remove(current)
    return False


def iddfs(maze, start,goal):
    max_depth = len(maze) * len(maze[0])
    node=[0]

    for depth in range(max_depth):
        visited = set()
        if dls(maze, start, goal,depth,visited, node) :
            return True , depth, node[0]

    return False,-1, node[0]





found, depth, explored_nodes = iddfs(maze, start, goal)

print("Goal Found:", found)
print("Depth at which goal found:", depth)
print("Total nodes explored:", explored_nodes)

