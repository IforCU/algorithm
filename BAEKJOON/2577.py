A = int(input())
B = int(input())
C = int(input())
str = list(map(int,list(str(A*B*C))))
for i in range(10):
    print(str.count(i))