from collections import deque
from itertools import *
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(array, new_graph):
    queue = deque(virus)
    for y, x in array:
        new_graph[y][x] = 1

    while queue:
        y, x = queue.popleft()

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if new_graph[ny][nx] == 0:
                    new_graph[ny][nx] = 2
                    queue.append((ny, nx))

    count = sum(row.count(0) for row in new_graph)
    
    return count 
        

virus = []
space = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i,j))
        if graph[i][j] == 0:
            space.append((i,j))


expect_value_list = list(combinations(space, 3))
ans = 0

for walls in expect_value_list:
    new_graph = copy.deepcopy(graph)
    ans = max(ans, bfs(walls, new_graph))

print(ans)