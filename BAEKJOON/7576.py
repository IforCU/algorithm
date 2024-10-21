from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def contains_zero(arr):
    for row in arr:
        if 0 in row:
            return True
    return False

def find_max_value(arr):
    max_value = float('-inf')
    for row in arr:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value

def bfs():
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque()

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                queue.append((x,y))
                visited[y][x] = True
            elif graph[y][x] == -1:
                visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx]:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((nx, ny))
                    visited[ny][nx] = True
    
    if contains_zero(graph):
        return False
    else:
        return True

if bfs():
    print(find_max_value(graph) - 1)
else:
    print(-1)