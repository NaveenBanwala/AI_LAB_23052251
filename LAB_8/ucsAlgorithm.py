import heapq

# ---------- Path Reconstruction ----------
def reconstruct_path(visited, start, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = visited[current][1]   # parent node

    path.reverse()
    return path


# ---------- Uniform Cost Search ----------
def ucsImplement(graph, start, goal):

    # Priority Queue → (cost, node)
    pq = [(0, start)]

    # visited[node] = (cost, parent)
    visited = {
        start: (0, None)
    }

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        #If goal is reached then return and construct path 
        if current_node == goal:
            return current_cost, reconstruct_path(visited, start, goal)

        # Explore neighbours for 
        for neighbour, cost in graph[current_node]:
            total_cost = current_cost + cost

            if neighbour not in visited or total_cost < visited[neighbour][0]:
                visited[neighbour] = (total_cost, current_node)
                heapq.heappush(pq, (total_cost, neighbour))

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

cost, path = ucsImplement(graph, 'A', 'D')

print("Cost:", cost)
print("Path:", path)
