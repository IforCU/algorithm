import sys
input = sys.stdin.readline
N, M = map(int, input().split())
maps = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    maps[i] = list(map(int, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        dp[i][j] = maps[i][j] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for i in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    ans = dp[y2-1][x2-1] + dp[y1-2][x1-2] - dp[y2-1][x1-2] - dp[y1-2][x2-1]
    print(ans)