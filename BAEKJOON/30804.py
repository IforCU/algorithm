import sys
input = sys.stdin.readline
N = int(input())
fruit = list(map(int, input().split()))

def check(queue):
    if len(set(queue)) > 2:
        return False
    return True
count = 0
left = 0
fruit_count = {}

for right in range(0,N):
    if fruit[right] in fruit_count:
        fruit_count[fruit[right]] += 1
    else:
        fruit_count[fruit[right]] = 1
    while len(fruit_count) > 2:
        fruit_count[fruit[left]] -= 1
        if fruit_count[fruit[left]] == 0:
            del fruit_count[fruit[left]]
        left += 1
    count = max(count,right - left + 1)

print(count)