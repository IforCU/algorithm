from collections import deque
import sys
input = sys.stdin.readline

def round(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())
level = []
for _ in range(N):
    level.append(int(input()))

level = deque(sorted(level))
rd = round((N / 100)* 15)
avg = N - (2*rd)
for i in range(rd):
    level.pop()
    level.popleft()

if avg <= 0:
    avg = 1
print(round(sum(level)/avg))