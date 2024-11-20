from collections import deque
N, K = map(int, input().split())

def bfs(n,k):
    if n == k:
        return '0\n1'
    size = max(2*k, n) + 1
    dp = [-1] * (size)
    ways = [0] * (size)

    dp[n] = 0
    ways[n] = 1
    queue = deque([n])
    
    while queue:
        x = queue.popleft()
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < size:
                if dp[nx] == -1:
                    dp[nx] = dp[x] + 1
                    ways[nx] = ways[x]
                    queue.append(nx)
                elif dp[nx] == dp[x] + 1:
                    ways[nx] += ways[x]
    return str(dp[k]) + '\n' + str(ways[k])

print(bfs(N, K))