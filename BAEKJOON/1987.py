import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    ans = 1
    st = set()
    st.add((x,y,graph[y][x]))
    while st:
        x, y, visited = st.pop()
        ans = max(ans, len(visited))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < C and 0 <= ny < R:
                if graph[ny][nx] not in visited:
                    st.add((nx,ny,visited + graph[ny][nx]))
    return ans

print(dfs(0,0))