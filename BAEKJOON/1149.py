import sys
input = sys.stdin.readline
N = int(input())
dp = [[0,0,0] for _ in range(N)]
R = []
G = []
B = []
for _ in range(N):
    r, g, b = map(int, input().split())
    R.append(r)
    G.append(g)
    B.append(b)

for i in range(1,N):

    dp[0][0] = R[0]
    dp[0][1] = G[0]
    dp[0][2] = B[0]

    for j in range(3):
        if j == 0:
            dp[i][j] = R[i] + min(dp[i-1][1], dp[i-1][2])
        elif j == 1:
            dp[i][j] = G[i] + min(dp[i-1][0], dp[i-1][2])
        else:
            dp[i][j] = B[i] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))