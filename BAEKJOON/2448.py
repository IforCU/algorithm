N = int(input())

pattern = [[' '] * 2 * N for _ in range(N)]

def recursion(x,y,n):
    if n == 3:
        pattern[x][y] = '*'
        pattern[x+1][y-1] = pattern[x+1][y+1] = '*'
        for i in range(-2,3):
            pattern[x+2][y+i] = '*'
    else:
        nn = n//2
        recursion(x,y,nn)
        recursion(x + nn, y - nn, nn)
        recursion(x + nn, y + nn, nn)

recursion(0,N-1,N)
for i in pattern:
    print(''.join(i))