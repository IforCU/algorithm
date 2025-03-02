A, B = map(int, input().split())

ans = 0
p = 1

while p <= B:
    cb = (B + 1) // (p * 2) * p + max(0, (B + 1) % (p * 2) - p)
    ca = A // (p * 2) * p + max(0, A % (p * 2) - p)

    ans += cb - ca
    p *= 2

print(ans)