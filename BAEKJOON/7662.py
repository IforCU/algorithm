import heapq
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())

    isDeleted = [False]*k

    minHeap = []
    maxHeap = []

    for i in range(k):    
        D, N = map(str, input().rstrip().split())
        n = int(N)

        if D == 'I':
            heapq.heappush(minHeap,(n,i))
            heapq.heappush(maxHeap,(-n,i))

        else:
            if n == 1:
                while maxHeap and isDeleted[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)

                if maxHeap:
                    num, key = heapq.heappop(maxHeap)
                    isDeleted[key] = True
            else:
                while minHeap and isDeleted[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                
                if minHeap:
                    num, key = heapq.heappop(minHeap)
                    isDeleted[key] = True
                    
    while maxHeap and isDeleted[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    while minHeap and isDeleted[minHeap[0][1]]:
        heapq.heappop(minHeap)

    if not minHeap:
        print('EMPTY')
    else:
        print(-maxHeap[0][0], minHeap[0][0])