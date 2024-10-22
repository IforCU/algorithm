from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

def D(n : int):
    return (n*2)%10000

def S(n : int):
    if n == 0 :
        return 9999
    else:
        return n-1
    
def L(n : int):
    return (n%1000) * 10 + (n//1000)

def R(n : int):
    return (n//10) + (n%10) * 1000

def bfs(A, B):
    queue = deque()
    queue.append((A,''))
    visited = [False for _ in range(10001)]
    while queue:
        x, com = queue.popleft()
        XD = D(x)
        XS = S(x)
        XL = L(x)
        XR = R(x)

        if XD == B:
            return com+'D'
        elif XS == B:
            return com+'S'
        elif XL == B:
            return com+'L'
        elif XR == B:
            return com+'R'

        if not visited[XD]:
            queue.append((XD, com+'D'))
            visited[XD] = True
        if not visited[XS]:
            queue.append((XS, com+'S'))
            visited[XS] = True
        if not visited[XL]:
            queue.append((XL, com+'L'))
            visited[XL] = True
        if not visited[XR]:
            queue.append((XR, com+'R'))
            visited[XR] = True

for _ in range(T):
    A, B = map(int, input().rstrip().split())
    print(bfs(A, B))