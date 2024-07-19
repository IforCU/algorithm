message = list(input().upper())

haspMap = {}

for i in message:
    if(i in haspMap):
        haspMap[i] += 1
    else :
        haspMap[i] = 1
    

maxValue = max(haspMap.values())
duplication = 0
answer = ''

for i in haspMap:
    if haspMap.get(i) == maxValue :
        duplication += 1
        answer = i

if(duplication > 1):
    print("?")
else :
    print(answer)