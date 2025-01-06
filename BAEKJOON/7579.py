N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

max_cost = sum(costs)
dp = [0] * (max_cost + 1)

for i in range(N):
    memory = memories[i]
    cost = costs[i]
    for j in range(max_cost, cost - 1, -1):
        dp[j] = max(dp[j], dp[j-cost] + memory)

for cost in range(max_cost + 1):
    if dp[cost] >= M:
       print(cost)
       break