import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, cost = map(int, input().split())
    graph[x].append((y,cost))
    graph[y].append((x,cost))

def dfs(x, dist):
    for y, d in graph[x]:
        if distance[y] == -1:
            distance[y] = dist + d
            dfs(y, dist + d)


distance = [-1] * (n+1)
distance[1] = 0
dfs(1,0)

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start,0)

print(max(distance))