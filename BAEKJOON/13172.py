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

# 더 간단한 방법
# 문제가 요구하는 것은 a × b^-1 mod X 구하여 sum을 만드는것
# b ^ x-2 =  b^-1  mod X가 성립, 이때 X는 두 수보다 큰 소수
# 즉 a x (b ^ x-2)를 구하는 것 중간 값 마다 mod를 넣어서 나머지를 구해야함.
# pow는 차제적으로 mod(나머지)를 매개 인자값으로 넣을 수 있는 함수
# n, s 에서 s/n 값은  s * pow(n, MOD - 2, MOD)가 구해야 하는 기대값 
# n ^ (MOD-2) * s의 모든 합을 다시 MOD로 나누어주면 됨.
# INF = int(1e9) + 7
# m = int(input())
# a = [list(map(int, input().split())) for _ in range(m)]
# print(sum([s*pow(n,INF-2,INF) for n, s in a]) % INF)