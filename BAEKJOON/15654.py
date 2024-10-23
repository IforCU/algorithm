N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for _ in range(N)]
arr.sort()
back_arr = [0 for _ in range(M)]

def dfs(n, m, depth):
    if depth == m:
        print(' '.join(map(str, back_arr)))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            back_arr[depth] = arr[i]
            dfs(n,m, depth + 1)
            visited[i] = False

dfs(N, M, 0)