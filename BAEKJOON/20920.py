N, M  = map(int, input().split())
Map = {}

for i in range(N):
    str = input()
    if(len(str) >= M):
        if str in Map:
            Map[str] += 1
        else:
            Map[str] = 1

def sort_criteria(word):
    return (-Map[word], -len(word), word)

sorted_keys = sorted(Map.keys(), key=sort_criteria)

for key in sorted_keys:
    print(key)
