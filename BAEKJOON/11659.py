import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
M = int(data[1])

numbers = list(map(int, data[2:N+2]))

prefix_sums = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sums[i] = prefix_sums[i - 1] + numbers[i - 1]

query_start = N + 2
results = []
for _ in range(M):
    i = int(data[query_start])
    j = int(data[query_start + 1])
    results.append(prefix_sums[j] - prefix_sums[i - 1])
    query_start += 2

sys.stdout.write('\n'.join(map(str, results)) + '\n')
