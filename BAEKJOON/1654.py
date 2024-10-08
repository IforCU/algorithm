K, N = map(int,input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    count = sum(line // mid for line in lines)

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)