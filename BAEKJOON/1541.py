s = str(input())

num = list(s.split('-'))

for i in range(len(num)):
    if '+' in num[i]:
        num[i] = sum(list(map(int, num[i].split('+'))))
    else:
        num[i] = int(num[i])

if len(num) == 1:
    print(num[0])
else:
    a = num[0] * 2
    for i in num:
        a -= i
    print(a)