import math
N = int(input())
num = math.factorial(N)
count = 0
for i in str(num)[::-1]:
    if i == '0':
        count += 1
    else:
        break

print(count)