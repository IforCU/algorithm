from collections import deque
N, M = map(int, input().split())
positions = list(map(int, input().split()))
queue = deque(range(1, N+1))
ans = 0

for target in positions:
    while queue[0] != target:
        if queue.index(target) <= len(queue) // 2:
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())
        ans += 1
    queue.popleft()

print(ans)