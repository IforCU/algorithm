from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

def count_array_sums(T, A, B):
    array_A = defaultdict(int)
    n = len(A)
    for i in range(n):
        current_sum = 0
        for j in range(i,n):
            current_sum += A[j]
            array_A[current_sum] += 1
    
    count = 0
    m = len(B)
    for i in range(m):
        current_sum = 0
        for j in range(i,m):
            current_sum += B[j]
            count += array_A[T-current_sum]

    return count

print(count_array_sums(T, A, B))