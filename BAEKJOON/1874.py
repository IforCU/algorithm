import sys
input = sys.stdin.readline
n = int(input())
stack = []
com = []
failure = False
count = 1
for _ in range(n):
    num = int(input())

    while count <= num:
        stack.append(count)
        com.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        com.append('-')
    else:
        failure = True

if failure:
    print('NO')
else:
    for ch in com:
        print(ch)
