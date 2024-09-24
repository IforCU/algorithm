from collections import deque
N = int(input())
for _ in range(N):
    dq1 = deque()
    dq2 = deque()
    for char in input():
        if char == '<':
            if len(dq1):
                dq2.appendleft(dq1.pop())
        elif char == '>':
            if len(dq2):
                dq1.append(dq2.popleft())
        elif char == '-':
            if len(dq1):
                dq1.pop()
        else:
            dq1.append(char)
    print(''.join(dq1)+ ''.join(dq2))
