import heapq
import sys


heap=[0]


n = int(input())
for _ in range(n) :
    input1 = int(sys.stdin.readline())
    
    if input1 == 0:
        if heap[0] != 0:
            print(-heapq.heappop(heap))
        else:
            print(heap[0])
    
    else:
        heapq.heappush(heap,-input1)
            