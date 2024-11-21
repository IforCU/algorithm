import sys
import math
input = sys.stdin.readline
X = 1000000007

def get_expected_value(n, s):
    return s * get_squared_num(n, X-2) % X

def get_squared_num(num, exp):
    if exp == 1:
        return num

    if exp % 2 == 0:
        half = get_squared_num(num, exp//2)
        return half * half%X
    else:
        return num * get_squared_num(num, exp - 1) % X

M = int(input())

sum = 0
for _ in range(M):
    n, s = map(int, input().split())
    gcd = math.gcd(n, s)
    n //= gcd
    s //= gcd

    sum += get_expected_value(n, s)
    sum %= X
print(sum)