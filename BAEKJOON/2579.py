import sys
input = sys.stdin.readline
N = int(input().rstrip())
stairs = [0] * (N+1)
dp = [0] * (N+1)
for i in range(1,N+1):
    stairs[i] = int(input().rstrip())

if N==1:
    print(stairs[1])
elif N==2:
    print(sum(stairs))
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3,N+1):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
    print(dp[-1])