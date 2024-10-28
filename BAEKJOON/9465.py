import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr_one = list(map(int, input().split()))
    arr_two = list(map(int, input().split()))
    dp_one = [0 for _ in range(n)]
    dp_two = [0 for _ in range(n)]
    dp_one[0] = arr_one[0]
    dp_two[0] = arr_two[0]

    for i in range(1,n):
        dp_one[i] = max(dp_one[i-1], dp_two[i-1]+arr_one[i])
        dp_two[i] = max(dp_two[i-1], dp_one[i-1]+arr_two[i])
    
    print(max(dp_one[-1], dp_two[-1]))