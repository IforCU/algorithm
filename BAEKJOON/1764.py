import sys
input = sys.stdin.readline
N, M = map(int, input().split())
h = {}
n = []
for _ in range(N):
    h[input().rstrip()] = 1

for _ in range(M):
    a = input().rstrip()
    if h.get(a,0) == 1:
        n.append(a)

n.sort()
print(len(n))
for name in n:
    print(name)