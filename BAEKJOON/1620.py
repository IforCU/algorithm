import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Encyclopedia = {}
ReEncyclopedia = {}
for i in range(1,N+1):
    s = input().rstrip()
    Encyclopedia[i] = s
    ReEncyclopedia[s] = i

for _ in range(M):
    s = input().rstrip()
    if s.isdigit():
        print(Encyclopedia[int(s)])
    else:
        print(ReEncyclopedia[s])