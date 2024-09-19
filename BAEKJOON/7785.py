import sys
N = int(input())
s = set()

for _ in range(N):
    name, el = input().split()
    if el == 'enter':
        s.add(name)
    else:
        if name in s:
            s.remove(name)

for name in sorted(s, reverse=True):
    print(name)

