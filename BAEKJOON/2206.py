from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    queue = deque([(0, 0, 1, 1)])
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = True

    while queue:
        x, y, dist, crush = queue.popleft()

        if x == M-1 and y == N-1:
            return dist
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0 and not visited[ny][nx][crush]:
                    visited[ny][nx][crush] = True
                    queue.append((nx ,ny ,dist + 1, crush))
                elif graph[ny][nx] == 1 and crush == 1 and not visited[ny][nx][0]:
                    visited[ny][nx][0] = True
                    queue.append((nx, ny, dist + 1, 0))    
    return -1

ans = bfs()
print(ans)