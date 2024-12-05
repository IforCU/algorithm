import sys
input = sys.stdin.readline
N = int(input())
location = [tuple(map(int, input().split())) for _ in range(N)]

area = 0
for i in range(N):
    x1, y1 = location[i]
    x2, y2 = location[(i+1) % N]
    area += x1 * y2 - y1 * x2

ans = abs(area) / 2
print(f"{ans:.1f}")