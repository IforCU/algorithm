N, S = map(int, input().split())
array = list(map(int, input().split()))

left, right = 0, 0
partial_sum = array[0]
ans = 100001

while True:
    if partial_sum < S:
        right += 1
        if right == N:
            break
        partial_sum += array[right]
    else:
        partial_sum -= array[left]
        ans = min(ans, right-left+1)
        left += 1

print(ans if ans != 100001 else 0)

# 부분합
# 투 포인트 알고리즘 활용
# right 값과 left 값을 가지고 부분 값들의 합을 구하는 방식
# 부분합이 목표보다 높으면 left 값을 줄임
# 부분합이 목표보다 낮으면 right 값을 늘림
# 모든 배열을 확인한 후에 목표한 값이 없으면 ans조건에 충족되지 않음
