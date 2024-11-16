N = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)

ans = [0 for _ in range(N)]

for i in range(N):
    ans[i] = sorted_A.index(A[i])
    sorted_A[sorted_A.index(A[i])] = -1

print(*ans)