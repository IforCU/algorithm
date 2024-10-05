N = int(input())

user = [[] for _ in range(201)] 

def add_user(x,y):
    if 0 <= x < len(user):
        user[x].append(y)

for _ in range(N):
    list = []
    x, y = map(str,input().split())
    add_user(int(x),y)

for i in range(len(user)):
    if user[i]:
        for ch in user[i]:
            print(i, ch)