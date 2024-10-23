N, M = map(int, input().split())
arr = [0 for _ in range(M)]

def dfs(n, m, depth, start):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, n+1):
        arr[depth] = i
        dfs(n, m, depth + 1, i)

dfs(N, M, 0, 1)