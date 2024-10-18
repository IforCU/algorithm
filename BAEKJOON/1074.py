import math
N, r, c = map(int, input().split())

n = int(math.pow(2,N))
dx = [0,-1,0,-1]
dy = [0,0,-1,-1]
def Z(end, x, y, l):
    if l == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == c and ny == r:
                print(end-i)
                return
    else:
        L = l//2
        fx = [x,x-L,x,x-L]
        fy = [y,y,y-L,y-L]
        for i in range(4):
            if (fx[i] - L) < c <= (fx[i]) and (fy[i] - L) < r <= (fy[i]):
                Z(end - (L*L*i),fx[i],fy[i],L)

Z((n*n) - 1, n-1, n-1, n)