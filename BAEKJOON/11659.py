N, M = map(int, input().split())

Number = list(map(int, input().split()))

for i in range(M):
    I, J = map(int, input().split())
    if I == J:
        print(Number[I-1])
    else:
        J = min(J, N)
        print(sum(Number[I-1:J]))
