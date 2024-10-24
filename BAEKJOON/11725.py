from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
node = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)

def bfs():
    queue = deque()
    queue.append(1)
    visited = [False for _ in range(N+1)]
    visited[1] = True
    while queue:
        x = queue.popleft()

        for i in node[x]:
            if not visited[i]:
                queue.append(i)
                answer[i] = x
                visited[i] = True
    
bfs()
for i in range(2,N+1):
    print(answer[i])