import sys
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()

max_value = 0
jewels_able = []
j = 0

for bag in bags:
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(jewels_able, -jewels[j][1])
        j += 1
    
    if jewels_able:
        max_value -= heapq.heappop(jewels_able)

print(max_value)