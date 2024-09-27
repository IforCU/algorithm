N = int(input())
for _ in range(N):
    score = 0
    stk = 0
    quiz = list(input())
    for an in  quiz:
        if an == 'O':
            stk += 1
            score += stk
        else:
            stk = 0
    print(score)