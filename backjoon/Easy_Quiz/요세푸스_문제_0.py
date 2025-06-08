import sys
from collections import deque
n, k = map(int, input().split(' '))

#print(n,k)
q =deque(range(n,0,-1))
#print(q)
result = []
if len(q) == 1 :
    result.append(q.pop())
while len(q) != 0:
    for _ in range(k-1):
        q.appendleft(q.pop())
    
    result.append(q.pop())
    #print(q)

print("<",end='')
if len(result) >= 1:
    for i in range(0,len(result)-1):
        print(f'{result[i]},',end=' ')
    print(result[-1],end='')
    
print(">",end='')
#print(result)