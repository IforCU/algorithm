from collections import deque
N, K = map(int, input().split())
queue = deque()
for i in range(1,N+1):
    queue.append(i)
ans = []
while queue:
    for i in range(1,K):
        x = queue.popleft()
        queue.append(x)
    res = queue.popleft()
    ans.append(str(res))

print("<",end='')
print(", ".join(ans),end='')
print(">")