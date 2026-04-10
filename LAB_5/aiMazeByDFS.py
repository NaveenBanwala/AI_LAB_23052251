
def dfsMaze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    visited = set()

    def dfs(r, c, dist):
        if (r,c)== goal:
            return dist
        
        visited.add((r, c))

        for dr, dc in directions:
            newRow, newCol = r + dr, c + dc

            if (0 <= newRow < rows and
                0 <= newCol < cols and
                maze[newRow][newCol] == 0 and
                (newRow, newCol) not in visited):

                result = dfs(newRow, newCol ,dist+1)
                if result != -1 :
                    return result
                

        return -1 #backtrack
    return dfs(start[0],start[1],0)



maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,1],
    [1,1,0,0,0],
    ]

start =(0,0) 
goal =(3,2)

print(f"Distance from start{start} to goal{goal}" , dfsMaze(maze, start, goal))