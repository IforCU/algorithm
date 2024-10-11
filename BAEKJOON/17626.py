import math
n = int(input())

dp = [0] * 50001

def four_squares(N):

    for i in range(1,N+1):
        cal = []
        sq = int(math.sqrt(i))
        for j in range(1,sq+1):
            cal.append(dp[i-(j*j)] + 1)
        dp[i] = min(cal)
    return dp[N]

print(four_squares(n))