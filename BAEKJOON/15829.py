N = int(input())
s = input()
answer = 0
for i in range(N):
    answer += (int(ord(s[i]) - 96)) * (31**i)
print(answer)