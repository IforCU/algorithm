N = int(input())
ans = 0

visited_x = [False for _ in range(N)]
visited_di_r = [False for _ in range(2 * N)]
visited_di_l = [False for _ in range(2 * N)]

def dfs(row):
    global ans
    if row == N:
        ans += 1
        return
    for col in range(N):
        if not visited_x[col] and not visited_di_r[row + col] and not visited_di_l[row - col + (N - 1)]:
            visited_x[col] = True
            visited_di_r[row + col] = True
            visited_di_l[row - col + (N - 1)] = True
            dfs(row + 1)
            visited_x[col] = False
            visited_di_r[row + col] = False
            visited_di_l[row - col + (N - 1)] = False

dfs(0)
print(ans)