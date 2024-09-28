import math
N = int(input())
numbers = list(map(int,input().split()))
count = 0
def primeNumber(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

for i in numbers:
    if(primeNumber(i)):
         count += 1

print(count)