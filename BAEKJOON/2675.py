N = int(input())
for _ in range(N):
    S, R = input().split()
    S = int(S)
    for s in R:
        print(f'{s}'*S,end='') 
    print('')
