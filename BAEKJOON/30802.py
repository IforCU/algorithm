N = int(input())
shirts = list(map(int,input().split()))
T, P = map(int,input().split())
count = 0
for i in shirts:
    count += i//T
    if i%T > 0:
        count += 1

print(count)
print(f'{N//P} {N%P}')