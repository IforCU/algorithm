import sys
input = sys.stdin.readline
N = int(input())
s = [False] * 21
answer = []
for _ in range(N):
    M = list(map(str,input().split()))
    if M[0] == 'add':
        s[int(M[1])] = True
    elif M[0] == 'remove':
        s[int(M[1])] = False
    elif M[0] == 'check':
        if s[int(M[1])]:
            print(1)
        else:
            print(0)
    elif M[0] == 'toggle':
        if s[int(M[1])]:
            s[int(M[1])] = False
        else:
            s[int(M[1])] = True
    elif M[0] == 'all':
        s = [True] * 21
    else:
        s = [False] * 21