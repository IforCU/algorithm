from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
maze = [[0] for _ in range(N)]
for i in range(N):
    maze[i] = list(map(int, input().rstrip()))

def bfs():
    visited = [[False for _ in range(M)] for _ in range(N)]
    maps_count = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    maps_count[0][0] = 1
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 0:
                visited[i][j] = True
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx]:
                    if maze[ny][nx] == 1:
                        queue.append((nx,ny))
                        visited[ny][nx] = True
                        maps_count[ny][nx] = maps_count[y][x] + 1
                if ny == (N-1) and nx == (M-1):
                    return maps_count[y][x] + 1
            
print(bfs())