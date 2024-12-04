exp = input().strip()
st = []
ans = ''
for s in exp:
    if s.isalpha():
        ans += s
    else:
        if s == '(':
            st.append(s)
        elif s == '*' or  s == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                ans += st.pop()
            st.append(s)
        elif s == '+' or s == '-':
            while st and st[-1] != '(':
                ans += st.pop()
            st.append(s)
        elif s == ')':
            while st and st[-1] != '(':
                ans += st.pop()
            st.pop()

while st:
    ans += st.pop()

print(ans)