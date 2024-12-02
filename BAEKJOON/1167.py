import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while data[idx] != -1:
        graph[node].append((data[idx], data[idx+1]))
        idx += 2

def dfs(node, distance):
    for next_node, d in graph[node]:
        if dist[next_node] == -1:
            dist[next_node] = distance + d
            dfs(next_node, distance + d)

dist = [-1] * (V + 1) 
dist[1] = 0 
dfs(1, 0)

far_node = dist.index(max(dist)) 
dist = [-1] * (V + 1) 
dist[far_node] = 0 
dfs(far_node, 0)

print(max(dist))