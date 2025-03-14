import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

lis = []
for x in A:
    if not lis or lis[-1] < x:
        lis.append(x)
    else:
        left, right = 0, len(lis) - 1
        while left < right:
            mid = (left + right) // 2
            if lis[mid] < x:
                left = mid + 1
            else:
                right = mid
        lis[right] = x

print(len(lis))