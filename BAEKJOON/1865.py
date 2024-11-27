import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(n, edges):
    dist = [INF] * (n + 1)
    dist[1] = 0
    
    for i in range(n):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if i == n - 1:
                    return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))  
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))  

    if bellman_ford(N, edges):
        print("YES")
    else:
        print("NO")