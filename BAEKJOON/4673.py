def d(n):
    return n + sum(int(digit) for digit in str(n))

generated = set()
for i in range(1, 10001):
    generated.add(d(i))

for i in range(1, 10001):
    if i not in generated:
        print(i)