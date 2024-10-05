N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
answer = float('inf')

def paint_ch(paint):
    if paint == 'W':
        return 'B'
    else:
        return 'W'

def paint_color(start_x, start_y):
    count_w_start, count_b_start = 0, 0
    for i in range(8):
        for j in range(8):
            current_color = board[start_x+i][start_y+j]

            excepted_w = 'W' if (i+j) % 2 == 0 else 'B'
            excepted_b = 'B' if (i+j) % 2 == 0 else 'W'

            if current_color != excepted_w:
                count_w_start += 1
            if current_color != excepted_b:
                count_b_start += 1
    return min(count_w_start, count_b_start)


for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        count = paint_color(i,j)
        answer = min(answer,count)

print(answer)