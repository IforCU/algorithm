N = int(input())
M = int(input())
S = input().rstrip()
P = 'I'
for _ in range(N):
    P += 'OI'
length = (2*N) + 1
count = 0
for i in range((M - (2*N))):
    if S[i:i+length] == P:
        count += 1
print(count)