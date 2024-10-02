A = input()
B = input()
C = input()
i = 0
if str.isdigit(A):
    i = 3 + int(A)
elif str.isdigit(B):
    i = 2 + int(B)
else:
    i = 1 + int(C)

if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
elif i % 3 == 0:
    print('Fizz')
elif i % 5 == 0:
    print('Buzz')
else:
    print(i)