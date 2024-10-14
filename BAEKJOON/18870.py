import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
a = sorted(list(set(arr)))
v = {}
for i in range(len(a)):
    v[a[i]] = i

for i in arr:
    print(v[i],end=' ')