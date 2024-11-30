import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstr(start, end):
    dis = [INF] * (n+1)
    dis[start] = 0
    queue = []
    heapq.heappush(queue, (0, start, [start])) 
    
    while queue:
        dist, now, path = heapq.heappop(queue)
        if now == end:  
            return dist, path
        if dist > dis[now]: 
            continue
        for nn, nd in graph[now]:
            cost = dist + nd
            if cost < dis[nn]:
                dis[nn] = cost
                heapq.heappush(queue, (cost, nn, path + [nn]))

ans, line = dijkstr(start, end)
print(ans)
print(len(line))
print(*line)