import sys
input = sys.stdin.readline
N, M = map(int, input().split())
floor = [0 for _ in range(N)] 
ans = 0
for i in range(N):
    floor[i] = list(input().rstrip())

w = [0 for _ in range(M)]
l = [0 for _ in range(N)]

for i in range(N):
    for j in range(M):
        if floor[i][j] == 'X':
            l[i] = l[i] + 1
            w[j] = w[j] + 1

a = w.count(0)
b = l.count(0)
ans = a + b - min(a,b)
print(ans)