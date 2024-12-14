A = ' '+input().strip()
B = ' '+input().strip()

dp = [[0 for _ in range(len(B))] for _ in range(len(A))]

for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

i, j = len(A) - 1, len(B) - 1
lcs = []

while i > 0 and j > 0:
    if A[i] == B[j]:
        lcs.append(A[i])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1
print(''.join(reversed(lcs)))
