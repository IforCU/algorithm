import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])  
    return parent[x]

def union(a, b):
    parent[a] = b

G = int(input())
P = int(input())

parent = list(range(G + 1))
cnt = 0

for _ in range(P):
    g = int(input())
    docking = find(g)

    if docking == 0:
        break

    union(docking, docking - 1)
    cnt += 1

print(cnt)