from collections import deque

# Utility function to print the board
def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()

# Check if the current state is the goal state
def is_goal(board, goal):
    return board == goal

# Generate possible moves from the current state
def get_neighbors(board):
    neighbors = []
    rows, cols = len(board), len(board[0])
    
    # Find the position of the blank space (0)
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                x, y = i, j
                break
    
    # Possible moves: up, down, left, right
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    for move in moves:
        new_x, new_y = move
        if 0 <= new_x < rows and 0 <= new_y < cols:
            # Swap the blank space with the adjacent tile
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            neighbors.append(new_board)
    
    return neighbors

# BFS to solve the 8-puzzle problem
def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    visited.add(tuple(tuple(row) for row in start))
    
    while queue:
        current_board, path = queue.popleft()
        
        if is_goal(current_board, goal):
            return path
        
        for neighbor in get_neighbors(current_board):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Test the BFS implementation
start = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

result = bfs(start, goal)

if result:
    print("Solution found!")
    for step in result:
        print_board(step)
else:
    print("No solution exists.")
