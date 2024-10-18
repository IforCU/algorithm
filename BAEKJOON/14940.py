from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
maps = [[0 for _ in range(M)] for _ in range(N)]
goal = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(N):
    line = list(map(int, input().rstrip().split()))
    graph[i] = line
    for j in range(M):
        if line[j] == 2:
            goal.append(j)
            goal.append(i)

def bfs(a,b):
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((a,b))
    visited[b][a] = True

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx]:
                    queue.append((nx,ny))
                    maps[ny][nx] = maps[y][x] + 1
                    visited[ny][nx] = True
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                maps[i][j] = -1


bfs(goal[0], goal[1])

for i in maps:
    print(*i)