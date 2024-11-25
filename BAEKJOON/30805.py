N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

res = []
while A and B:
    max_A = max(A)
    max_B = max(B)
    if max_A == max_B:
        res.append(max_A)
        A = A[A.index(max_A) + 1:]
        B = B[B.index(max_A) + 1:]
    elif max_A > max_B:
        A.remove(max_A)
    else:
        B.remove(max_B)

print(len(res))
if res:
    print(" ".join(map(str, res)))