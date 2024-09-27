# 97 ~ 122
s = list(input())
for ch in range(97,123):
    try:
        print(s.index(chr(ch)),end=' ')
    except:
        print('-1',end=' ')
