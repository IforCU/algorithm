import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][k] or (graph[j][i] and graph[i][k]):
                graph[j][k] = 1
                    
for i in graph:
    print(*i)