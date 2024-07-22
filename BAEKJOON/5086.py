while 1:
    M, N = map(int, input().split())

    if(M == 0 & N == 0):
        break
    
    if(N%M == 0 ):
        print("factor")
    elif(M%N == 0):
        print("multiple")
    else:
        print("neither")
