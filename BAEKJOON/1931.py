import sys
input = sys.stdin.readline

N = int(input().rstrip())
meeting = []

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    meeting.append((x, y))

meeting.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meeting:
    if start >= end_time:  
        count += 1
        end_time = end 

print(count)