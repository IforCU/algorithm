N, X = map(int,input().split())
numbers = list(map(int,input().split()))
for n in numbers:
    if n < X:
        print(f'{n} ',end='')