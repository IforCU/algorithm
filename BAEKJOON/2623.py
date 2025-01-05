from collections import deque, defaultdict

def music_order(N, M, sequences):
    graph = defaultdict(list)
    in_degree = [0] * (N+1)

    for sequence in sequences:
        for i in range(len(sequence) - 1):
            graph[sequence[i]].append(sequence[i + 1])
            in_degree[sequence[i + 1]] += 1

    queue = deque(sorted([i for i in range(1, N + 1) if in_degree[i] == 0]))
    ans = []
    while queue:
        current = queue.popleft()
        ans.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(ans) != N:
        return [0]
    return ans

N, M = map(int, input().split())
sequences = []
for _ in range(M):
    data = list(map(int, input().split()))
    sequences.append(data[1:])

ans = music_order(N, M, sequences)
if ans == [0]:
    print(0)
else:
    print("\n".join(map(str, ans)))