from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
group_size = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, group_id):
    queue = deque([(sx, sy)])
    visited[sx][sy] = group_id
    count = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = group_id
                queue.append((nx, ny))
                count += 1
    
    return count

group_id = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == -1:
            group_size.append(bfs(i, j, group_id))
            group_id += 1

ans = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            adj_groups = set()
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] != -1:
                    adj_groups.add(visited[ni][nj])

            ans[i][j] = (1 + sum(group_size[g] for g in adj_groups)) % 10

for row in ans:
    print("".join(map(str, row)))
