from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
maps = [[] for _ in range(N)]
do = []
for i in range(N):
    maps[i] = list(input().rstrip())
    if 'I' in maps[i]:
        do.append(i)
        do.append(maps[i].index('I'))
count = 0

def bfs(x,y):
    global count
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    queue.append((x,y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        px, py = queue.popleft()
        visited[py][px] = True
        for i in range(4):
            nx = dx[i] + px
            ny = dy[i] + py
            
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx]:
                    if maps[ny][nx] == 'O':
                        queue.append((nx,ny))
                    elif maps[ny][nx] == 'P':
                        queue.append((nx,ny))
                        count += 1
                    visited[ny][nx] = True
    return count
answer = bfs(do[1],do[0])
if answer == 0:
    print('TT')
else:
    print(answer)