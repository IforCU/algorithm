X = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in stick:
    if X >= i:
        count += 1
        X -= i
    
    if X == 0:
        break

print(count)