N = int(input())
n = list(map(int, input().split()))
n.sort()
M = int(input())
m = list(map(int, input().split()))

def list_find(list, x):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == x:
            return True
        elif list[mid] > x:
            end = mid -1
        else:
            start = mid + 1
    return False
 

for i in m:
    if list_find(n,i):
        print('1')
    else:
        print('0')
    