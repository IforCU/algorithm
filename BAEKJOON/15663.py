import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
back_arr = [0 for _ in range(M)]
visited = [False for _ in range(N)]
answer = []
arr.sort()
def dfs(n, m, depth):
    if m == depth:
        answer.append(' '.join(map(str, back_arr)))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            back_arr[depth] = arr[i]
            dfs(n,m,depth + 1)
            visited[i] = False

dfs(N, M, 0)
answer = list(set(answer))
ans = []
for i in answer:
    ans.append(list(map(int, i.split(' '))))

ans.sort()
for i in ans:
    print(*i)