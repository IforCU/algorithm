from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int,input().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for sub in graph:
    sub.sort()

dfs_visited = []
def dfs(maps, v):
    if v not in dfs_visited:
        dfs_visited.append(v)
    else:
        return
    for i in maps[v]:
        if i not in dfs_visited:
            dfs(maps,i)


def bfs(maps, v):
    visited = []
    queue = deque()
    queue.append(v)

    while queue:
        x = queue.popleft()
        if x not in visited:
            visited.append(x)

        for i in maps[x]:
            if i not in visited:
                queue.append(i)
    return visited

dfs(graph,V)
print(*dfs_visited)
print(*bfs(graph,V))