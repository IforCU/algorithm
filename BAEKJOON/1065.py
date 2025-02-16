N = int(input())
count = 0

for i in range(1, N+1):
    if i < 100:
        count += 1
    else:
        a = i // 100
        b = (i//10) % 10
        c = i % 10

        if (a-b) == (b-c):
            count += 1

print(count)