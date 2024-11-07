import sys
input = sys.stdin.readline
N, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

def matrix_cal(arr1, arr2):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            s = sum(arr1[row][i] * arr2[i][col] for i in range(N))
            result[row][col] = s % 1000
    return result

def power(n, arr):
    if n == 1:
        return arr
    if n%2 == 0:
        half = power(n//2,arr)
        return matrix_cal(half,half)
    else:
        return matrix_cal(arr, power(n-1, arr))

ans = power(B, matrix)
for i in ans:
    for j in i:
        print(j%1000,end=' ')
    print()