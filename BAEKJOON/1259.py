while True:
    s = input()
    check = True
    if s == '0':
        break
    if len(s) == 1:
        print('yes')
        continue
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            check = False
    
    if check:
        print('yes')
    else:
        print('no')