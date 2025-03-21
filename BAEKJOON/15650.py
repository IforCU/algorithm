N, M = map(int, input().split())
arr = [0 for _ in range(M)]
visited = [False for _ in range(N+1)]

def dfs(n, m, depth, start):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, n+1):
        if not visited[i]:
            visited[i] = True
            arr[depth] = i
            dfs(n, m, depth + 1, i + 1)
            visited[i] = False

dfs(N, M, 0, 1)