N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
back_arr = [0 for _ in range(M)]
answer = []
def dfs(n,m,depth, start):
    if depth == m:
        answer.append(' '.join(map(str, back_arr)))
        return

    for i in range(start,n):
        back_arr[depth] = arr[i]
        dfs(n,m,depth + 1, i)
            
dfs(N, M, 0, 0)
answer = list(set(answer))
ans = []
for i in answer:
    ans.append(list(map(int, i.split(' '))))

ans.sort()
for i in ans:
    print(*i)