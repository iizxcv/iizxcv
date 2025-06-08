import sys

stk=[]
num = int(sys.stdin.readline())

for _ in range(num):
    i =int(sys.stdin.readline())
    if i == 0:
        stk.pop()
    else:    
        stk.append(i)

print(sum(stk))