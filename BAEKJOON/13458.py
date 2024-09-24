N = int(input())
room = list(map(int,input().split()))
B, C = map(int,input().split())
viewer = 0
for pe in room:
    pe -= B
    viewer += 1
    if pe > 0:
        viewer += pe//C
        if pe%C > 0:
            viewer += 1
print(viewer)