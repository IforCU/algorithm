from collections import deque
A, B = map(int, input().split())

def two_times(n):
    return 2*n

def add_right_one(n):
    return n*10 + 1

def bfs(a, b):
    queue = deque()
    queue.append((a,1))
    ans = []
    while queue:
        x, count = queue.popleft()
        x_two = two_times(x)
        x_one = add_right_one(x)
        if x_two == b or x_one == b:
            ans.append(count + 1)
        if x_two < b:
            queue.append((x_two, count + 1))
        if x_one < b:
            queue.append((x_one, count + 1))
    
    if ans:
        return min(ans)
    else:
        return -1

print(bfs(A,B))