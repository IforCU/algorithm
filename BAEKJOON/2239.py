import sys
input = sys.stdin.readline
board = []
for _ in range(9):
    board.append(list(map(int, input().strip())))

empty = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_valid(x, y, num):
    for i in range(9):
        if board[x][i] == num:
            return False
        
    for i in range(9):
        if board[i][y] == num:
            return False
    
    square_x, square_y = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if board[square_x + i][square_y + j] == num:
                return False
    return True

def dfs(idx=0):
    if idx == len(empty):  
        return True

    x, y = empty[idx]  
    for num in range(1, 10):  
        if is_valid(x, y, num): 
            board[x][y] = num  
            if dfs(idx + 1):  
                return True
            board[x][y] = 0 
    return False

dfs()

for row in board:
    print(''.join(map(str, row)))
