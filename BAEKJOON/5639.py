import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

tree = {}
N = int(input())

def tree_find(n,k):
    if n in tree:
        if n > k:
            if tree[n][0] != 0:
                tree_find(tree[n][0],k)
            else:
                tree[n] = (k,tree[n][1])
        else:
            if tree[n][1] != 0:
                tree_find(tree[n][1],k)
            else:
                tree[n] = (tree[n][0],k)
    else:
        if n > k:
            tree[n] = (k,0)
        else:
            tree[n] = (0,k)

while True:
    try:
        num = int(input())
        tree_find(N,num)
    except:
        break

def postOrder(n):
    if n in tree:
        if tree[n][0] != 0:
            postOrder(tree[n][0])
        if tree[n][1] != 0:
            postOrder(tree[n][1])
    print(n)

postOrder(N)