from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append((i,j))
        elif graph[i][j] == 1:
            house.append((i,j))

def ch_dis_house(chi, min_value):
    sum_dis = 0
    for y1, x1 in house:
        dis = 1e9
        for y2, x2 in chi:
            if dis > abs(x2-x1) + abs(y2-y1):
                dis = abs(x2-x1) + abs(y2-y1)
        sum_dis += dis
        if sum_dis >= min_value:
            return ''
    return sum_dis

chi_com = list(combinations(chicken,M))    
ans = [1e9]
for i in chi_com:
    k = ch_dis_house(i, ans[-1])
    if k != '':
        ans.append(k)

print(ans[-1])