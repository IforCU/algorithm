from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)

    for _ in range(K):
        X, Y = map(int, input().split())
        adj[X].append(Y)
        in_degree[Y] += 1
    
    W = int(input())

    dp = build_time[:]
    q = deque([i for i in range(1, N+1) if in_degree[i] == 0])

    while q:
        current = q.popleft()
        for next_build in adj[current]:
            in_degree[next_build] -= 1
            dp[next_build] = max(dp[next_build], dp[current] + build_time[next_build])
            if in_degree[next_build] == 0:
                q.append(next_build)
    
    print(dp[W])