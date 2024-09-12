N = int(input())

for i in range(1, N + 1):
    A, B = input().split()
    A, B = int(A), int(B)
    result = A + B
    print(f"Case #{i}: {A} + {B} = {result}")
