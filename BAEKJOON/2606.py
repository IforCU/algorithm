import sys
from collections import deque
input = sys.stdin.readline
com = int(input().rstrip())
N = int(input().rstrip())

graph = [[] for _ in range(com+1)]

for _ in range(N):
    x,y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

def virus():
    visited = [False] * (com+1)
    queue = deque([1])
    visited[1] = [True]
    count = 0

    while queue:
        current = queue.popleft()
        count += 1

        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    return count - 1

print(virus())