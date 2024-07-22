X = int(input())
N = int(input())

for i in range(1,N+1):
    a,b = map(int, input().split())
    X -= a*b

if(X == 0):
    print("Yes")
else:
    print("No")