from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    queue = deque(input().rstrip().strip("[]").split(','))
    if queue[0] == '':
        queue.popleft()
    error = False
    direction = True
    for com in p:
        if error:
            break
        if com == 'R':
            direction = not direction
        else:
            if queue:
                if direction:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                error = True
    if error:
        print('error')
    else:
        result = list(queue)
        if not direction:
            result.reverse()
        print('[' + ','.join(result) + ']')