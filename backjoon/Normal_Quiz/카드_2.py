import sys
from collections import deque

N = int(sys.stdin.readline())
DQ = deque(range(N,0,-1))

#print(DQ)
temp = None
while len(DQ)>1:
    DQ.pop()
    #temp= DQ.pop()
    DQ.appendleft(DQ.pop())
    #print(DQ)

       
print(DQ.pop())
    


    