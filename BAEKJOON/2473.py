import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
closest = float('inf')
res = ()

for i in range(n - 2):
    l, r = i + 1, n - 1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        if abs(s) < abs(closest):
            closest = s
            res = (arr[i], arr[l], arr[r])
        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            print(*sorted(res))
            exit()

print(*sorted(res))
