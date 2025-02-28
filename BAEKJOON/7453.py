from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

A, B, C ,D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB_sum = Counter(a + b for a in A for b in B)

count = 0
for c in C:
    for d in D:
        count += AB_sum[-(c+d)]
    
print(count)