from typing import Any
import sys



class my_stack:
    
    def __init__(self,capacity)-> None:
        self.stk = [None]* capacity
        self.capacity = capacity
        self.ptr = 0
    
    
    def top(self):
        if self.ptr == 0:
            print(-1)
        else:
            print(self.stk[self.ptr - 1])
        
        
    def push(self, value):
        if self.ptr < self.capacity:
            self.stk[self.ptr] = value
            self.ptr += 1
    
    def pop(self):
        if self.ptr == 0:
            print(-1)
        else:
            self.ptr -= 1
            print(self.stk[self.ptr])
    
    def size(self):
        print(self.ptr)
    
    def empty(self):
        print(1 if self.ptr == 0 else 0)
    
n = int(sys.stdin.readline())

stk= my_stack(n)

for _ in range(n):
    cmd = sys.stdin.readline().strip()
    
    if cmd.startswith("push"):
        _, x =  cmd.split()
        stk.push(int(x))
    elif cmd =="pop":
        stk.pop()   
    elif cmd =="size":
        stk.size()
    elif cmd =="empty":
        stk.empty()
    elif cmd =="top":
        stk.top()
    
    else:
        break