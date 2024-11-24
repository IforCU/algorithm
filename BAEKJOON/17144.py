from collections import deque
import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

directions = [(0,1), (0,-1), (1,0), (-1, 0)]

ap = []

for a in range(R):
    if graph[a][0] == -1:
        ap.append(a)

def spread():
    queue = deque()
    for y in range(R):
        for x in range(C):
            if graph[y][x] > 0:  
                queue.append((y, x, graph[y][x]))

    while queue:
        y, x, amount = queue.popleft()
        spread_amount = amount // 5  
        if spread_amount == 0:
            continue  

        spread_count = 0
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] != -1:  # 확산 가능
                graph[ny][nx] += spread_amount
                spread_count += 1
        
        graph[y][x] -= spread_amount * spread_count

    

def air_purifier():
    top, bottom = ap
    for i in range(top - 1, 0, -1):  
        graph[i][0] = graph[i - 1][0]
    for i in range(C - 1):  
        graph[0][i] = graph[0][i + 1]
    for i in range(top):  
        graph[i][C - 1] = graph[i + 1][C - 1]
    for i in range(C - 1, 1, -1):  
        graph[top][i] = graph[top][i - 1]
    graph[top][1] = 0  

    for i in range(bottom + 1, R - 1):  
        graph[i][0] = graph[i + 1][0]
    for i in range(C - 1):  
        graph[R - 1][i] = graph[R - 1][i + 1]
    for i in range(R - 1, bottom, -1):  
        graph[i][C - 1] = graph[i - 1][C - 1]
    for i in range(C - 1, 1, -1):  
        graph[bottom][i] = graph[bottom][i - 1]
    graph[bottom][1] = 0

for _ in range(T):
    spread()
    air_purifier()

ans = sum(sum(row) for row in graph) + 2
print(ans)