N = int(input())
arr = list(map(int, input().split()))
dp_max = [1 for _ in range(N)]
dp_min = [1 for _ in range(N)]
min_value = min(arr)
for i in range(1,N):
    max_value = max(dp_max)
    for j in range(i):
        if arr[j] < arr[i]:
            dp_max[i] = max(dp_max[i], dp_max[j] + 1)
        elif dp_max[i] > max_value:
            break

for i in range(N-1,-1,-1):
    max_value = max(dp_min)
    for j in range(N-1,i-1,-1):
        if arr[j] < arr[i]:
            dp_min[i] = max(dp_min[i], dp_min[j] + 1)
        elif dp_min[i] > max_value:
            break

ans = [0 for _ in range(N)]
for i in range(N):
    ans[i] = dp_max[i] + dp_min[i] - 1

print(max(ans))