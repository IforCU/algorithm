N = int(input()) # 입력 값
stack = [] # Stack 

for _ in range(N): # N만큼 반복
    s = input() # 한줄 입력
    for char in s: # 입력 받은 크기 만큼 실행
        if char == '(':
            stack.append(char)
        else:
            try:
                stack.pop()
            except IndexError: # Stack.pop이 안되면 VPS 성립이 안된다고 판단
                print('NO')
                break
    else: # 만약의 오류를 위한 처리
        if len(stack) == 0: 
            print('YES')
        else:
            print('NO')
    stack = [] 
