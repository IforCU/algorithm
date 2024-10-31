from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
people = list(map(int, input().split()))[1:]
party = []
visited = [False for _ in range(M)]

for _ in range(M):
    party.append(list(map(int, input().split()))[1:])

def ch_party(n):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        for i in range(M):
            if not visited[i]:
                if x in party[i]:
                    visited[i] = True
                    queue.extend(j for j in party[i] if j != x and j not in people)

if people:
    for i in people:
        ch_party(i)
    print(visited.count(False))
else:
    print(M)