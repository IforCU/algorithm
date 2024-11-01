import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def extra(n):
    dist  = [int(1e12)] * (V+1)
    dist[n] = 0
    queue = [(0,n)]

    while queue:
        cDist, cNode = heapq.heappop(queue)

        for aNode, aDist in graph[cNode]:
            tDist = cDist + aDist
            if tDist < dist[aNode]:
                dist[aNode] = tDist
                heapq.heappush(queue,(tDist,aNode))
            
    return dist

distK = extra(K)

for i in range(1,V+1):
    if distK[i] == int(1e12):
        print('INF')
    else:
        print(distK[i])