nubmers = []
for _ in range(9):
    nubmers.append(int(input()))
mn = max(nubmers)
print(mn)
print(nubmers.index(mn)+1)