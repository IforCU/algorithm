import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array_a = []
array_b = []

for _ in range(N):
    array_a.append(list(map(int, input().split())))

for _ in range(N):
    array_b.append(list(map(int, input().split())))


for i in range(N):
    for j in range(len(array_a[0])):
        print(array_a[i][j] + array_b[i][j], end=' ')
    print()