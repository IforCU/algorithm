import heapq
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
shark_size = 2
shark_eat = 0
shark_location = (0, 0)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_location = (i, j)
            graph[i][j] = 0

def bfs(location, graph):
    visited = [[False] * N for _ in range(N)]
    heap = []
    queue = [(0, location[0], location[1])]  
    visited[location[0]][location[1]] = True

    while queue:
        time, y, x = heapq.heappop(queue)

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] <= shark_size:
                visited[ny][nx] = True
                if 0 < graph[ny][nx] < shark_size:
                    heapq.heappush(heap, (time + 1, ny, nx))  
                else:
                    heapq.heappush(queue, (time + 1, ny, nx))

    if heap:
        return heapq.heappop(heap) 
    return None

def simulate():
    global shark_size, shark_eat, shark_location
    ans = 0

    while True:
        result = bfs(shark_location, graph)
        if not result:
            break

        time, y, x = result
        graph[shark_location[0]][shark_location[1]] = 0
        shark_location = (y, x)
        graph[y][x] = 0
        ans += time
        shark_eat += 1

        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0
    return ans

print(simulate())