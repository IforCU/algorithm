from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

#Spanning Tree
#모든 정점을 연결하는 최소 간선 수를 구하는것
#통신 네트워크 구축에 활용
#MST = 간선 가중치의 합이 최소인 트리

# 프림 알고리즘
# 정점 중심으로 트리를 만듬
def prim(V, edges):
    graph = defaultdict(list)
    for A, B, C in edges:
        graph[A].append((C,B))
        graph[B].append((C,A))

    visited = [False] * (V+1)
    min_heap = [(0,1)]
    mst_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if visited[node]:
            continue
        
        visited[node] = True
        mst_weight += weight

        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_weight, next_node))
    
    return mst_weight

# 크루스칼 알고리즘
# 간선 중심으로 트리를 만듬
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
    for A, B, C in edges:
        if find(parent, A) != find(parent, B):
            union(parent, rank, A, B)
            mst_weight += C
    
    return mst_weight

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

print(prim(V, edges))