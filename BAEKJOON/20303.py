import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    
visited = [False] * N
groups = []

def dfs(node, group):
    stack = [node]
    people, total_candy = 0, 0
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        visited[cur] = True
        people += 1
        total_candy += candies[cur]
        for neighbor in graph[cur]:
            if not visited[neighbor]:
                stack.append(neighbor)
    group.append((people, total_candy))

for i in range(N):
    if not visited[i]:
        temp_group = []
        dfs(i, temp_group)
        groups.append(temp_group[0])

dp = [0] * K

for people, candy in groups:
    for j in range(K - 1, people - 1, -1):
        dp[j] = max(dp[j],dp[j - people] + candy)

print(max(dp))