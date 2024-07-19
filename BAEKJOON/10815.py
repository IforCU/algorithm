M = int(input())
cards = set(map(int,input().split()))
N = int(input())
queries = list(map(int,input().split()))

for i in queries:
    if(i in cards):
        print("1",end=" ")
    else:
        print("0",end=" ")