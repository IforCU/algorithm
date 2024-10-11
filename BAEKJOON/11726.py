n = int(input())

dp = [0] * 1001

def tiling(N):
    dp[1] = 1
    dp[2] = 2
    for i in range(3,N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

print(tiling(n)%10007)