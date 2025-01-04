DDR = list(map(int, input().split()))
DDR.pop()
MAX = float('inf')
curr_dp = [[MAX] * 5 for _ in range(5)]
next_dp = [[MAX] * 5 for _ in range(5)]
curr_dp[0][0] = 0

def move_cost(from_pos , to_pos):
    if from_pos == to_pos:
        return 1
    if from_pos == 0:
        return 2
    if abs(from_pos - to_pos) == 2:
        return 4
    return 3

for step in DDR:
    for l in range(5):
        for r in range(5):
            if curr_dp[l][r] == MAX:
                continue

            if step != r:
                next_dp[step][r] = min(next_dp[step][r], curr_dp[l][r] + move_cost(l,step))

            
            if step != l:
                next_dp[l][step] = min(next_dp[l][step], curr_dp[l][r] + move_cost(r, step))
    curr_dp, next_dp = next_dp, [[MAX] * 5 for _ in range(5)]

print(min(min(row) for row in curr_dp))