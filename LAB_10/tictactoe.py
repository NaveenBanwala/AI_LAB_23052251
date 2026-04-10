# Game AI Using Search Algorithms
# Objective: Implement AI to solve a simple turn-based game.
# Problem Statement: Design an AI agent to play a game (e.g., Tic-Tac-Toe or
# Snake and Ladder) using search algorithms.

# Tasks:
# 1. Use BFS and DFS for exploring game states.
# 2. Implement A* Search with a heuristic function to improve efficiency.
# 3. Compare search strategies for different game board configurations.

import heapq
from collections import deque

# Simple TicTacToe Helper
class TicTacToe:

    # check win
    def is_win(self, board, player):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        for a,b,c in wins:
            if board[a]==board[b]==board[c]==player:
                return True
        return False

    # available moves
    def moves(self, board):
        return [i for i in range(9) if board[i]=="."]


game = TicTacToe()

# ---------------- BFS ----------------
def bfs(board, player):
    queue = deque([(board,[])])
    visited=set()

    while queue:
        state,path = queue.popleft()

        if game.is_win(state,player):
            return path[0]

        for m in game.moves(state):
            new=list(state)
            new[m]=player
            new="".join(new)

            if new not in visited:
                visited.add(new)
                queue.append((new,path+[m]))


# ---------------- DFS ----------------
def dfs(board, player):
    stack=[(board,[])]

    while stack:
        state,path = stack.pop()

        if game.is_win(state,player):
            return path[0]

        for m in game.moves(state):
            new=list(state)
            new[m]=player
            new="".join(new)

            stack.append((new,path+[m]))


# ---------------- A* ----------------
def heuristic(board, player):
    # simple heuristic = count of player's marks
    return board.count(player)

def astar(board, player):
    pq=[(0,board,[])]
    visited=set()

    while pq:
        cost,state,path = heapq.heappop(pq)

        if game.is_win(state,player):
            return path[0]

        for m in game.moves(state):
            new=list(state)
            new[m]=player
            new="".join(new)

            h=heuristic(new,player)

            if new not in visited:
                visited.add(new)
                heapq.heappush(pq,(cost-h,new,path+[m]))


# Initial board
# O . .
# . X .
# . . .
start="O...X...."

print("BFS Move:", bfs(start,"X"))
print("DFS Move:", dfs(start,"X"))
print("A* Move :", astar(start,"X"))