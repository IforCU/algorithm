from collections import deque
N, K = map(int, input().split())

def bfs(n,k):
    size = 2 * max(n,k)
    visited = [False] * (size + 1)
    visited[n] = True
    dp = [0] * (size + 1)
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if (2*x) <= size:
            if not visited[2*x]:
                queue.append(2*x)
                visited[2*x] = True
                if dp[2*x] != 0:
                    dp[2*x] = min(dp[x], dp[2*x])
                else:
                    dp[2*x] = dp[x]
        if (x-1) >= 0:
            if not visited[x-1]:    
                queue.append(x-1)
                visited[x-1] = True
                if dp[x-1] != 0:
                    dp[x-1] = min(dp[x]+1, dp[x-1])
                else:
                    dp[x-1] = dp[x]+1
        if (x+1) <= size:
            if not visited[x+1]:
                queue.append(x+1)
                visited[x+1] = True
                if dp[x+1] != 0:
                    dp[x+1] = min(dp[x]+1, dp[x+1])
                else:
                    dp[x+1] = dp[x]+1
        if dp[k] != 0:
            break
    return dp[k]

print(bfs(N,K))