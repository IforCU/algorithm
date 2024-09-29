N = int(input())
s = input()
answer = 0
for i in range(N):
    answer += (ord(s[i]) - 96) * (31**i)
print(answer % 1234567891)