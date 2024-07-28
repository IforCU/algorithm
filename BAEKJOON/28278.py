import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
commands = data[1:]

stack = []
result = []

i = 0
while i < len(commands):
    if commands[i] == '1':
        i += 1
        X = int(commands[i])
        stack.append(X)
    elif commands[i] == '2':
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif commands[i] == '3':
        result.append(len(stack))
    elif commands[i] == '4':
        if stack:
            result.append(0)
        else:
            result.append(1)
    elif commands[i] == '5':
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
    i += 1

sys.stdout.write('\n'.join(map(str, result)) + '\n')