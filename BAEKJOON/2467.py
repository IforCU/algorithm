N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left = 0
right = N-1

solutions_sum = float('inf')
ans = (0,0)

while left < right:
    cur_sum = solutions[left] + solutions[right]

    if abs(cur_sum) < abs(solutions_sum):
        solutions_sum = cur_sum
        ans = (solutions[left], solutions[right])

    if cur_sum < 0:
        left += 1
    else:
        right -= 1

print(min(ans), max(ans))