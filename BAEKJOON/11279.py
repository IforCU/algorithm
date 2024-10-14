import sys
input = sys.stdin.readline
import heapq
heap = []
N = int(input())

for _ in range(N):
    item = int(input())
    if item == 0:
        if heap:
             print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-item, item))