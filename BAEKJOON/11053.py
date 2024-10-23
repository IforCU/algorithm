N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]
min_value = min(arr)
for i in range(1,N):
    max_value = max(dp)
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        elif dp[i] > max_value:
            break

print(max(dp))