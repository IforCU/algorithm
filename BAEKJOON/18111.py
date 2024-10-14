import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
maps = [[] for _ in range(N)]
for i in range(N):
    maps[i] = list(map(int, input().split()))
maps.sort(reverse=True)
answer= []
ju = False
def leveling_land(land,b,h):
    global ju
    if ju:
        return
    time = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] != h:
                if land[i][j] > h:
                    b += land[i][j] - h
                    time += (land[i][j] - h) * 2
                else:
                    b -= h - land[i][j]
                    time += h - land[i][j]

    if b >= 0:
        if answer:
            if time < answer[0]:
                answer[0] = time
                answer[1] = h
            elif time == answer[0]:
                if answer[1] < h:
                    answer[1] = h
            else:
                ju = True
        else:
            answer.append(time)
            answer.append(h)


value = 0
for i in maps:
    if value < max(i):
        value = max(i)

for i in range(value+1,-1,-1):
    leveling_land(maps,B,i)

print(answer[0], answer[1])