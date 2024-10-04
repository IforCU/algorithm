N = int(input())
list = []
for _ in range(N):
    x, y = map(int,input().split())
    list.append([x,y,1])

for i in list:
    for j in list:
        if i[0] > j[0] and i[1] > j[1]:
            j[2] += 1

for i in list:
    print(i[2], end=' ')