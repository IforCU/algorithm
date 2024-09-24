N = int(input())
val = []
stk = []
str = input()
for _ in range(N):
    val.append(int(input()))

for char in str:
    if char.isalpha():
        stk.append(val[ord(char) - ord('A')])
    else:
        b = stk.pop()
        a = stk.pop()
        if char == '+':
            stk.append(a+b)
        elif char == '-':
            stk.append(a-b)
        elif char == '*':
            stk.append(a*b)
        else:
            stk.append(a/b)

print(f'{stk[0]:.2f}')