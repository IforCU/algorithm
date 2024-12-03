MOD = 1000000007

def matrix_mul(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]

def matrix_pow(matrix, exp):
    result = [[1, 0], [0, 1]]
    base = matrix

    while exp > 0:
        if exp % 2 == 1:
            result = matrix_mul(result, base)
        base = matrix_mul(base, base)
        exp //= 2

    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1)
    return result[0][0]

n = int(input())
print(fibonacci(n))