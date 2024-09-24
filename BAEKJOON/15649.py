import itertools

N, M = map(int, input().split())

nb = list(range(1, N+1))
for perm in itertools.permutations(nb,M):
    print(*perm)