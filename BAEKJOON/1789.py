S = int(input())

N = 0
sum = 0
while(S >= sum):
    sum += N
    N += 1
N -= 1
if sum > S:
    N -= 1
print(N)