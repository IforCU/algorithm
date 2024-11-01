import heapq
import sys
input = sys.stdin.readline
N, E = map(int, input().split())
INF = int(1e12)

graph = [[] for _ in range(N+1)]
for _ in range(E):
    x, y, dis = map(int, input().split())
    graph[x].append([y,dis])
    graph[y].append([x,dis])

v1,v2 = map(int, input().split())

def extra(start):
    dist = [int(1e12)] * (N+1)
    dist[start] = 0
    q = [(0,start)]

    while q:
        cDist, cNode = heapq.heappop(q)

        if cDist > dist[cNode]:
            continue

        for aNode, aDist in graph[cNode]:
            distance = cDist + aDist

            if distance < dist[aNode]:
                dist[aNode] = distance
                heapq.heappush(q,(distance, aNode))
    
    return dist

dist1 = extra(1)
distV1 = extra(v1)
distV2 = extra(v2)

total1 = dist1[v1] + distV1[v2] + distV2[N]
total2 = dist1[v2] + distV2[v1] + distV1[N]

ans = min(total1,total2)

if ans >= int(1e12):
    print(-1)
else:
    print(ans)