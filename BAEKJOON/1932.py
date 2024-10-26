import math
import sys
input = sys.stdin.readline
N = int(input())
tg = [[] for _ in range(N)]
for i in range(N):
    tg[i] = list(map(int, input().split()))

limit = 0
for i in range(1,N+1):
    limit += i

dp = [0 for _ in range(limit)]
dp[0] = tg[0][0]

def sum_triangle():
    count = 1
    for i in range(1,N):
        length = len(tg[i])
        for j in range(length):
            if j == 0:
                 dp[count] = tg[i][j] + dp[count-length+1]
            elif j == length-1:
                dp[count] = tg[i][j] + dp[count-length]
            else:
                dp[count] = max(tg[i][j] + dp[count-length], tg[i][j] + dp[count-length+1])
            count += 1

    return max(dp)

print(sum_triangle())