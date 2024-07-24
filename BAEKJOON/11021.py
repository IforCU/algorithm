N = int(input())

for i in range(1,N+1):
    first, second = map(int,input().split())
    print(f"Case #{i}: {first+second}")