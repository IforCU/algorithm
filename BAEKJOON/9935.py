string = input().rstrip()
exp = input().rstrip()

exp_len = len(exp)
st = []

for char in string:
    st.append(char)
    if char == exp[-1] and ''.join(st[-exp_len:]) == exp:
        del st[-exp_len:]

result = ''.join(st)
print(result if result else 'FRULA')