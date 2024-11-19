A, B, N = map(int, input().split())

for i in range(N):
    A = (A%B) * 10
    ans = A//B

print(ans)