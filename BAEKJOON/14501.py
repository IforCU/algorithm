import sys
N = int(input())
schedule = []

for i in range(N):
    d, p = map(int, sys.stdin.readline().split())
    schedule.append([d, p])

schedule.reverse()
schedule.insert(0, [])

d = [0] * (N+1)

for i in range(1, N+1):
    if i < schedule[i][0]: # 일 
        d[i] = d[i-1]
    else:
        d[i] = max(d[i-1], schedule[i][1] + d[i - schedule[i][0]])
    
    print(d)

print(d[-1])