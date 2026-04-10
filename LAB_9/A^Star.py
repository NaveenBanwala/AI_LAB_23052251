import heapq

GOAL = [[1,2,3],
        [4,5,6],
        [7,8,0]]


def state_to_tuple(state):
    return tuple(tuple(row) for row in state) #Because tuples are immutabke ,ordered and collection of elements

def h1_misplaced(state):
    count = 0

    for i in range(3):
        for j in range(3):

            if state[i][j] != 0 and state[i][j] != GOAL[i][j]:
                count += 1

    return count


def h2_manhattan(state):
    dist = 0

    for i in range(3):
        for j in range(3):

            val = state[i][j]

            if val != 0:
                goal_x = (val-1)//3
                goal_y = (val-1)%3

                dist += abs(i-goal_x) + abs(j-goal_y)

    return dist


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []

    x, y = find_blank(state)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x+dx, y+dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = \
            new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors


def astar(start, heuristic):
    pq = []
    visited = set()
    g_cost = {}

    start_tuple = state_to_tuple(start)

    g_cost[start_tuple] = 0

    heapq.heappush(pq,
        (heuristic(start), 0, start))
    
    nodes_explored = 0

    while pq:

        f, g, current = heapq.heappop(pq)
        nodes_explored += 1

        if current == GOAL:
            return g, nodes_explored

        visited.add(state_to_tuple(current))

        for neighbor in get_neighbors(current):

            t = state_to_tuple(neighbor)

            if t in visited:
                continue

            new_g = g + 1
            h = heuristic(neighbor)
            f = new_g + h

            if t not in g_cost or new_g < g_cost[t]:

                g_cost[t] = new_g

                heapq.heappush(pq,
                    (f, new_g, neighbor))

    return -1, nodes_explored


start =[[1,2,3],
        [4,0,5],
        [6,7,8]]

depth1, nodes1 = astar(start, h1_misplaced)
depth2, nodes2 = astar(start, h2_manhattan)

print("BY Misplaced tiles")
print("Solution Depth:", depth1)
print("Nodes Explored:", nodes1)

print("BY Manhattan Distance" )
print("Solution Depth:", depth2)
print("Nodes Explored:", nodes2)


