from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
comparisons = [tuple(map(int, input().split())) for _ in range(M)]

adj_list = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for A, B in comparisons:
    adj_list[A].append(B)
    in_degree[B] += 1

queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])
ans = []

while queue:
    current = queue.popleft()
    ans.append(current)

    for neighbor in adj_list[current]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

print(*ans)