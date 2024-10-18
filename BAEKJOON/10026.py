from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(str,input().rstrip())) for _ in range(N)]
red_graph = [['' for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            red_graph[i][j] = 'R'
        else:
            red_graph[i][j] = graph[i][j]

visited_normal = [[False for _ in range(N)] for _ in range(N)]
visited_red = [[False for _ in range(N)] for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
color_normal = {'R':0, 'G':0, 'B':0}
color_red = {'R':0, 'B':0}
def bfs(visited,maps,a,b):
    target = maps[b][a]
    visited[b][a] = True
    queue = deque()
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx]:
                    if maps[ny][nx] == target:
                        queue.append((nx,ny))
                        visited[ny][nx] = True
    
    return target
    
for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            color_normal[bfs(visited_normal,graph,j,i)] += 1
        if not visited_red[i][j]:
            color_red[bfs(visited_red,red_graph,j,i)] += 1

print(sum(color_normal.values()), sum(color_red.values()))