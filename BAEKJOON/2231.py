N = int(input())
answer = 0  

for i in range(1, N):  
    total = i + sum(int(digit) for digit in str(i)) 
    if total == N:  
        answer = i  
        break  

print(answer)