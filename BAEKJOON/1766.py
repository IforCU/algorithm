import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = []
ans = []

for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    ans.append(cur)
    for nxt in graph[cur]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            heapq.heappush(q, nxt)

print(*ans)
