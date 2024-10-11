T = int(input())
dp = [0] * 101

def P(N):
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for i in range(6,N+1):
        dp[i] = dp[i-1] + dp[i-5]
    return dp[N]

for _ in range(T):
    N = int(input())
    print(P(N))