import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]  
safe_zone_count = 0

def dfs(x, y):
    global safe_zone_count
    visited[x][y] = 1  

    dx, dy = direction[grid[x][y]]
    nx, ny = x + dx, y + dy

    if visited[nx][ny] == 0: 
        dfs(nx, ny)
    elif visited[nx][ny] == 1: 
        safe_zone_count += 1

    visited[x][y] = 2

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j)

print(safe_zone_count)
