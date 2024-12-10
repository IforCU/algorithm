import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(V+1))
    rank = [0] * (V+1)
    
    mst_weight = 0
    max_weight = 0

    for A, B, C in edges:
        if find(parent, A) != find(parent, B):
            union(parent, rank, A, B)
            mst_weight += C
            max_weight = max(max_weight, C)
    
    return mst_weight - max_weight

print(kruskal(N, edges))