import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
dic = {}

for i in N_list:
    if dic.get(i,0) == 0:
        dic[i] = 1
    else:
        dic[i] += 1

for i in M_list:
    print(dic.get(i,0),end=' ')