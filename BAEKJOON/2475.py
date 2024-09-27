numbers = list(map(int,input().split()))
unique = 0
for n in numbers:
    unique += n*n
print(unique%10)