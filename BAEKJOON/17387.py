import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3- x1)


def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    c1 = ccw(x1, y1, x2, y2, x3, y3)
    c2 = ccw(x1, y1, x2, y2, x4, y4)
    c3 = ccw(x3, y3, x4, y4, x1, y1)
    c4 = ccw(x3, y3, x4, y4, x2, y2)

    if c1 * c2 < 0 and c3 * c4 < 0:
        return 1

    def is_between(x1, y1, x2, y2, x3, y3):
        return min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2)

    if c1 == 0 and is_between(x1, y1, x2, y2, x3, y3):
        return 1
    if c2 == 0 and is_between(x1, y1, x2, y2, x4, y4):
        return 1
    if c3 == 0 and is_between(x3, y3, x4, y4, x1, y1):
        return 1
    if c4 == 0 and is_between(x3, y3, x4, y4, x2, y2):
        return 1
    
    return 0

print(is_intersect(x1, y1, x2, y2, x3, y3, x4, y4))