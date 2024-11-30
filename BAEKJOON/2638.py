from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0

def contains_one(arr):
    return any(1 in row for row in arr)

def bfs():
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    air = [[False] * M for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        air[x][y] = True

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and cheese[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return air

while contains_one(cheese):
    melt = []
    air = bfs()

    for y in range(N):
        for x in range(M):
            if cheese[y][x] == 1:
                count = 0
                for dx, dy in direction:
                    ny = y + dy
                    nx = x + dx

                    if air[ny][nx]:
                        count += 1
                if count >= 2:
                    melt.append((x, y))
    
    if melt:
        for x, y in melt:
            cheese[y][x] = 0
        ans += 1    

print(ans)