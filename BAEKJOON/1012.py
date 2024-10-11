from collections import deque

def bfs(x, y, maps, M, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x,y))
    maps[y][x] = -1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < M and 0 <= ny < N and maps[ny][nx] == 1:
                maps[ny][nx] = -1
                queue.append((nx,ny))
    

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    maps = [[0]*M for _ in range(N)]  
    count = 0
    
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        maps[y][x] = 1  
    
    for y in range(N):
        for x in range(M):
            if maps[y][x] == 1:  
                bfs(x, y, maps, M, N)
                count += 1  
    
    print(count)