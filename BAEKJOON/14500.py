import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
big = 0
for i in graph:
    if big < max(i):
        big = max(i)
maxValue = 0

def dfs(x,y,s, cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, s)
        return
    elif (s + big*(4-cnt) <= maxValue):
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(nx,ny, s + graph[ny][nx], cnt + 1)
                visited[ny][nx] = False

def exce(x,y):
    global maxValue
    for n in range(4):
        
        tmp = graph[y][x]
        for k in range(3):
            t = (n+k)%4            
            nx = x + dx[t]
            ny = y + dy[t]

            if not (0 <= nx < M and 0 <= ny < N):
                tmp = 0
                break
            tmp += graph[ny][nx]
        
        maxValue = max(maxValue, tmp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(j, i, graph[i][j], 1)
        visited[i][j] = False
        exce(j, i)

print(maxValue)