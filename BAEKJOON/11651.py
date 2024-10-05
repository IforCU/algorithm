N = int(input())
list = []
for _ in range(N):
    x, y = map(int, input().split())
    list.append([y,x])

list.sort()

for y, x in list:
    print(x, y)