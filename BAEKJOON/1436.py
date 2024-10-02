N = int(input())
count = 0
num = 0
def check(n):
    ch = 0
    for i in str(n):
        if i == '6':
            ch +=1
        else:
            ch = 0
        if ch == 3:
            return True
    return False

while N > count:
    num += 1
    if check(num):
        count += 1
    
print(num)