from collections import deque
import sys
input = sys.stdin.readline

ladder = [0 for _ in range(101)]
snake = [0 for _ in range(101)]
N, M = map(int, input().split())
visited = [False for _ in range(101)]
maps = [0 for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

def bfs():
    visited[1] = True
    queue = deque()
    queue.append(1)
    
    while queue:
        x = queue.popleft()
        for i in range(1,7):
            nx = x+i
            
            if 0 < nx <= 100:
                if ladder[nx]:
                    nx = ladder[nx]
                elif snake[nx]:
                    nx = snake[nx]

                if not visited[nx]:
                    visited[nx] = True
                    maps[nx] = maps[x] + 1
                    queue.append(nx)

                if nx == 100:
                    return 
bfs()
print(maps[100])