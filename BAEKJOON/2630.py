import sys
input = sys.stdin.readline
N = int(input().rstrip())
maps = [0] * N
for i in range(N):
    maps[i] = list(map(int, input().rstrip().split()))

def count_paper(x,y,size):
    global color, white
    now_color = maps[y][x]
    is_single_color = True

    for i in range(y,y+size):
        for j in range(x,x+size):
            if maps[i][j] != now_color:
                is_single_color = False
                break
        if not is_single_color:
            break
    
    if is_single_color:
        if now_color == 1:
            color += 1
        else:
            white += 1
    else:
        half_size = size//2
        count_paper(x, y, half_size)
        count_paper(x + half_size,y, half_size)
        count_paper(x,y + half_size, half_size)
        count_paper(x + half_size, y + half_size, half_size)

color = 0
white = 0

count_paper(0,0,N)

print(white)
print(color)