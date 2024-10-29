import heapq
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for i in range(M):
    city1, city2, cost = map(int, input().split())
    graph[city1].append((city2, cost))

start, end = map(int, input().split())
costs = [1e9 for _ in range(N+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0,start])

while heap:
    cost, v =  heapq.heappop(heap)
    if costs[v] < cost:
        continue
    for dv, dCost in graph[v]:
        sum_cost = cost + dCost
        if costs[dv] <= sum_cost:
            continue
        
        costs[dv] = sum_cost
        heapq.heappush(heap, [sum_cost, dv])

print(costs[end])