from collections import deque
case = int(input())

def printer(arr):
    max_value = max(arr)
    if arr[0] != max_value:
        arr.append(arr.popleft())
        return False
    else:
        arr.popleft()
        return True

for _ in range(case):
    N, M = map(int, input().split())
    que = deque(list(map(int, input().split())))
    count = 0
    while que:
        if printer(que):
            count += 1
            if M <= 0:
                break
        M -= 1
        if M < 0:
            M = len(que) - 1
    print(count)