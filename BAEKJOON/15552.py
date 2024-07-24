import sys

N = int(sys.stdin.readline())

for i in range(0,N):
    first, second = map(int,sys.stdin.readline().split())
    print(first + second)