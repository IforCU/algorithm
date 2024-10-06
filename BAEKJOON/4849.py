while True:
    s = input()
    if s =='.':
        break
    st = []
    check = False
    for ch in s:
        try:
            if ch == '(':
                st.append(ch)
            elif ch == ')':
                if st.pop() != '(':
                    check = True
                    break
            elif ch == '[':
                st.append(ch)
            elif ch == ']':
                if st.pop() != '[':
                    check = True
                    break
        except:
            check = True
            break
    if len(st) == 0 and check == False:
        print('yes')
    else:
        print('no')