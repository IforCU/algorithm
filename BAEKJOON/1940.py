n = int(input())
m = int(input())
array = list(map(int, input().split()))

array.sort()

left , right = 0, n-1
count = 0

while left < right:
    current_sum = array[left] + array[right]
    if current_sum == m:
        count += 1
        left += 1
        right -= 1
    elif current_sum < m:
        left += 1
    else:
        right -= 1

print(count)