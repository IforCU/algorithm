from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
node = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)

visited = [False for _ in range(N+1)]
def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in node[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

count = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        count += 1
print(count)