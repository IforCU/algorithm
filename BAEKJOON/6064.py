import sys
input = sys.stdin.readline
n = int(input())

def kaing_calender(m, n, x, y):
    while x <= m*n:
        if (x-1) % n + 1 == y:
            return x
        x += m
    return -1
    
for _ in range(n):
    M, N, X, Y = map(int, input().rstrip().split())
    print(kaing_calender(M, N, X, Y))