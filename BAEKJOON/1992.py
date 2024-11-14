import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]

def check(n,map):
    first = map[0][0]
    for i in range(n):
        for j in range(n):
            if map[i][j] != first:
                return False
    return True

def quad_Tree(n, map):
    
    if check(n, map):
        return str(map[0][0])
    
    half = n//2
    
    top_left = [row[:half] for row in map[:half]]
    top_right = [row[half:] for row in map[:half]]
    bottom_left = [row[:half] for row in map[half:]]
    bottom_right = [row[half:] for row in map[half:]]
    
    temp = '('
    temp += quad_Tree(half, top_left)
    temp += quad_Tree(half, top_right)
    temp += quad_Tree(half, bottom_left)
    temp += quad_Tree(half, bottom_right)
    temp += ')'

    return temp

print(quad_Tree(N,graph))