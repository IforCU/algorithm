import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for i in range(M):
    city1, city2, cost = map(int, input().split())
    graph[city1].append((city2, cost))

visited = [False for _ in range(N+1)]

ans = []

def dfs(x,y,cost):
    if x == y:
        ans.append((cost))
        return
    
    for i, value in graph[x]:
        if not visited[i]:
            if ans:
                if ans[-1] <= cost + value:
                    continue
            
            visited[i] = True
            dfs(i,y,value + cost)
            visited[i] = False

a, b = map(int, input().split())
dfs(a,b,0)
print(ans[-1])