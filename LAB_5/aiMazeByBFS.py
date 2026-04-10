# import collections
# from collections import deque

# def bfsMaze(maze, start, goal):

#     rows ,cols = len(maze), len(maze[0])
#     #Upper, Down, Left ,Right
#     directions = [(-1,0), (1,0), (0,-1), (0,1)]
#     dq = deque()

#     #row, col, distance
#     dq.append((start[0], start[1], 0))

#     visited = set()
#     visited.add(start)

#     while dq :
#         r, c, dist = dq.popleft()

#         if(r,c) == goal :
#             return dist
        
#         for dr,dc in directions :
#             #here i take nc and nr as new col and new row
#             nr, nc = r + dr, c + dc

#             if( 0<=nr< rows and 0<=nc<cols and maze[nr][nc]== 0 and (nr,nc) not in visited ):
#                 visited.add((nr, nc))
#                 dq.append((nr, nc, dist + 1))
    
#     return -1



# maze = [
#     [0,1,0,0,0],
#     [0,1,0,1,0],
#     [0,0,0,1,1],
#     [1,1,0,1,0],
#     ]
# start =(1,0) 
# goal =(3,4)

# print("Distance " , bfsMaze(maze, start, goal))


from collections import deque

def bfsMaze(maze, start,goal):
    rows,cols = len(maze), len(maze[0])

    queue = deque()

    directions = [(-1,0), (1,0),(0,1),(0,-1)]

    queue.append((start[0], start[1], 0))

    vis = set()
    vis.add(start)
    

    while queue:
        r , c ,dist =queue.popleft() 

        if ( r,c)==goal :
            return dist
        
        for dr, dc in directions:
            newRow, newCol = r + dr , c + dc

            if(0<=newRow<rows and  0<=newCol < cols and (newRow, newCol) not in vis and maze[newRow][newRow] == 0):
                vis.add((newRow, newCol))
                queue.append((newRow, newCol, dist +1))
    return -1            


maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,1],
    [1,1,0,0,0],
    ]
start =(1,0) 
goal =(3,2)

print(f"Distance from start{start} to goal{goal}" , bfsMaze(maze, start, goal))








