from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
Map = [[] for _ in range(N)]
apartment = [[0 for _ in range(N)] for _ in range(N)]
number = 1
for i in range(N):
    Map[i] = list(map(int, input().rstrip()))

def bfs(a,b,num):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[b][a] = True    
    apartment[b][a] = num
    queue = deque()
    queue.append((a,b))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx]:
                    if Map[ny][nx] == 1:
                        queue.append((nx,ny))
                        visited[ny][nx] = True
                        apartment[ny][nx] = num
    count = 0
    for i in visited:
        for j in i:
            if j:
                count += 1
    return count

ans = []
for i in range(N):
    for j in range(N):
        if Map[j][i] == 1 and apartment[j][i] == 0:
            ans.append(bfs(i,j,number))
            number += 1

ans.sort()
print(len(ans))
for i in ans:
    print(i)