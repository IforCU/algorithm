list = []
for i in range(10):
    list.append(int(input())%42)

print(len(set(list)))