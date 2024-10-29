import sys
input = sys.stdin.readline
N = int(input())
dpB = [0,0,0]
dpS = [0,0,0]

for i in range(N):
    a, b, c = list(map(int, input().split()))
    dpB = [a + max(dpB[0],dpB[1]), b + max(dpB[0],dpB[1],dpB[2]), c + max(dpB[1],dpB[2])]
    dpS = [a + min(dpS[0],dpS[1]), b + min(dpS[0],dpS[1],dpS[2]), c + min(dpS[1],dpS[2])]

print(max(dpB), min(dpS))