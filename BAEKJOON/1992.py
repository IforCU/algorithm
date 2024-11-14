import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

def check(map, x, y, size):
    first = map[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if map[i][j] != first:
                return False
    return True

def quad_Tree(map, x, y, size):
    
    if check(map, x, y, size):
        return str(map[y][x])
    
    half = size // 2
    temp = '('
    temp += quad_Tree(graph, x, y, half)
    temp += quad_Tree(graph, x + half, y, half)
    temp += quad_Tree(graph, x, y + half, half)
    temp += quad_Tree(graph, x + half, y + half, half)
    temp += ')'

    return temp

print(quad_Tree(graph, 0, 0, N))