import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, R, Q = map(int, input().split())

tree = [[] for _ in range(N+1)]
size = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node, parent):
    size[node] = 1
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            size[node] += size[neighbor]

dfs(R, -1)

for _ in range(Q):
    u = int(input())
    print(size[u])