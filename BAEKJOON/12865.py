import sys
input = sys.stdin.readline
N, K = map(int, input().split())
thing = []
for _ in range(N):
    W, V = map(int, input().split())
    thing.append((W,V))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        w = thing[i-1][0]
        v = thing[i-1][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

print(dp[-1][-1])