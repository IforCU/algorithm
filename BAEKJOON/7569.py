from collections import deque
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())
graph = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
dz = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]

def contains_zero(arr):
    for layer in arr:
        for row in layer:
            if 0 in row:
                return True
    return False

def find_max_value(arr):
    max_value = float('-inf')
    for layer in arr:
        for row in layer:
            for value in row:
                if value > max_value:
                    max_value = value
    return max_value

def bfs():
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
    queue = deque()
    
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] == 1:
                    queue.append((x,y,z))
                    visited[z][y][x] = True
                elif graph[z][y][x] == -1:
                    visited[z][y][x] = True
    
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if not visited[nz][ny][nx]:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append((nx,ny,nz))
                    visited[nz][ny][nx] = True
    
    if contains_zero(graph):
        return False
    else:
        return True

if bfs():
    print(find_max_value(graph)-1)
else:
    print(-1)