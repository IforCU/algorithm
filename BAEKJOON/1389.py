from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    friend = {i : 0 for i in range(1,N+1)}
    visited = [False for _ in range(N+1)]
    visited[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        for a in graph[x]:
            if not visited[a]:
                queue.append(a)
                visited[a] = True
                friend[a] = friend[x] + 1
    return sum(friend.values())

ans = []
for i in range(1,N+1):
    ans.append(bfs(i))
print(ans.index(min(ans)) + 1)