import sys
input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    clothes = {}
    for _ in range(n):
        a, b = map(str, input().rstrip().split())
        if b in clothes:
            clothes[b] += 1
        else:
            clothes[b] = 2
    
    count = 1
    for val in clothes.values():
        count *= val
    print(count-1)