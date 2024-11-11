import math
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    b = math.comb(m, n)
    print(b)