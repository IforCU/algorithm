import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

t = list(map(int, input().split()))
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        
ans = 0
for a in range(1,n+1):
    sum_value = 0
    for b in range(1,n+1):
        if graph[a][b] <= m:
            sum_value += t[b-1]
    ans = max(ans, sum_value)

print(ans)