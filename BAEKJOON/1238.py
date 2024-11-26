from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e,t))

def dijkstr(start):
    dis = [INF] * (N+1)
    dis[start] = 0
    queue = deque()
    queue.append((0,start))

    while queue:
        dist, now = queue.popleft()

        if dis[now] < dist:
            continue
        for nn, nd in graph[now]:
            cost = dist + nd
            if cost < dis[nn]:
                dis[nn] = cost
                queue.append((cost, nn))
    return dis

to_party = [0] * (N+1)
for i in range(1, N+1):
    to_party[i] = dijkstr(i)[X]

from_party = dijkstr(X)

ans = 0
for i in range(1, N+1):
    ans = max(ans, to_party[i] + from_party[i])

print(ans)